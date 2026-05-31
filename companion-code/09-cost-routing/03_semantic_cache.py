"""
03 — Semantic cache: embed query, vergelijk met vorige queries.
Bij similarity > threshold: return cached answer.
Hit-rates 20-40% in support-bots, tot 73% in case-studies.
"""
import os
from dotenv import load_dotenv
import numpy as np
import voyageai
from anthropic import Anthropic

load_dotenv()
voyage = voyageai.Client()
client = Anthropic()


class SemanticCache:
    def __init__(self, threshold: float = 0.92):
        self.threshold = threshold
        self.cache: list[dict] = []  # [{query_emb, answer, hits, original_query}]

    def get_or_call(self, user_msg: str) -> dict:
        q_emb = np.array(voyage.embed([user_msg], model="voyage-3").embeddings[0])

        # Check cache
        for entry in self.cache:
            sim = np.dot(q_emb, entry["query_emb"]) / (
                np.linalg.norm(q_emb) * np.linalg.norm(entry["query_emb"])
            )
            if sim >= self.threshold:
                entry["hits"] += 1
                return {"answer": entry["answer"], "cached": True,
                        "similarity": float(sim),
                        "original_query": entry["original_query"]}

        # Cache miss → call LLM
        resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=300,
            messages=[{"role": "user", "content": user_msg}],
        )
        answer = resp.content[0].text
        self.cache.append({
            "query_emb": q_emb,
            "answer": answer,
            "hits": 0,
            "original_query": user_msg,
        })
        return {"answer": answer, "cached": False}

    def stats(self) -> dict:
        total_hits = sum(e["hits"] for e in self.cache)
        total_queries = total_hits + len(self.cache)
        return {
            "cache_size": len(self.cache),
            "total_queries": total_queries,
            "hit_rate": total_hits / total_queries if total_queries else 0,
        }


def main() -> None:
    cache = SemanticCache(threshold=0.92)

    # Simuleer support-bot met semantisch overlappende queries
    queries = [
        "Hoe annuleer ik mijn abonnement?",
        "Wat kost Claude Haiku per 1M tokens?",
        "Hoe zeg ik mijn abonnement op?",       # semantisch identiek aan #1
        "Hoeveel kost Haiku per miljoen tokens?",  # ~identiek aan #2
        "Waar reset ik mijn wachtwoord?",
        "Cancel mijn membership alsjeblieft",    # weer #1
    ]

    for q in queries:
        r = cache.get_or_call(q)
        cache_label = "HIT " if r["cached"] else "MISS"
        sim = f"(sim={r['similarity']:.3f})" if r["cached"] else ""
        print(f"{cache_label} {sim:<15} {q}")

    print(f"\n{cache.stats()}")


if __name__ == "__main__":
    main()
