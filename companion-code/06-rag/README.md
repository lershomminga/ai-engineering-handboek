# 06 — RAG (Retrieval-Augmented Generation)

Van naive vector-search → hybrid → contextual → reranked.

## Setup

```bash
# Start Postgres + pgvector (eénmalig)
docker compose up -d

# Wacht 10s, dan:
psql postgresql://postgres:postgres@localhost:5432/handbook -c "CREATE EXTENSION IF NOT EXISTS vector;"

# Python deps
pip install -r requirements.txt
python 01_naive_rag.py    # bouwt index + run eerste query
```

## Scripts

| # | Bestand | Niveau |
|---|---|---|
| 01 | `01_naive_rag.py` | Embed + cosine search + LLM (baseline) |
| 02 | `02_hybrid_search.py` | + BM25 + Reciprocal Rank Fusion |
| 03 | `03_contextual_retrieval.py` | Anthropic Contextual Retrieval (-67% errors) |
| 04 | `04_with_reranker.py` | + Cohere Rerank v3 |

Elke stap voegt iets toe — vergelijk de outputs op dezelfde query.

## Seed data

10 sample docs over Anthropic features in `seed_data/`.
