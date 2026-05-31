"""
04 — Hybrid search + Cohere Rerank v3 als final stage.
Stack: retrieve top-50 (hybrid) → rerank naar top-5 met cross-encoder.

In productie: +30-50% precision op moeilijke queries, +25ms p95 latency.
Vereist COHERE_API_KEY (gratis tier 1000 calls/maand).
"""
import os
from dotenv import load_dotenv
import cohere
# Hergebruik hybrid-search uit 02
from importlib import import_module
hybrid = import_module("02_hybrid_search")

load_dotenv()
co = cohere.Client(os.environ["COHERE_API_KEY"])


def search_with_rerank(query: str, top_k: int = 3) -> list[dict]:
    # Stap 1: hybrid retrieve top-15 candidates
    candidates = hybrid.hybrid_search(query, k=15)
    docs = [c[1] for c in candidates]

    # Stap 2: rerank met Cohere
    reranked = co.rerank(
        model="rerank-multilingual-v3.0",   # NL-vriendelijk
        query=query,
        documents=docs,
        top_n=top_k,
    )
    return [
        {
            "text": docs[r.index],
            "relevance_score": r.relevance_score,
            "original_id": candidates[r.index][0],
        }
        for r in reranked.results
    ]


def main() -> None:
    query = "Wat veranderde in maart 2026 rond caching?"
    print(f"Q: {query}\n")
    results = search_with_rerank(query)
    for i, r in enumerate(results, 1):
        print(f"[{i}] relevance={r['relevance_score']:.3f}")
        print(f"    {r['text'][:120]}...\n")


if __name__ == "__main__":
    main()
