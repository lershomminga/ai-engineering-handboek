# Starter Skeleton

Begin hier. Vul de 12 TODO's in om de capstone af te maken.

## Folder-layout

```
starter/
├── README.md           # dit bestand
├── requirements.txt
├── docker-compose.yml  # Postgres + Redis + Langfuse self-host
├── .env.example
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI webhook ingress (TODO 1-3)
│   ├── guardrails.py   # Presidio + Llama Guard (TODO 4-5)
│   ├── classify.py     # Haiku structured output (TODO 6)
│   ├── rag.py          # Voyage + pgvector + Cohere (TODO 7-9)
│   ├── generate.py     # Sonnet + faithfulness check (TODO 10)
│   ├── action.py       # Auto-reply vs Slack-escalate (TODO 11)
│   └── observability.py # Langfuse spans (TODO 12)
├── evals/
│   └── cases.jsonl     # 30 test-tickets
└── tests/
    └── test_e2e.py     # Pytest E2E suite
```

## 12 TODO's (in volgorde)

1. **TODO 1** — FastAPI webhook endpoint `/webhook/zendesk`
2. **TODO 2** — JWT-auth voor admin-endpoints
3. **TODO 3** — Cost-tracking insert in Postgres per request
4. **TODO 4** — Presidio NL-config met IBAN/BSN/RSIN-recognizers
5. **TODO 5** — Llama Guard 3 1B als input-classifier
6. **TODO 6** — Classify ticket met structured output (Pydantic)
7. **TODO 7** — Voyage embeddings + contextual retrieval setup
8. **TODO 8** — Hybrid search (BM25 + RRF)
9. **TODO 9** — Cohere Rerank v3 als final stage
10. **TODO 10** — Generate antwoord + RAGAS faithfulness check
11. **TODO 11** — Auto-reply vs Slack-escalate beslissingsboom
12. **TODO 12** — Langfuse trace per ticket met parent/child spans

## Start

```bash
cp .env.example .env
# Vul alle keys in
docker compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Eval-suite runnen

```bash
pytest tests/test_e2e.py -v
# Of voor CI:
python -m pytest tests/ --json-report --json-report-file=results.json
```

## Pass-criteria

Zie `../README.md` rubric. Mikken op ≥18/23 voor senior-niveau.
