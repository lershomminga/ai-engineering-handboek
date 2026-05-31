"""
03 — Anthropic Contextual Retrieval (sept 2024).
Voor elk chunk: Haiku genereert een 50-100 woord context-prefix die het
chunk relateert aan het hele document. Embed daarna chunk + context-prefix.

Resultaat (Anthropic-benchmark): -35% retrieval errors alleen al,
-49% met BM25, -67% met reranking erbovenop.

Trick: gebruik prompt-caching op het document → bij 100 chunks/doc is
de doc-tekst 100× cached. Eenmalige cost-impact daardoor laag.
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

CONTEXT_PROMPT = """<document>
{document}
</document>

Hier is een chunk uit dit document:
<chunk>
{chunk}
</chunk>

Geef een korte (max 60 woorden) context die dit chunk situeert binnen het
hele document, zodat search-systemen het beter terugvinden. Antwoord ALLEEN
met de context, geen voorwoord."""


def load_full_doc() -> str:
    return Path(__file__).parent.joinpath("seed_data/docs.txt").read_text()


def chunks_with_context(full_doc: str, chunks: list[str]) -> list[str]:
    """Voor elk chunk: Haiku genereert context-prefix. Met caching op doc."""
    contextualized = []
    for chunk in chunks:
        resp = anthropic.messages.create(
            model="claude-haiku-4-5",
            max_tokens=200,
            system=[{
                "type": "text",
                "text": CONTEXT_PROMPT.format(document=full_doc, chunk=chunk),
                "cache_control": {"type": "ephemeral"},  # cache hele doc
            }],
            messages=[{"role": "user", "content": "Genereer de context."}],
        )
        context = resp.content[0].text.strip()
        contextualized.append(f"{context}\n\n{chunk}")
        print(f"  [cache_read={resp.usage.cache_read_input_tokens}, "
              f"cache_write={resp.usage.cache_creation_input_tokens}]")
    return contextualized


def setup_contextual_db(full_doc: str, chunks: list[str]) -> None:
    print(f"Contextualiseren van {len(chunks)} chunks (Haiku)...")
    contextualized = chunks_with_context(full_doc, chunks)

    with psycopg.connect(DB_URL) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS docs_contextual")
            cur.execute("""
                CREATE TABLE docs_contextual (
                    id SERIAL PRIMARY KEY,
                    text TEXT NOT NULL,
                    embedding VECTOR(1024)
                )
            """)
            embeddings = voyage.embed(contextualized, model="voyage-3").embeddings
            for chunk, emb in zip(contextualized, embeddings):
                cur.execute("INSERT INTO docs_contextual (text, embedding) VALUES (%s, %s)",
                            (chunk, emb))
            conn.commit()
            print(f"Indexed {len(chunks)} contextualized chunks.")


def main() -> None:
    full_doc = load_full_doc()
    raw_chunks = [c.strip() for c in full_doc.split("--- DOC") if c.strip()]
    setup_contextual_db(full_doc, raw_chunks)
    print("\nDone. Run 02_hybrid_search.py met 'docs_contextual' tabel om")
    print("verschil te zien op een vage query als 'Wat veranderde in maart?'")


if __name__ == "__main__":
    main()
