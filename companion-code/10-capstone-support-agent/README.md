# 10 — Capstone: Production-Ready Customer Support Agent

Build één concreet project dat alles uit het handboek raakt.

## Wat ga je bouwen?

Een **customer support agent** die:

1. Tickets ontvangt via webhook (Inngest of FastAPI direct)
2. Classificeert (billing / shipping / product / complaint / spam)
3. Bij FAQ → direct antwoord via **RAG** over je docs
4. Bij escalatie → context optrekt + **drafted reply** voor human review
5. Logged elke stap naar **Langfuse** (observability)
6. Tracked **cost per ticket** in Postgres
7. Geslaagd: **eval-suite** van 30 testtickets in CI

## Modules die je raakt

| Wat | Module |
|---|---|
| Prompt design | Prompting Basics + Advanced + Patterns |
| Structured output | Structured Outputs |
| RAG-pipeline | RAG |
| Tool use | Tools & MCP |
| Agent loop | Agents |
| Cost-tracking | Cost Opt + Backend |
| Observability | Observability |
| Evals | Evals |
| Frontend (admin-UI) | Frontend + AI UX |
| Security (PII-redact) | Security + Guardrails |

## Rubric — 10 criteria

| # | Criterium | Gewicht | Pass-bar |
|---|---|---:|---|
| 1 | Prompt design (system + format + few-shot) | 3 | ≥ 80% classify-accuracy |
| 2 | Structured output (Pydantic + retry) | 2 | 100% schema-compliance |
| 3 | RAG-quality (contextual + hybrid) | 3 | ≥ 0.85 RAGAS faithfulness |
| 4 | Tool reliability (geen silent fails) | 2 | ≥ 95% success-rate |
| 5 | Cost-tracking per ticket in DB | 2 | werkt + dashboard |
| 6 | Observability (Langfuse spans) | 2 | trace per ticket compleet |
| 7 | Security (PII-redact + system isolation) | 3 | Presidio test-set 100% |
| 8 | Eval-suite (30 cases + CI gate) | 3 | green op main |
| 9 | Admin-UI (queue + override) | 1 | werkt |
| 10 | Documentation (README + architecture-doc) | 2 | helder voor outsider |

**Totaal:** 23 punten. Senior-niveau = 18+. Production-ready = 21+.

## Voorbeeld-oplossingen

We hebben drie voorbeeld-implementaties zodat je kunt vergelijken:

- `starter/` — skeleton met TODO's (begin hier)
- `solution-minimal/` — slaagt rubric net (TODO: implementeer zelf)
- `solution-production/` — alle bells & whistles (TODO)
- `solution-anti-pattern/` — bewust gebrekkig met annotaties (TODO)

## Tijdsinvestering

- Junior: ~1 week
- Mid: ~3 dagen
- Senior: ~1 dag voor minimal, 2-3 voor production

## Architectuur

Zie `ARCHITECTURE.md` voor de complete data-flow + componenten.
