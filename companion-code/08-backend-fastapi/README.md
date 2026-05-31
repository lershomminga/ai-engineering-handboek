# 08 — Backend (FastAPI + streaming + auth + rate-limit)

Productie-baseline voor een Claude-backed chat-API.

## Features

- **Streaming SSE** met disconnect-detect
- **JWT-auth** (HS256)
- **Sliding-window rate-limit** per user via Redis
- **Cost-tracking** insert in Postgres per call
- **Idempotency-key** header support
- **OTEL spans** (basic)

## Run

```bash
docker compose up -d   # Postgres + Redis
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Test:
curl -N -H "Authorization: Bearer $(python -c 'import jwt; print(jwt.encode({\"sub\":\"user_1\"}, \"your-jwt-secret-min-32-chars\", \"HS256\"))')" \
  -H "Content-Type: application/json" \
  -d '{"message":"Hallo"}' \
  http://localhost:8000/chat
```
