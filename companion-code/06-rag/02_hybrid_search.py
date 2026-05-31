"""
02 — Hybrid search: BM25 + dense vector + Reciprocal Rank Fusion.
Vereist dat 01_naive_rag.py al gerund is (DB is gevuld).
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import psycopg
from pgvector.psycopg import register_vector
from rank_bm25 import BM25Okapi
import voyageai

load_dotenv()
voyage = voyageai.Client()
DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/handbook")


def get_all_chunks() -> list[tuple[int, str]]:
    """Laad alle chunks uit DB voor BM25-indexering in-memory."""
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, text FROM docs ORDER BY id")
            return cur.fetchall()


def hybrid_search(query: str, k: int = 5) -> list[tuple[int, str, float]]:
    """RRF fusion van BM25 + dense vector. K_RRF=60 default."""
    chunks = get_all_chunks()
    ids = [c[0] for c in chunks]
    texts = [c[1] for c in chunks]

    # BM25 ranking
    bm25 = BM25Okapi([t.lower().split() for t in texts])
    bm25_scores = bm25.get_scores(query.lower().split())
    bm25_top = np.argsort(bm25_scores)[::-1][:k * 2]  # neem top-2k

    # Dense ranking
    q_emb = voyage.embed([query], model="voyage-3").embeddings[0]
    with psycopg.connect(DB_URL) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, embedding <=> %s AS dist FROM docs ORDER BY dist LIMIT %s",
                (q_emb, k * 2),
            )
            dense_ranking = [r[0] for r in cur.fetchall()]
    dense_top = [ids.index(did) for did in dense_ranking]

    # RRF fusion
    K_RRF = 60
    rrf: dict[int, float] = {}
    for rank, idx in enumerate(bm25_top):
        rrf[idx] = rrf.get(idx, 0) + 1 / (K_RRF + rank)
    for rank, idx in enumerate(dense_top):
        rrf[idx] = rrf.get(idx, 0) + 1 / (K_RRF + rank)

    fused = sorted(rrf.items(), key=lambda x: -x[1])[:k]
    return [(ids[idx], texts[idx], score) for idx, score in fused]


def main() -> None:
    queries = [
        "Wat kost prompt caching?",
        "Hoe werkt MCP transport in 2026?",
        "Workload Identity Federation",   # keyword-heavy → BM25 helpt
    ]
    for q in queries:
        print(f"\nQ: {q}")
        results = hybrid_search(q, k=3)
        for i, (id_, text, score) in enumerate(results, 1):
            print(f"  [{i}] (id={id_}, score={score:.4f}) {text[:100]}...")


if __name__ == "__main__":
    main()
