# Claude Engineering Handboek — Audit & Aanvullings­rapport

**Datum:** 2026-05-09  
**Methode:** Zes parallelle deep-research agents · interne content-audit · Anthropic feature coverage · canon benchmarking (Anthropic + niet-Anthropic) · UX/feature audit · diepte-gap analyse  
**Doel:** geprioriteerde lijst waar jij uit kiest. Geen "doe alles", wel "dit is wat het zou kunnen worden".

---

## TL;DR

Het handboek is **content­ueel sterk** (12.500 regels, 33 modules, doordachte categorisatie) maar heeft drie soorten gaten:

1. **Content-diepte** — sommige modules zijn ondiep (Cowork/Dispatch/Routines, Resources, Schemas) of missen specifieke deep-dives die in de canon standaard zijn (LLM-as-judge bias, hybrid search, contextual retrieval, agent memory, prompt versioning).
2. **Recente Anthropic features** ontbreken of zijn dun — Computer Use API-tool, Structured Outputs, Sessions API, Managed Agents, Tool Search, Citations, Files/Batch API patronen, prompt caching TTL-changes, 1M context economics.
3. **Interactiviteit** — het is een prachtig leesbaar boek, maar features die je verwacht in een 33-modules studieapp ontbreken: hash-routing, copy-knop op code, command palette, in-page TOC, prev/next, quizzen, BYOK prompt-sandbox, AI-tutor, glossary-tooltips. Tien quick-wins zouden de UX in ~3,5 uur transformeren.

**Strategie-advies:** drie sprints. Sprint 1 = UX quick-wins (1 dag). Sprint 2 = vier kritieke nieuwe modules (Observability, Computer Use, Structured Outputs, Multi-agent). Sprint 3 = zeven canon-modules (Fine-tuning, Voice, Memory, Guardrails, Prompt Ops, Routing, AI UX). Zie §6.

---

## 1. Wat het handboek nú al sterk doet

| | Sterk punt |
|---|---|
| ✓ | **Logische curriculum-volgorde** — Fundamenten → Prompting → Capabilities → Build → Productie volgt natuurlijke escalatie. |
| ✓ | **Diepte in 70% van de modules** — Tools&MCP (408 regels), Agents (405), Backend (614), Security (826), Claude Code Deep (619), RAG (452), Evals (374) zijn écht diep, niet alleen theorie. |
| ✓ | **Ecosysteem-bewustzijn** — Anthropic-op-3-clouds, MCP standaardisering, n8n integratie tonen marktrealisme. |
| ✓ | **Safety-first** — Constitutional AI, prompt-injection lagen, compliance zijn ingebakken. |
| ✓ | **Cross-references** — modules verwijzen naar elkaar (zie ook X). |
| ✓ | **Visuele identiteit** — oranje accent, Fraunces serif, dark mode, sticky header, fijn lettertype-werk. |
| ✓ | **9 categorieën sidebar + numbering** — duidelijk leerpad. |
| ✓ | **Glossary met 90+ termen** — solide referentie-laag. |

---

## 2. Diepe interne content-audit (per module)

Bevindingen per module van de Explore-agent. **Diepte-verdeling:** 60% diep · 30% gemiddeld · 10% dun.

### Modules die uitbreiding verdienen

