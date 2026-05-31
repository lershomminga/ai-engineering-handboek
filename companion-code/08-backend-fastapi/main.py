"""
Production-baseline FastAPI backend voor Claude chat-API.

Features:
  - Streaming SSE met disconnect-detect
  - JWT-auth (HS256)
  - Sliding-window rate-limit per user via Redis
  - Cost-tracking insert in Postgres per call
  - Idempotency-key support (24u dedup-window)
"""
import os
import time
import json
import asyncio
from typing import Annotated
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import jwt
import redis.asyncio as redis
import psycopg
from fastapi import FastAPI, Depends, HTTPException, Header, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from anthropic import AsyncAnthropic

load_dotenv()

JWT_SECRET = os.environ["JWT_SECRET"]
DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/handbook")
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

claude = AsyncAnthropic()
rds: redis.Redis | None = None
db_conn: psycopg.AsyncConnection | None = None

# Pricing per 1M tokens
PRICES = {
    "claude-haiku-4-5": {"in": 0.80, "out": 4.00},
    "claude-sonnet-4-6": {"in": 3.00, "out": 15.00},
    "claude-opus-4-7": {"in": 15.00, "out": 75.00},
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rds, db_conn
    rds = redis.from_url(REDIS_URL, decode_responses=True)
    db_conn = await psycopg.AsyncConnection.connect(DB_URL, autocommit=True)
    async with db_conn.cursor() as cur:
        await cur.execute("""
            CREATE TABLE IF NOT EXISTS llm_calls (
                id SERIAL PRIMARY KEY,
                user_id TEXT NOT NULL,
                model TEXT NOT NULL,
                input_tokens INT,
                output_tokens INT,
                cost_usd NUMERIC(10, 6),
                idempotency_key TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW()
            )
        """)
        await cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_idempotency
            ON llm_calls(idempotency_key) WHERE idempotency_key IS NOT NULL
        """)
    yield
    await rds.close()
    await db_conn.close()


app = FastAPI(lifespan=lifespan)


# --- Auth ---
async def current_user(authorization: Annotated[str | None, Header()] = None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing Bearer token")
    token = authorization[7:]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload["sub"]
    except jwt.PyJWTError as e:
        raise HTTPException(401, f"Invalid JWT: {e}")


# --- Rate-limit (sliding window) ---
async def check_rate_limit(user_id: str, limit_per_minute: int = 30) -> None:
    """Token-bucket via Redis sorted-set: 30 req/min/user."""
    now = time.time()
    key = f"rl:{user_id}"
    async with rds.pipeline() as pipe:
        pipe.zremrangebyscore(key, 0, now - 60)
        pipe.zcard(key)
        pipe.zadd(key, {str(now): now})
        pipe.expire(key, 60)
        _, count, _, _ = await pipe.execute()
    if count >= limit_per_minute:
        raise HTTPException(429, f"Rate limit {limit_per_minute}/min exceeded")


# --- Idempotency check ---
async def check_idempotency(key: str) -> dict | None:
    """Als deze key recent gebruikt: retour cached resultaat."""
    async with db_conn.cursor() as cur:
        await cur.execute(
            "SELECT cost_usd, created_at FROM llm_calls "
            "WHERE idempotency_key = %s AND created_at > NOW() - INTERVAL '24 hours' "
            "LIMIT 1",
            (key,),
        )
        row = await cur.fetchone()
        return {"cost_usd": row[0], "created_at": row[1]} if row else None


# --- Endpoint ---
class ChatRequest(BaseModel):
    message: str
    model: str = "claude-haiku-4-5"


@app.post("/chat")
async def chat(
    req: ChatRequest,
    request: Request,
    user_id: str = Depends(current_user),
    idempotency_key: str | None = Header(None, alias="Idempotency-Key"),
):
    await check_rate_limit(user_id)

    # Idempotency
    if idempotency_key:
        cached = await check_idempotency(idempotency_key)
        if cached:
            return {"status": "cached", "from": cached["created_at"].isoformat()}

    async def event_stream():
        input_tokens = 0
        output_tokens = 0
        full_text = ""

        async with claude.messages.stream(
            model=req.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": req.message}],
        ) as stream:
            async for text in stream.text_stream:
                # Disconnect-detect
                if await request.is_disconnected():
                    print(f"Client disconnected: {user_id}")
                    return
                full_text += text
                yield f"data: {json.dumps({'text': text})}\n\n"

            final = await stream.get_final_message()
            input_tokens = final.usage.input_tokens
            output_tokens = final.usage.output_tokens

        # Cost-tracking insert
        prices = PRICES.get(req.model, {"in": 3, "out": 15})
        cost = (input_tokens * prices["in"] + output_tokens * prices["out"]) / 1_000_000
        async with db_conn.cursor() as cur:
            await cur.execute(
                "INSERT INTO llm_calls (user_id, model, input_tokens, output_tokens, cost_usd, idempotency_key) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (user_id, req.model, input_tokens, output_tokens, cost, idempotency_key),
            )
        yield f"data: {json.dumps({'done': True, 'cost_usd': cost})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/cost/{user_id}")
async def get_user_cost(user_id: str, _: str = Depends(current_user)):
    """Geef totale spend per user (laatste 30 dagen)."""
    async with db_conn.cursor() as cur:
        await cur.execute(
            "SELECT COUNT(*), COALESCE(SUM(cost_usd), 0) FROM llm_calls "
            "WHERE user_id = %s AND created_at > NOW() - INTERVAL '30 days'",
            (user_id,),
        )
        n, total = await cur.fetchone()
        return {"user_id": user_id, "calls_30d": n, "spend_usd_30d": float(total)}
