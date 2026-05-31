"""
Capstone — main entrypoint (FastAPI webhook ingress).

Vul 12 TODO's in (zie ../README.md).
"""
import os
import hmac
import hashlib
from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Header, HTTPException, BackgroundTasks
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Customer Support Agent — Capstone")


class ZendeskTicket(BaseModel):
    ticket_id: str
    subject: str
    body: str
    customer_email: str
    customer_name: str | None = None


# === TODO 1: Webhook endpoint ===
@app.post("/webhook/zendesk")
async def zendesk_webhook(
    ticket: ZendeskTicket,
    request: Request,
    background: BackgroundTasks,
    x_zendesk_signature: Annotated[str | None, Header()] = None,
):
    # TODO 1a: Verify HMAC-signature
    raw_body = await request.body()
    expected = hmac.new(
        os.environ["ZENDESK_WEBHOOK_SECRET"].encode(),
        raw_body,
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(expected, x_zendesk_signature or ""):
        raise HTTPException(401, "Invalid signature")

    # TODO 1b: Enqueue ticket voor async processing
    # background.add_task(process_ticket, ticket)
    raise NotImplementedError("Implement TODO 1b: enqueue async processing")


# === TODO 2: JWT-auth voor admin-endpoints ===
# from app.auth import current_admin

# @app.get("/admin/queue", dependencies=[Depends(current_admin)])
# async def get_queue(): ...


# === TODO 3: Cost-tracking ===
# Zie 08-backend-fastapi/main.py voor pattern. Insert per LLM-call:
#   user_id, ticket_id, model, input_tokens, output_tokens, cost_usd, stage


# === Main processing pipeline ===
async def process_ticket(ticket: ZendeskTicket) -> dict:
    """De volledige flow — zie ../ARCHITECTURE.md."""

    # TODO 4-5: Guardrails (PII-redact + Llama Guard)
    # redacted = await guardrails.process(ticket)

    # TODO 6: Classify
    # classification = await classify.run(redacted)

    # TODO 7-9: RAG (only voor FAQ-categorie)
    # if classification.category in {"billing", "shipping", "product"}:
    #     chunks = await rag.retrieve(redacted.body)

    # TODO 10: Generate
    # draft = await generate.run(redacted, chunks, classification)

    # TODO 11: Action gate (auto-reply vs escalate)
    # await action.dispatch(draft, classification)

    # TODO 12: Observability — span per stage
    # langfuse_trace.update(...)

    raise NotImplementedError("Implement TODO 4-12")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