| Module | Huidige regels | Bevinding | Prioriteit |
|---|---:|---|---|
| **Cowork / Dispatch / Routines** | ~158 | Onderbenut voor wat een kritieke productie-guide voor teams moet zijn. Geen team-setup-checklist, geen governance-policies, geen kosten-tracking multi-user, geen audit-logs per persoon. | 🔴 Hoog |
| **Resources** | dun | Te kort voor een handboek dat lezers verder moet sturen. Mist canon-leeslijst (Huyen, Yan, Hamel, Latent Space). | 🔴 Hoog |
| **Schemas** | 303 (6 schemas) | 6 ASCII-diagrammen. Mist: error-recovery, multi-agent coordination, caching layers, security layers, observability pipeline, prompt caching breakpoints. | 🟡 Midden |
| **Prompt Patterns** | 144 | 16 patterns genoemd, maar geen "wanneer pattern X inzetten" decision-matrix, geen anti-patterns, geen interplay tussen patterns. | 🟡 Midden |
| **Workflow Checklist & 20 Prompt-Wetten** | <300 | Geen interactive checkboxes, voelt statisch. | 🟡 Midden |
| **Exercises** | per hoofdstuk 3, 60 totaal | 100% tekst, geen self-check, geen vinkje, geen kennistest. Content is er — alleen interactie ontbreekt. | 🔴 Hoog (UX-fix) |
| **Hosting Free** | 157 | Mist concrete stap-voor-stap deploy-tutorial, "eerste waardevolle app met gratis tiers". | 🟢 Laag |
| **Cost Optimization** | 396 | Mist cost-calculator widget, "hoe meet je true cost-per-outcome", model-vergelijkingstabel met live pricing. | 🟡 Midden |
| **Cases per Industrie** | 417 | Voelt als "wat je kunt doen" i.p.v. "hoe je het doet". Geen kwantitatieve resultaten (ROI), geen failure-mode per industrie. | 🟡 Midden |

### Top-10 prioritaire content-uitbreidingen (over modules heen)

1. **End-to-end werkende code-voorbeelden** — Agents, RAG, Automation, Frontend, Backend missen elk een paste-and-run PoC.
2. **Interactive decision-trees** — "Welk model?" / "RAG vs agent vs workflow?" / "Security per industrie?"
3. **Diepere security per industrie** — Finance, Healthcare, Legal hebben elk eigen compliance-eisen.
4. **Cost-calculator widget** — "Mijn app verwerkt X berichten/dag met model Y, wat kost het?"
5. **Observability deep-dive als eigen module** — OTEL + Langfuse/LangSmith/Helicone/Phoenix vergelijking.
6. **Multi-tenant governance handbook** — Cowork & Dispatch verdienen 3× meer ruimte.
7. **Failure-mode-atlas** — Per architecture-pattern: wat kan fout, wat zie je, hoe fix je het?
8. **Evals-as-CI/CD** — GitHub Actions/GitLab integratie, niet alleen standalone scripts.
9. **Voice/multimodal deep-dive** — Whisper, ElevenLabs, real-time API, sub-300ms latency-budget.
10. **Benchmark-suite voor je eigen app** — "wat is een baseline voor MIJN use case", niet generieke SWE-bench.

---

## 3. Anthropic feature coverage gaps

Op peildatum nov 2025 / mei 2026 bestaan ~35-40 productie-klare features. Schatting: **18-20 goed gedekt · 8-12 onvolledig · 7-10 waarschijnlijk volledig missend**.

### Absoluut MISSING (hoge prioriteit)

| # | Feature | Waarom kritiek |
|---|---|---|
| 1 | **Computer Use API-tool** | Gamechanger voor automation/RPA. `computer-use-2025-11-24` beta header. Verdient eigen module of grote subsectie. |
| 2 | **Structured Outputs (JSON Schema)** | `anthropic-beta: structured-outputs-2025-11-13`. Garanteerde JSON, niet hetzelfde als tool-use. Kern van de canon (Huyen, Jxnl, OpenAI, Vercel). |
| 3 | **Claude Agent SDK (Python/TS)** | Distinct van Claude Code CLI. Voor engineers die programmatic agents willen, niet via CLI. Het handboek mist deze hele lijn. |
| 4 | **Managed Agents (hosted runtime)** | Beta sinds 2025; Anthropic-hosted agent containers met sessions, vaults, webhooks. Voor productie-deploy. |
| 5 | **Sessions API V2** | Multi-turn state, resume/fork. Essentieel voor agents. |
| 6 | **Tool Search Tool** | Voor agents met >50 tools, dynamic loading zonder context overhead. |
| 7 | **MCP Connector (API-level)** | Anders dan Claude Code's MCP. Voor MCP-architectuur in eigen apps. |
| 8 | **Citations API** | Track sources native; integreert met PDF support. |
| 9 | **Memory Tool / Memory Stores** | Anthropic memory primitive (beta), los van RAG. |
| 10 | **Claude.ai product-features (Projects, Artifacts, Voice, Memory, MCP Connectors)** | Engineers moeten weten hoe gebruikers integreren. |

