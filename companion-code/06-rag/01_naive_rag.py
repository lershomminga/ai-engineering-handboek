"""
01 — Naive RAG: embed + cosine search + LLM.
Baseline om mee te vergelijken.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg
from pgvector.psycopg import register_vector
import voyageai
from anthropic import Anthropic

load_dotenv()
voyage = voyageai.Client()
anthropic = Anthropic()
DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/handbook")


def load_chunks() -> list[str]:
    """Parseer seed_data/docs.txt — split op '--- DOC' markers."""
    text = Path(__file__).parent.joinpath("seed_data/docs.txt").read_text()
    raw = text.split("--- DOC")
    return [c.strip() for c in raw if c.strip()]


def setup_db(chunks: list[str]) -> None:
    """Maak tabel + embed + insert."""
    with psycopg.connect(DB_URL) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute("DROP TABLE IF EXISTS docs")
            cur.execute("""
                CREATE TABLE docs (
                    id SERIAL PRIMARY KEY,
                    text TEXT NOT NULL,
                    embedding VECTOR(1024)
                )
            """)
            # Embed in batch (voyage-3 = 1024 dim)
            embeddings = voyage.embed(chunks, model="voyage-3").embeddings
            for chunk, emb in zip(chunks, embeddings):
                cur.execute("INSERT INTO docs (text, embedding) VALUES (%s, %s)",
                            (chunk, emb))
            conn.commit()
            print(f"Indexed {len(chunks)} chunks.")


def retrieve(query: str, k: int = 3) -> list[str]:
    q_emb = voyage.embed([query], model="voyage-3").embeddings[0]
    with psycopg.connect(DB_URL) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT text FROM docs ORDER BY embedding <=> %s LIMIT %s",
                (q_emb, k),
            )
            return [r[0] for r in cur.fetchall()]


def answer(query: str) -> str:
    chunks = retrieve(query)
    context = "\n\n---\n\n".join(chunks)
    resp = anthropic.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": (
                f"Beantwoord op basis van deze context:\n\n{context}\n\n"
                f"Vraag: {query}"
            ),
        }],
    )
    return resp.content[0].text


def main() -> None:
    chunks = load_chunks()
    setup_db(chunks)

    queries = [
        "Wat kost prompt caching?",
        "Hoe werkt MCP transport in 2026?",
        "Wat is de token-tax voor Nederlands?",
    ]
    for q in queries:
        print(f"\nQ: {q}")
        print(f"A: {answer(q)}")


if __name__ == "__main__":
    main()
