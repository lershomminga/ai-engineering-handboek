# Architecture — Customer Support Agent

## Data-flow

```
┌─────────────┐
│  Email /    │  webhook (Zendesk / Gmail / FastAPI direct)
│  Inkomende  │
│  ticket     │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│  GUARDRAILS LAAG                                         │
│   1. Llama Guard (jailbreak detect)                      │
│   2. Presidio (PII-redact: NAW, IBAN, email)             │
└──────┬───────────────────────────────────────────────────┘
       │  (redacted ticket)
       ▼
┌──────────────────────────────────────────────────────────┐
│  CLASSIFY (Haiku, structured output)                     │
│   { category, urgency, sentiment, refund_request? }      │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────┴────────────┐
│ Route op category         │
├───────────────────────────┤
│ billing/shipping/product  │──┐
│   → RAG-pipeline          │  │
├───────────────────────────┤  │
│ complaint                 │──┼──→ Auto-reply draft + escalate
├───────────────────────────┤  │
│ spam                      │──┴──→ Discard + log
└──────────┬────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│  RAG (Voyage embeddings + pgvector + Cohere rerank)      │
│   - Contextual chunks van FAQ-docs                        │
│   - Hybrid search (BM25 + dense + RRF)                    │
│   - Top-5 chunks → context voor generation                │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│  GENERATE (Sonnet 4.6 + citations)                       │
│   - Draft antwoord met [citation:N] markers              │
│   - Faithfulness-check via RAGAS                         │
│   - Bij score < 0.85: escalate naar human                │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│  ACTION GATE                                             │
│   - Auto-reply als urgency=low + faithfulness>0.85       │
│   - Anders → Slack #support-queue voor human review      │
└──────┬───────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│  OBSERVABILITY                                           │
│   - Langfuse trace: alle spans (classify→RAG→gen→action) │
│   - Postgres: cost_per_ticket insert                     │
│   - Slack alerts bij refusal-rate spike of cost-anomaly  │
└──────────────────────────────────────────────────────────┘
```

## Componenten

| Component | Tech | Reden |
|---|---|---|
| Webhook ingress | FastAPI + Inngest | Durable retry, audit-trail |
| Guardrails | Presidio + Llama Guard 3 1B | NL PII coverage + snel |
| LLM-calls | Anthropic Python SDK | Native streaming + cost-tracking |
| RAG | Voyage-3 + pgvector + Cohere Rerank v3 | Beste NL-quality |
| Storage | Postgres + Redis (cache) | Battle-tested + cheap |
| Observability | Langfuse self-host | OTEL-native + GDPR (NL data) |
| Frontend | Next.js 15 + AI SDK 5 | Streaming + tool-cards |
| Queue | Inngest | Durable workflows + retries |
| Deploy | Render of Fly.io | Simpel + EU-regions |

## Kost-targets

- Cost per resolved ticket: ≤ €0,03
- Cost per escalated ticket: ≤ €0,08 (RAG + Opus voor de moeilijke)
- p95 ticket-to-response: ≤ 15 seconden (zonder human review)

## Failure-modes om te testen

1. PII in inkomende ticket (BSN, IBAN) → moet redacted in logs
2. Prompt-injection in ticket-body → Spotlighting + Llama Guard moet vangen
3. Hallucinated FAQ-antwoord → RAGAS-faithfulness < 0.85 → escalate
4. Anthropic 529 overload → fallback chain naar Bedrock
5. RAG-DB onbereikbaar → graceful degradation naar generic answer + escalate
6. Cost-spike (10× normaal) → cron-alert + admin notify

## Eval-set structuur

`evals/cases.jsonl` met 30 testtickets verdeeld:
- 12× FAQ-ready (verwacht: auto-reply met juiste citation)
- 8× escalate (verwacht: draft + Slack notify)
- 5× spam (verwacht: discard)
- 3× PII-heavy (verwacht: redacted in alle downstream)
- 2× prompt-injection (verwacht: blocked + audit-log)

CI-gate: ≥ 85% pass-rate, geen criticals failures.