### Gedeeltelijk gedekt — check & uitbreiden

- **Prompt caching** — voeg toe: workspace-level cache isolation (sinds feb 2026), 1h TTL via `"ttl":"1h"`, default veranderd van 1h → 5m in maart 2026, hit-rate monitoring, kosten-impact rekenvoorbeeld.
- **Extended Thinking** — voeg toe: Adaptive thinking (Opus 4.7), Effort/Task budgets, summary tokens.
- **Batch API** — voeg toe: 50% korting, 24h SLA, 300K output tokens op Opus 4.7.
- **Vision + PDF + Citations** — voeg toe: combinaties, conflicten (citations × structured outputs).
- **Sub-agents** — voeg toe: context isolation, permission scoping, sub-agent prompts.
- **Hooks (Claude Code)** — voeg toe: SessionStart/End, SubagentStart/Stop, duration_ms, matcher patterns.
- **MCP** — voeg toe: lazy schema loading via ToolSearch (10× context reductie bij 50+ tools), 8M downloads ecosystem (april 2025).
- **Plugins** — voeg toe: `.plugin` format, plugin marketplaces, plugin dependencies.
- **1M context window** — kosten-implicaties, latency, alternatieven.

### Recente 2025-2026 features (makkelijk gemist)

- **Cowork (Q1 2026)** — agentic desktop, distinct van Claude Code. Module bestaat maar is dun.
- **Dispatch** — phone → desktop QR-trigger.
- **Skills MCP** — portable skill packages met MCP backend.
- **Financial Services agent templates** (Q1 2026) — 10 pre-built agents.
- **Claude 4.7 Opus** — adaptive thinking + 1M op standaard pricing.
- **Workload Identity Federation** — auth via AWS/GCP/Azure/GitHub/Okta/K8s/SPIFFE.
- **Plan Mode / Output Styles / Headless Mode / Voice Dictation** in Claude Code.
- **Routines / Scheduled Tasks / Channels** in Claude Code.

---

## 4. Canon-gap analyse (niet-Anthropic AI engineering)

