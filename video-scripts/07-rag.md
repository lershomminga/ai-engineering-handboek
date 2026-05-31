# 07 — RAG · richtduur 30-40 min

De grootste build-along. Companion-code `06-rag` heeft docker-compose + 4 stages —
de kijker bouwt mee.

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "RAG is niet 'stop het in een vector-database'. Dat is de naive versie die
> in productie faalt. Ik bouw live de hele pijplijn op — van naive cosine-search
> naar hybrid + contextual + reranked — en je ziet bij elke stap de kwaliteit
> omhoog gaan."
>
> *Toon:* de RAG-module + Schema #11 (RAG full pipeline).

## 📋 LEERDOELEN
Embeddings, chunking, de vier retrieval-stages, en wanneer je RAG juist NIET moet
gebruiken.

## 🎬 BEATS

**Beat 1 — De RAG-flow + setup (0:30-5:00)**
- *Zeg:* offline (chunk→embed→store) vs online (query→retrieve→generate).
- *Toon:* `06-rag/` — `docker compose up -d` live, pgvector draait. Toon de
  10 seed-docs in `seed_data/docs.txt`.

**Beat 2 — Stage 1: Naive RAG (5:00-12:00)**
- *Zeg:* embeddings = betekenis als vector, cosine-similarity = afstand.
- *Toon:* `01_naive_rag.py` — run live, bouwt de index, beantwoordt 3 queries.
  Laat een query zien die het naive systeem mist (vage/keyword-query).

**Beat 3 — Stage 2: Hybrid search (12:00-20:00)**
- *Zeg:* "BM25 vangt exacte termen, dense vangt betekenis. RRF fuset ze."
- *Toon:* `02_hybrid_search.py` — run op "Workload Identity Federation" (keyword-
  heavy) en laat zien hoe BM25 die redt waar pure vector faalt.
- *⚠ Noem:* leg de RRF-formule kort uit (k=60), maar blijf praktisch.

**Beat 4 — Stage 3: Contextual Retrieval (20:00-28:00)**
- *Zeg:* "Anthropic's truc: Haiku schrijft per chunk een context-prefix vóór het
  embedden. -67% retrieval errors. En met prompt-caching op het document bijna gratis."
- *Toon:* `03_contextual_retrieval.py` — run live, wijs op de `cache_read` vs
  `cache_write` tokens in de output (de caching-truc in actie).

**Beat 5 — Stage 4: Reranking (28:00-33:00)**
- *Zeg:* "Cross-encoder als laatste stap: retrieve 15, rerank naar top-5."
- *Toon:* `04_with_reranker.py` — run, laat de relevance-scores zien.

**Beat 6 — Wanneer NIET RAG (33:00-37:00)**
- *Zeg:* "Past alles in 200k context en is het statisch? Stuur het gewoon mee. RAG
  is complexity — gebruik 'm alleen als je 'm nodig hebt."
- *Toon:* de "wanneer NIET RAG"-sectie + de vector-DB-tradeoffs-tabel.

## 🔁 RECAP + CTA (37:00-38:30)
> *Zeg:* "Het 2026-recept: contextual ingest → hybrid + RRF → reranker → cache.
> Maar hoe weet je dat je RAG goed is? Volgende video: evals — we meten het."