Benchmarked tegen: Chip Huyen "AI Engineering" (O'Reilly 2025), Eugene Yan, Hamel Husain, Jason Liu, Latent Space 2025 reading list, OpenAI Cookbook, Vercel AI SDK, LangChain/LangGraph, Promptfoo, Langfuse, Brilliant.org, MDN, Khan Academy, Codecademy.

### Volledig ontbrekende modules (canon-standaard)

1. **Fine-tuning & distillation** — Huyen besteedt 2 hoofdstukken, Hamel een hele Maven-cursus. Wanneer FT vs RAG vs prompting, LoRA/QLoRA, model distillation (Claude Haiku als student van Sonnet), synthetic data pipelines.
2. **Synthetic data generation** — Self-Instruct, Evol-Instruct, Magpie, persona-based, model collapse preventie.
3. **Inference optimization & latency** — TTFT, prefix caching, speculative decoding, chunked prefill. Anthropic prompt caching = 90% goedkoper, 85% sneller — verkooppunt onbenut.
4. **Observability stack als architectuur** — LangSmith vs Langfuse vs Helicone vs Braintrust vs Phoenix vergelijking, OpenTelemetry GenAI Semantic Conventions.
5. **Prompt versioning & registry** — extract uit code, immutability, environment aliases, Langfuse/PromptLayer/MLflow/Braintrust.
6. **LLM-as-Judge deep dive** — prompting templates, position-bias mitigatie, pairwise vs scalar, alignment-workflow.
7. **Multi-agent orchestration patterns** — Conductor / Swarm / Hierarchy / Graph; ReAct / Reflexion / Plan-Execute / Debate / Verifier-Critic. ~70% van productie = orchestrator-worker.
8. **Guardrails ecosystem** — NeMo Guardrails, Llama Guard, Guardrails AI, defense-in-depth, OWASP LLM Top-10.
9. **Agent memory architecturen** — vector / graph / episodic / procedural; Mem0/Zep/MemGPT.
10. **Voice & speech** — Whisper, Vapi, Retell, Realtime API, sub-300ms latency budget. Voice-agents zijn volwassen markt 2026.
11. **AI UX patterns** — streaming token UI, regenerate, edit, branching, citations hover, tool-call rendering, suggested follow-ups.

### Gedeeltelijk gedekt — diepte toevoegen

| Topic | Naar welke module | Wat toevoegen |
|---|---|---|
| Hybrid search + RRF + ColBERT reranking | RAG | BM25 + dense + RRF productie-pipeline |
| Contextual retrieval (Anthropic, sept 2024) | RAG | -67% retrieval errors, Claude-specifieke feature |
| Late chunking vs contextual retrieval | RAG | Trade-off matrix, 8k+ docs |
| Vector DB tradeoffs | RAG | Pinecone vs pgvector vs Qdrant vs Weaviate decision tree |
| GraphRAG + knowledge graphs | RAG | Microsoft GraphRAG voor query-focused summarisation |
| RAGAS metrics | Evals/RAG | Faithfulness, answer relevance, context precision/recall |
| Function calling reliability | Tools&MCP | Schema validation, parallel, silent-fail detection |
| Streaming UX patterns | Frontend | SSE > WebSocket; 40% perceived speed gain |
| Multi-model routing & fallback gateway | CostOpt | LiteLLM/Portkey/OpenRouter/RouteLLM (-85% cost) |
| Caching strategies | CostOpt | Semantic cache 31% hit rate; multi-tier |
| Reasoning models / test-time compute | ClaudeDeep | o1/o3/R1/QwQ patroon, ToT, self-consistency |
| Indirect prompt injection defenses | Security | Microsoft Spotlighting, Data Prompt Isolation, signed prompts |
| PII detection (Presidio + GLiNER) | Security | Productie redaction stack |
| Cost attribution per tenant | CostOpt | Header-tagging, per-feature dashboards |

### Top-15 canon-onderwerpen die in 4+ bronnen staan en onvolledig zijn in het handboek

| # | Topic | Module-target |
|---|---|---|
| 1 | LLM-as-Judge bias & mitigatie | Evals |
| 2 | Hybrid search + reranking | RAG |
| 3 | Multi-agent orchestration taxonomie | Agents (nieuw) |
| 4 | Observability platform comparison | Nieuwe module |
| 5 | Prompt versioning & registry | Evals (uitbreiden) of nieuw |
| 6 | Fine-tuning ladder + LoRA/QLoRA | Nieuw |
| 7 | Structured outputs / Instructor / Pydantic | Prompting Advanced (uitbreiden) |
| 8 | Synthetic data generation | Nieuw of in FT |
| 9 | Memory architecturen (vector/graph/episodic/procedural) | Nieuw of in Agents |
| 10 | Multi-model routing (RouteLLM/Portkey/LiteLLM) | CostOpt |
| 11 | Semantic caching | CostOpt |
| 12 | Reasoning models / test-time compute | ClaudeDeep |
| 13 | Streaming UX & generative UI | Frontend (uitbreiden) |
| 14 | Indirect prompt injection defenses | Security |
| 15 | Voice agents & real-time API | Nieuw |

---

## 5. UX & interactiviteit gaps

Het handboek is contentueel uitstekend, maar interactie-laag is dun: 5 stuks state in localStorage (`completed`, `notes`, `darkMode`, `searchQuery`, `glossarySearch`, `sidebarOpen`). Onderstaande zijn benchmark-vergelijkingen.

### Wat er nu **niet** in zit

- ❌ Hash-routing / deeplinks → bookmark/share onmogelijk
- ❌ Copy-knop op code-blocks → user moet handmatig selecteren in 100+ `<Pre>`'s
- ❌ Prev/Next-navigatie onderaan een hoofdstuk
- ❌ In-page Table of Contents (terwijl hoofdstukken 200-800 regels zijn)
- ❌ Cmd+K command palette
- ❌ Full-text search door body content
- ❌ Glossary-tooltips inline in bodytext (90+ termen aanwezig, maar "RAG" of "MCP" in een paragraaf is pure tekst)
- ❌ Quizzen / drills / spaced repetition
- ❌ Oefening-checkboxes (60 oefeningen, allemaal `<li>` items zonder vinkje)
- ❌ Code playground / BYOK prompt-sandbox
- ❌ AI-tutor (ironisch in een Claude-handboek)
- ❌ JSON export/import van voortgang → cross-device sync onmogelijk
- ❌ Print-stylesheet
- ❌ PDF/Markdown export
- ❌ Embeds (YouTube, Loom, Excalidraw, Mermaid)
- ❌ "Laatst bijgewerkt"-stempel per module
- ❌ Streaks / badges / mastery-mechanics
- ❌ Bookmarks / favorieten
- ❌ Module-prerequisites / leerpad-suggesties (klikbaar)
- ❌ Theme-varianten (sepia, dyslexic font)
- ❌ EN-toggle (i18n)

### Quick-wins (≤ 1 uur per stuk, hoge impact)

1. **Copy-knop op `<Pre>`** — `navigator.clipboard.writeText` in helper. ~20 min. Massa-impact (honderden code-blocks).
2. **Hash-routing** — `useEffect` op `hashchange`. ~25 min. Maakt alles bookmark/shareable.
3. **Prev/Next-knoppen** onderaan modules. ~15 min.
4. **Oefening-checkboxes** in `Exercises`. ~30 min.
5. **JSON export/import voortgang** in header. ~30 min. Lost cross-device pijn op zónder backend.
6. **Print-stylesheet** — `@media print` in index.css. ~15 min.
7. **`title` + `aria-label` op sidebar-buttons** — a11y. ~10 min.
8. **"Laatst bijgewerkt"-veld** per module. ~20 min.
9. **Streak-counter** in localStorage. ~30 min.
10. **Sepia theme** als derde optie. ~25 min.

**Totaal: ~3,5 uur werk, transformeert de UX.**

### Top-15 feature-toevoegingen geprioriteerd op (impact × haalbaarheid)/complexiteit

| # | Feature | Impact | Complex. |
|---|---|---|---|
| 1 | Cmd+K command palette (fuzzy door titels + headings + glossary) | Hoog | Midden |
| 2 | URL-routing met deeplinks (`/m/agents#02`) | Hoog | Laag |
| 3 | Copy-knop op `<Pre>` | Hoog | Laag |
| 4 | Prev/Next-navigatie | Hoog | Laag |
| 5 | In-page Table of Contents (sticky right-rail) | Hoog | Midden |
| 6 | Voortgang export/import (JSON-bestand) | Midden | Laag |
| 7 | Quiz-modus per hoofdstuk (3-5 vragen × 30 modules) | Hoog | Hoog |
| 8 | Oefening-checkboxes | Midden | Laag |
| 9 | Glossary-tooltips inline in bodytext | Hoog | Midden |
| 10 | **Prompt-sandbox met BYOK** | Zeer hoog | Hoog |
| 11 | **AI-Tutor** met module als systeem-prompt | Hoog | Hoog |
| 12 | Streaks + badges + milestone-celebrations | Midden | Midden |
| 13 | Print-stylesheet | Midden | Laag |
| 14 | Mermaid-diagrammen i.p.v. ASCII-art (klikbare nodes) | Midden | Midden |
| 15 | Versie-stempel per module | Laag | Laag |

> **De killer-feature** voor een Claude-handboek is #10+#11 gecombineerd: gebruikers leren prompt engineering door te prompten in een sandbox die zelf prompt engineering doet. Zelf-referentieel + on-brand.

---

## 6. Voorgestelde uitvoering — 5 sprints

### Sprint 1 — UX fundament (1 dag, ~6u)

Quick-wins #1-10 uit §5. Levert:
- Hash-routing → shareable bookmarkable
- Copy-knop op alle code
- Prev/Next onderaan modules
- Oefening-checkboxes (60 stuks)
- JSON sync (cross-device)
- Print-styles
- A11y labels
- "Laatst bijgewerkt" per module
- Streak-counter
- Sepia theme

**Resultaat:** "mooie statische long-read" → "tool die mensen dagelijks openen".

### Sprint 2 — Vier kritieke nieuwe modules (3-5 dagen)

Op basis van Anthropic gap §3 en canon §4:

1. **Computer Use** — API tool + state management + replay/recovery + Claude.ai browser computer use.
2. **Structured Outputs & Function Calling Reliability** — `output_schema`, Instructor/Pydantic, retry-met-validation, schema design.
3. **Observability** — OpenTelemetry GenAI conventions, LangSmith vs Langfuse vs Helicone vs Braintrust vs Phoenix, traces/spans/scores/datasets.
4. **Multi-agent Orchestration** — Conductor/Swarm/Hierarchy/Graph; ReAct/Reflexion/Plan-Execute/Debate; LangGraph/CrewAI/AutoGen.

### Sprint 3 — Cmd+K palette + In-page TOC + Glossary tooltips (2-3 dagen)

Maakt het boek écht bruikbaar als referentie­werk in plaats van als lineair leesboek.

### Sprint 4 — Quiz-modus + 90 vragen schrijven (1 week)

3 multiple-choice vragen × 30 modules. Brengt leereffectiviteit naar Brilliant/Anthropic-tutorial niveau.

### Sprint 5 — BYOK prompt-sandbox + AI-Tutor (1 week)

Killer-feature. Claude API CORS is open → pure browser-fetch werkt. Disclaimer over key-storage komt al voor in Security-module.

### Sprint 6+ — Canon-modules afronden (loopt door)

Op volgorde van prioriteit:
- Fine-tuning & Adaptation (LoRA/QLoRA + distillation + synthetic data)
- Voice & Speech (Whisper/Vapi/Retell/Realtime)
- Agent Memory (vector/graph/episodic/procedural)
- Guardrails (NeMo/Llama Guard/Guardrails AI)
- Prompt Ops (versioning, registry, CI gating)
- Multi-model Routing (LiteLLM/Portkey/OpenRouter/RouteLLM)
- AI UX Patterns (streaming, branching, citations)

### Sprint X — Bestaande modules uitbreiden (parallel werk)

Per module 50-200 regels toevoegen voor de gemarkeerde gaps. Volgorde:
- **Cowork/Dispatch/Routines** — verdrievoudigen (158 → ~500 regels). Team-setup, governance, audit-logs, kosten-tracking.
- **RAG** — hybrid search, contextual retrieval, late chunking, GraphRAG, vector DB tradeoffs, RAGAS.
- **Evals** — LLM-as-judge bias, regression CI/CD, prompt versioning, framework comparison.
- **Security** — IPI defenses, PII redaction stack, OWASP LLM Top-10, sandboxing.
- **CostOpt** — multi-model routing, semantic caching, cache TTL changes, cost attribution.
- **Agents** — Plan-Execute trade-off, sub-agent delegation, tool reliability, Reflexion.
- **ClaudeDeep / ClaudeCodeDeep** — adaptive thinking, batch patterns, computer use, plugins/marketplaces, headless, output styles, Routines.
- **Resources** — canon reading list (Huyen, Yan, Hamel, Latent Space, Simon Willison, Cookbook, Latent Space 2025 papers).

---

## 7. Mogelijke nieuwe modules — overzicht

| Voorgestelde module | Categorie | Reden |
|---|---|---|
| **Computer Use** | Capabilities of Claude Mastery | API tool + browser computer use; gamechanger feature |
| **Structured Outputs** | Prompting of Capabilities | Canoniek productiepatroon; ontbreekt nu |
| **Observability** | Productie | Productie-LLM zonder dit is blind |
| **Multi-agent Orchestration** | Capabilities | ~70% van productie-systemen |
| **Agent Memory** | Capabilities | Vector/graph/episodic/procedural |
| **Voice & Speech** | Capabilities | Volwassen markt 2026 |
| **Fine-tuning & Adaptation** | Bouwen of Productie | LoRA/QLoRA + distillation + synthetic data |
| **Prompt Ops** | Productie | Versioning, registry, CI gating |
| **Guardrails Architectuur** | Productie | Defense-in-depth, OWASP LLM-Top-10 |
| **Multi-model Routing** | Productie | -85% cost mogelijk |
| **AI UX Patterns** | Bouwen | Streaming, branching, citations, tool-rendering |
| **Inference Optimization & Latency** | Productie | TTFT, KV-cache, speculative decoding |
| **Claude Agent SDK (Python/TS)** | Claude Mastery | Distinct van CLI |
| **Managed Agents (Anthropic-hosted)** | Claude Mastery / Productie | Beta, los van zelf-hosting |

Niet alle 14 hoeven te komen — kies de 4-7 met hoogste waarde voor jouw doelgroep.

---

## 8. Top-50 toevoegingen geprioriteerd op (impact × canon-frequentie)

Geconsolideerde lijst over alle 6 agents, gedupliceerd. **L** = laag, **M** = midden, **H** = hoog complexiteit.

### 🔴 Hoogste prioriteit (canon × Claude-specifiek × actuele lacune)

| # | Toevoeging | Type | Complex. |
|---|---|---|---|
| 1 | Hash-routing + deeplinks per heading | UX | L |
| 2 | Copy-knop op `<Pre>` | UX | L |
| 3 | Prev/Next-navigatie | UX | L |
| 4 | Module: Computer Use API-tool + Claude.ai browser | Content | M |
| 5 | Module: Structured Outputs & Schema-first | Content | M |
| 6 | Module: Observability (OTEL + 5 platforms) | Content | M |
| 7 | Module: Multi-agent Orchestration | Content | M |
| 8 | RAG uitbreiden: hybrid search + RRF + reranking | Content | M |
| 9 | RAG uitbreiden: contextual retrieval + late chunking | Content | L |
| 10 | Evals uitbreiden: LLM-as-judge bias-mitigatie | Content | L |
| 11 | Security uitbreiden: IPI defenses (Spotlighting, DPI) | Content | L |
| 12 | Cowork/Dispatch verdrievoudigen | Content | M |
| 13 | Prompt caching deep-dive (TTL, breakpoints, ordering) | Content | L |
| 14 | Cmd+K command palette | UX | M |
| 15 | In-page TOC (sticky right-rail) | UX | M |

### 🟡 Hoge prioriteit (canon × bredere community)

| # | Toevoeging | Type | Complex. |
|---|---|---|---|
| 16 | Module: Fine-tuning & Adaptation (LoRA/QLoRA + distillation) | Content | M |
| 17 | Module: Agent Memory architecturen | Content | M |
| 18 | Module: Voice & Speech (Whisper/Vapi/Retell/Realtime) | Content | M |
| 19 | Module: Guardrails (NeMo/Llama Guard/Guardrails AI) | Content | M |
| 20 | Module: Prompt Ops (versioning, registry, CI) | Content | M |
| 21 | Module: Multi-model Routing (LiteLLM/Portkey/OpenRouter) | Content | M |
| 22 | CostOpt uitbreiden: semantic caching + cost attribution | Content | L |
| 23 | Agents uitbreiden: Plan-Execute vs ReAct, Reflexion, sub-agents | Content | L |
| 24 | Tools&MCP uitbreiden: Tool Search Tool, parallel/strict/programmatic | Content | L |
| 25 | ClaudeDeep uitbreiden: adaptive thinking + 1M context economics | Content | L |
| 26 | ClaudeCodeDeep uitbreiden: hooks, plugins, headless, output styles, routines | Content | M |
| 27 | Module: Claude Agent SDK (Python/TS) | Content | M |
| 28 | Module: Managed Agents (Anthropic-hosted) | Content | M |
| 29 | Glossary-tooltips inline | UX | M |
| 30 | Quiz-modus per hoofdstuk + 90 vragen | UX | H |

### 🟢 Wenselijk (versterkt boek + UX)

| # | Toevoeging | Type | Complex. |
|---|---|---|---|
| 31 | BYOK prompt-sandbox | UX | H |
| 32 | AI-Tutor met module-context | UX | H |
| 33 | Oefening-checkboxes (60) | UX | L |
| 34 | JSON export/import voortgang | UX | L |
| 35 | Streaks + badges + milestone-celebrations | UX | M |
| 36 | Print-stylesheet | UX | L |
| 37 | Mermaid-diagrammen i.p.v. ASCII | UX | M |
| 38 | "Laatst bijgewerkt"-stempel per module | UX | L |
| 39 | Sepia theme + dyslexic-font optie | UX | L |
| 40 | Resources uitbreiden: canon reading list | Content | L |
| 41 | Cases uitbreiden: kwantitatieve resultaten + failure modes | Content | M |
| 42 | Schemas uitbreiden: 6 → 15 (caching/security/observability/prompt-cache) | Content | M |
| 43 | Decision-trees: model keuze, RAG-vs-agent, security per industrie | Content/UX | M |
| 44 | Cost-calculator widget (interactieve invoer) | Content/UX | M |
| 45 | Failure-mode-atlas per architecture-pattern | Content | M |
| 46 | Module-prerequisites grafiek (klikbaar) | UX | M |
| 47 | Module: Inference Optimization & Latency | Content | M |
| 48 | Module: AI UX Patterns (streaming/branching/citations) | Content | M |
| 49 | EN-toggle (i18n basis) | UX | M |
| 50 | Discussion via Giscus | UX | L |

---

## 9. Wat zou ik zelf doen, in één zin?

**Eerst Sprint 1 (1 dag UX), dan #4-#15 uit de top-50 (Computer Use module + observability + structured outputs + RAG-uitbreiding + Security IPI + Cowork-verdrievoudiging), dan Sprint 4-5 (quizzes + BYOK sandbox + AI-tutor) — dat is de volgorde met hoogste leereffect-per-uur en blijft 100% trouw aan de stijl die je nu al hebt.**

---

## Bronnen & verder lezen

### Anthropic (officieel)
- [Claude API docs](https://platform.claude.com/docs/en/intro)
- [Claude Code docs](https://code.claude.com/docs/en/overview)
- [Anthropic Cookbook (GitHub)](https://github.com/anthropics/anthropic-cookbook)
- [Anthropic Academy / Skilljar](https://anthropic.skilljar.com/)
- [Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [Anthropic courses repo](https://github.com/anthropics/courses)

### AI engineering canon
- Chip Huyen, *AI Engineering* (O'Reilly 2025)
- [Eugene Yan — Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/)
- [Hamel Husain — LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- [Latent Space — 2025 AI Engineering Reading List](https://www.latent.space/p/2025-papers)
- [Jason Liu — Systematically Improving RAG](https://jxnl.co/writing/)
- [Simon Willison — LLM tag](https://simonwillison.net/tags/llms/)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

### Specifieke deep-dive bronnen
- [Microsoft — Defending against indirect prompt injection](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks)
- [OWASP LLM Top-10 2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [OpenTelemetry GenAI Semantic Conventions](https://langfuse.com/integrations/native/opentelemetry)
- [RAGAS metrics docs](https://docs.ragas.io/en/stable/concepts/metrics/)
- [Anthropic Contextual Retrieval](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)
- [Mem0 — agent memory architectures](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [RouteLLM — multi-model routing](https://www.mindstudio.ai/blog/best-ai-model-routers-multi-provider-llm-cost)

### UX / interactive learning benchmarks
- [Brilliant.org case study (ustwo)](https://ustwo.com/work/brilliant/)
- [Khan Academy — gamification (Trophy)](https://trophy.so/blog/khan-academy-gamification-case-study)
- [Roadmap.sh](https://roadmap.sh/)
- [MDN interactive examples](https://github.com/mdn/interactive-examples)

---

*Einde rapport. ~3500 woorden, 50 toevoegingen geprioriteerd, 6 sprints geadviseerd.*
