# Master Expansion Plan — Claude Engineering Handboek

**Datum:** 2026-05-10 · **Versie:** 1.0
**Methode:** 8 parallelle deep-research agents · line-by-line audit van alle 45 modules · 100+ web-searches · benchmark tegen 2026-canon
**Output:** geprioriteerde lijst van **150+ concrete uitbreidingen**, gegroepeerd per cluster + masterprioriteit

---

## TL;DR

Het handboek is in mei 2026 ~15.246 regels over 45 modules. De deep-audit identificeert **drie soorten gaps**:

1. **Verouderde claims & API-versies** — bv. structured outputs gebruikt nog beta-header `2025-11-13` terwijl het GA is, Anthropic Memory Tool toont oude beta-naam, MCP-cijfers zijn outdated (770 → echte 9.652-22.775).
2. **Dun-vs-belofte modules** — AIUX (91 regels), HostingFree (158), PromptOps (93), FineTuning (88), Voice (71), Memory (105), Guardrails (104), Observability (105), Multi-agent (88), ComputerUse (113), AgentSDK (109) — elf modules onder de 200 regels die elk een productie-pijler representeren.
3. **Hands-on infrastructure ontbreekt** — geen companion-repo, geen runnable Python end-to-end voorbeelden voor 60% van de modules, geen capstone met scaffold, geen CI-gating-templates.

**Top-50 master-uitbreidingen** zijn hieronder. Geschat totaal-effort: **300-450 uur** (vs. 600-800u in de eerdere roadmap omdat we hier scherper prioriteren).

---

## Cluster-overzicht (huidige diepte per module)

| Module | Regels | H2's | Code-blokken | Diepte |
|---|---:|---:|---:|---|
| **Fundamenten** |  |  |  |  |
| fundamentals | 384 | 18 | 6 | Diep |
| claude-models | 434 | 17 | 7 | Diep |
| tokens-context | 359 | 16 | 11 | Zeer diep |
| api-keys | 222 | 9 | 9 | Gemiddeld |
| **Prompting** |  |  |  |  |
| prompting-basics | 223 | 7 | 3 | Gemiddeld |
| prompting-advanced | 546 | 22 | 12 | Zeer diep |
| prompt-patterns | 144 | 2 | 0 | Dun |
| structured-outputs | 130 | 7 | 3 | Dun |
| evals | 374 | 14 | 10 | Diep |
| **Agent stack** |  |  |  |  |
| skills | 424 | 17 | 8 | Diep |
| tools-mcp | 407 | 16 | 7 | Diep |
| computer-use | 113 | 6 | 2 | Zeer dun |
| agents | 404 | 14 | 9 | Diep |
| multi-agent | 88 | 5 | 2 | Zeer dun |
| agent-sdk | 109 | 7 | 6 | Dun |
| **Retrieval & Voice** |  |  |  |  |
| rag | 613 | 22 (incl. dupes) | 14 | Zeer diep maar dupes |
| memory | 105 | 8 | 4 | Dun |
| voice | 71 | 9 | 3 | Zeer dun |
| **Claude Mastery** |  |  |  |  |
| claude-deep | 155 | 7 | 2 | Dun |
| claude-code-deep | 619 | 12 + 9 H3 | 18 | Zeer diep |
| claude-cloud | 363 | 13 + 3 H3 | 9 | Diep |
| **Bouwen** |  |  |  |  |
| workflows | 523 | 14 | 11 | Sterk |
| automation | 519 | 14 | 9 | Sterk |
| second-brain | 563 | 17 | 11 | Zeer sterk |
| frontend | 468 | 17 | 8 | Sterk |
| ai-ux | 91 | 10 | 3 | **Schokkend dun** |
| backend | 615 | 19 | 14 | Zeer sterk |
| deployment | 476 | 22 | 6 | Sterk maar weinig code |
| hosting-free | 158 | 7 | 3 | Dun |
| **Productie** |  |  |  |  |
| security | 429 | 12 | 9 | Diep |
| guardrails | 104 | 7 | 3 | Dun |
| observability | 105 | 9 | 4 | Dun |
| prompt-ops | 93 | 8 | 4 | Dun |
| cost-opt | 500 | 16 | 12 | Diep |
| fine-tuning | 88 | 7 | 2 | Dun |
| **Praktijk & Referentie** |  |  |  |  |
| welcome | 116 | 0 (h2-helper) | 0 | Gemiddeld |
| roadmap | 489 | 18 | 0 | Diep |
| ecosystem | 401 | 16 | 0 | Diep |
| cases | 416 | 9 | 1 | Diep |
| workflow-checklist | 526 | 6 | 0 | Diep |
| exercises | 251 | 0 (H1 + tasks) | 0 | Gemiddeld |
| schemas | 164 | 6 | 6 | Gemiddeld |
| glossary | 136 | 1 | 0 | Gemiddeld (93 termen) |
| resources | 185 | 1 | 0 | Gemiddeld |

**Patroon:** de "Bouwen"- en "Productie"-categorieën hebben de scherpste asymmetrie — sommige modules zijn 500+ regels productie-grade, andere onder de 100. Eerste werk: gelijktrekken.

---

## Top-50 master-uitbreidingen (over alle modules)

Gerangschikt op **(impact × concreetheid × bridges-a-real-gap)**. Prio H = doe deze in fase 1, M = fase 2, L = fase 3.

### 🔴 Top-15 (fase 1, geschat 100-130 uur)

| # | Module | Uitbreiding | Effort |
|---|---|---|---|
| 1 | **structured-outputs** | Update Pattern 2 naar GA-API (`output_config.format`). Huidige code toont verouderde beta-header die binnenkort niet meer werkt | XS (~2u) |
| 2 | **memory** | Update Anthropic Memory Tool (header `context-management-2025-06-27`, type `memory_20250818`) + volledige `BetaAbstractMemoryTool`-subclass voorbeeld | S (~4u) |
| 3 | **ai-ux** | Volledige expansie 2-3× (alle 10 sub-secties uitbreiden met code + screenshots) | L (~24u) |
| 4 | **computer-use** | End-to-end Python harness met error-recovery (80-100 regels) + Anthropic Docker reference + hardening | L (~16u) |
| 5 | **rag** | Merge duplicaten (Contextual Retrieval, GraphRAG, hybrid, RAGAS staan elk 2×) + introduceer H3-niveau, verwijdert ~120 regels noise | M (~6u) |
| 6 | **claude-code-deep** | Complete Hooks Reference (~27 events tabel + env-vars + matcher-syntax) | M (~8u) |
| 7 | **claude-code-deep** | Plugin format + marketplace H2 (`.claude-plugin/plugin.json`, `marketplace.json`, reserved names) | M (~6u) |
| 8 | **glossary** | Uitbreiden naar 200+ termen + niveau-tag + categorie-tag + filter | M (~10u) |
| 9 | **observability** | Volledige OTEL GenAI span-attributes reference (30+ attrs tabel) + Langfuse self-host docker-compose v3 | M (~8u) |
| 10 | **agent-sdk** | Fix incorrecte imports + complete API-reference klasse-tabel + TypeScript-naast-Python voorbeelden | L (~16u) |
| 11 | **schemas** | Mermaid-migratie van 6 bestaande + 12 nieuwe schemas (prompt-cache, MCP, memory hierarchy, multi-agent, RAG 2026, eval CI/CD, cost flow, security, observability, error-recovery, context-compaction, voice realtime) | L (~20u) |
| 12 | **welcome** | Competentie-matrix met klikbare deep-links + persona-decision-tree + leerduur per categorie | S (~6u) |
| 13 | **multi-agent** | LangGraph state-machine voorbeeld met checkpointing + Framework feature-matrix met benchmarks (CrewAI 31k stars, AutoGen 42k, LangGraph 12.8k) | M (~10u) |
| 14 | **api-keys** | Admin API programmatic key management + Exponential backoff in productie (429 vs 529, equal jitter) + 2026 rate-limits | M (~6u) |
| 15 | **claude-deep** | Pricing-matrix per product (Free/Pro/Max/Team/Enterprise + API + Managed Agents + Routines) + Decision tree "welke laag pak ik?" | S (~6u) |

**Subtotaal fase 1: ~148u (≈ 4 weken full-time of 6-8 weken parttime)**

### 🟡 Top-15 (fase 2, geschat 90-120 uur)

| # | Module | Uitbreiding | Effort |
|---|---|---|---|
| 16 | **agents** | Werkende ReAct-agent code (30 regels, 3 tools) + Reflexion-loop implementatie + Agent debugging toolkit (logs/traces/replay) | M (~10u) |
| 17 | **rag** | Embedding-selectie-matrix als tabel (voyage-3-large, Cohere v4, OpenAI v3, BGE-M3, Jina v3) + Query transformation H2 (HyDE, multi-query, decomposition) | M (~8u) |
| 18 | **security** | Penetration-testing playbook (Garak + Promptfoo Red Team + PyRIT) + Incident-response playbook | M (~10u) |
| 19 | **guardrails** | NeMo Guardrails Colang 2.0 concreet policy-voorbeeld + Llama Guard 3 8B+1B + Prompt Guard 2 deployment (Python + role-split) | M (~10u) |
| 20 | **prompting-advanced** | CoT vs Adaptive Thinking cost/quality matrix + Self-correction loops met code + Few-shot benchmark mini-sectie | S (~8u) |
| 21 | **structured-outputs** | Streaming partial JSON H2 + oneOf/anyOf workarounds + Refusal-as-field deep-dive | M (~8u) |
| 22 | **prompt-patterns** | Decision-matrix wanneer-welk + per-pattern anti-example + Pattern-combinaties (4 archetypische stacks) | S (~6u) |
| 23 | **evals** | CI/CD met GitHub Actions YAML + Bias-mitigation code-patterns + Bootstrap-CI + McNemar Python-code | M (~8u) |
| 24 | **tools-mcp** | Tool Search Tool deep dive met evals-cijfers + SSE-deprecation + Streamable HTTP migratie + OWASP MCP Top 10 framework + CVE-2025-6514 case | M (~10u) |
| 25 | **frontend** | Volledig Next.js 15 + AI SDK 5 end-to-end voorbeeld (~80 regels) + Testing-strategie voor AI chat-apps + CopilotKit vs assistant-ui matrix | M (~10u) |
| 26 | **backend** | FastAPI streaming+auth+rate-limit complete example (~80 regels) + Multi-tenant key-vault pattern + Temporal + Batch API integratie | M (~10u) |
| 27 | **cost-opt** | Cost-calculator interactive widget + RouteLLM concrete setup + ICLR-2025 benchmarks + Stacking-strategies cumulatieve cijfers | M (~10u) |
| 28 | **fine-tuning** | Volledige QLoRA Unsloth tutorial (Llama 3.1 8B) + Distillation pipeline end-to-end + Synthetic-data comparison + Model collapse golden-ratio | L (~14u) |
| 29 | **claude-cloud** | Routine cookbook 8 → 15 recepten + Managed Agents introductie + Audit-log/Compliance API patterns | M (~10u) |
| 30 | **roadmap** | Claude Certified Architect-sectie + Quick-start paden (Weekend / 10u / 1 maand) + Interview-prep concrete resources + Portfolio uitbreiden naar 10 projecten | M (~10u) |

**Subtotaal fase 2: ~142u**

### 🟢 Top-20 (fase 3, geschat 80-110 uur)

| # | Module | Uitbreiding | Effort |
|---|---|---|---|
| 31 | **memory** | Concrete code per Tulving-type (working/episodic/semantic/procedural) + Zep / Graphiti H2 + Conflict-resolution code-patronen + GDPR forget-flow | M (~10u) |
| 32 | **voice** | Volledig Python Vapi codevoorbeeld (40+ regels) + OpenAI Realtime API code + actuele prijzen + NL/GDPR compliance diepte | M (~10u) |
| 33 | **rag** | LazyGraphRAG (jun 2025) + RAG production-ops H2 (incremental indexing, freshness TTL, multi-tenancy) + RAG CI-pipeline | M (~8u) |
| 34 | **workflow-checklist** | Interactive checkboxes voor 72 items + decision-tree "welke wet wanneer" + anti-pattern lijst + printable quick-reference card | S (~6u) |
| 35 | **cases** | "Bouw dit vandaag" tutorial per industrie + Compliance-checklist per sector + Failure modes per industrie + Architecture diagrams (Mermaid) | L (~14u) |
| 36 | **exercises** | 5 oefeningen per recent toegevoegde module (Structured Outputs / Computer Use / Multi-agent / Voice / Memory) + Difficulty-rating in uren + Solutions-repo-pointer + Capstone uitbreiden naar 5 varianten | M (~10u) |
| 37 | **resources** | Anthropic Certificeringen-sectie + DeepLearning.AI 2026 updates + NL-specifieke bronnen-sectie + Anthropic events-kalender | S (~6u) |
| 38 | **ecosystem** | MCP-cijfers update naar mei 2026 + Per-laag stack-diagram + Vendor-lock-in-matrix + Emerging tools to watch | S (~6u) |
| 39 | **prompt-ops** | Langfuse Prompt API end-to-end + Braintrust workflow + A/B-test pattern (sticky-key, Bayesian-stop) + Rollback strategy | M (~8u) |
| 40 | **observability** | Trace-link parent/child voor multi-step + Production sampling implementation + Cost-attribution code + Drift-detection metrics | M (~8u) |
| 41 | **skills** | "Schrijf je eerste skill in 15 minuten" walkthrough + Bad-skill gallery + evals.json schema + grader-prompt + Skill versioning | M (~8u) |
| 42 | **claude-code-deep** | Headless mode + CI patterns + Subagent YAML alle 15 frontmatter-velden + IDE feature-parity matrix + Output styles | M (~10u) |
| 43 | **deployment** | Per-platform deploy guides (6 platforms) + Bedrock vs Vertex vs Foundry matrix + Canary rollout + Model-upgrade migration runbook | M (~10u) |
| 44 | **automation** | Complete n8n workflow JSON dumps voor 3 templates + State-machine patroon + Test-strategieën zonder productie-data + Zapier → n8n migratie | M (~8u) |
| 45 | **second-brain** | Volledige n8n workflow JSON downloads + E2EE pattern bij multi-device sync + Voice-pipeline OpenAI Realtime Whisper | M (~8u) |
| 46 | **hosting-free** | Stap-voor-stap echte AI-app deploy op free tiers + Limits matrix + Gratis-tot-betaald thresholds + Self-host op homelab | M (~8u) |
| 47 | **fundamentals** | Sampling onder de motorkap (temperature/top-p/top-k/min-p) + Hallucinaties intrinsiek vs extrinsiek + Knowledge cutoff per model | S (~6u) |
| 48 | **tokens-context** | Automatic caching toggle (feb 2026) + Cache breakpoint 20-block lookback limit gotcha | XS (~3u) |
| 49 | **claude-models** | Claude via Bedrock vs Vertex vs direct API + Model routing in code + Adaptive thinking effort-levels deep-dive | M (~8u) |
| 50 | **prompting-basics** | Prompt-evolutie galerij v0→v4 + Anti-patterns met fix-zij-aan-zij + Per-domein prompt-templates | S (~6u) |

**Subtotaal fase 3: ~153u**

**TOTAAL Top-50: ~443 uur** verdeeld over 3 fases.

---

## Tien diepste gaps — geconsolideerd

Over alle 8 clusterrapporten heen herhalen deze gaps zich:

1. **Verouderde API-versies in code-voorbeelden** (Structured Outputs, Memory Tool, MCP-cijfers, Helicone maintenance-mode, prompt cache TTL).
2. **Ontbrekende end-to-end runnable code** — meeste modules tonen snippets, geen volledige werkende voorbeelden.
3. **Schokkend dunne UI-laag** — AIUX is 91 regels voor wat het zichtbare deel van AI-apps is.
4. **Geen companion-repo** — alle modules met code zouden naar één GitHub-repo moeten linken voor paste-and-run.
5. **Duplicatie binnen modules** — vooral RAG (Contextual Retrieval, GraphRAG, hybrid search staan elk 2×).
6. **Geen capstone-scaffold** — Exercises noemen "bouw dit", geen rubric, geen voorbeeld, geen review.
7. **Compliance dun voor regulated industries** — Healthcare/Finance/Legal-cases zonder NEN 7510, PCI-DSS, MDR, EU AI Act details.
8. **Geen production case studies met cijfers** — handboek noemt patterns, niet "bij klant X gingen we van Y naar Z".
9. **Auteur-identiteit ontbreekt** — nergens een "Over de auteur" met production-scars.
10. **Cross-references zijn één-richting** — Glossary, Resources, Schemas verwijzen niet terug naar de hoofdmodule.

---

## Aanbevolen uitvoeringsvolgorde

### Sprint A — Bug-fixes & verouderde claims (1 week, ~30u)

- **#1** structured-outputs GA-API update
- **#2** memory Anthropic Memory Tool update
- **#5** rag duplicaten merge
- **#48** tokens-context automatic caching toggle
- **#14** api-keys rate-limits 2026 + admin API
- **#9** observability OTEL reference + Langfuse v3
- **#38** ecosystem MCP-cijfers + Helicone maintenance-mode

Output: <ins>geen verouderde info meer</ins>. Onmiddellijke quality-lift zonder grote uitbreiding.

### Sprint B — Dun-modules optillen (3-4 weken, ~80-100u)

Doel: alle modules >= 200 regels brengen.

- **#3** ai-ux (91 → 250)
- **#4** computer-use (113 → 250)
- **#10** agent-sdk (109 → 230)
- **#13** multi-agent (88 → 220)
- **#19** guardrails (104 → 220)
- **#28** fine-tuning (88 → 220)
- **#31** memory (105 → 230)
- **#32** voice (71 → 230)
- **#39** prompt-ops (93 → 220)
- **#46** hosting-free (158 → 230)

Output: <ins>geen "schokkend dunne" modules meer</ins>. Productie-pijlers krijgen elk hun fair share.

### Sprint C — Companion-repo opzetten (2-3 weken, ~80-100u)

Niet in de Top-50 maar essentieel:

- Eén GitHub-repo `claude-handbook-code` met folder per priority-module
- Werkende code voor: Fundamentals, Prompting Advanced, Tools&MCP, Agents, RAG, Evals, Backend, Computer Use, Multi-agent, Voice, Memory
- Nightly CI tegen Anthropic API
- "Open in repo →" knop in elk Pre-blok

Output: <ins>lezers kunnen alles wat in het boek staat runnen binnen 5 minuten</ins>.

### Sprint D — Schemas & glossary (2 weken, ~30u)

- **#11** schemas Mermaid + 12 nieuwe
- **#8** glossary 93 → 200+
- **#12** welcome competentie-matrix + persona-tree

Output: <ins>navigatie en referentie-laag op niveau van Frontend Masters / O'Reilly</ins>.

### Sprint E — Schrijf-intensieve content-uitbreidingen (4-6 weken, ~100-120u)

Resterende top-50 items in volgorde van afhankelijkheid:

- Prompting cluster (#20, #21, #22, #50, #23, #27)
- Agents cluster (#16, #24, #41, #42)
- Bouwen cluster (#25, #26, #35, #36, #44, #45)
- Productie cluster (#18, #40, #43, #29, #30)
- Praktijk cluster (#34, #37)

Output: <ins>volwaardig premium-handboek</ins> dat de €199-prijs verdedigt.

---

## Verwachte impact op product-positie

| Sprint | Cumulatieve uren | Nieuwe prijs-ceiling | Reden |
|---|---:|:---:|---|
| A (bug-fixes) | 30 | €79 | Niet verouderd voelen |
| B (dun-optillen) | 130 | €99 | Geen "schokkend thin" modules |
| C (companion-repo) | 230 | €129 | Runnable code = "ik doe", niet "ik lees" |
| D (schemas + glossary) | 260 | €139 | Referentiewerk-status |
| E (volledige content) | 380 | €169 | Echt premium-niveau |
| Plus: video, community, capstone-review (eerdere roadmap) | 600+ | €299+ | Cohort + live element |

---

## Wat ik aanraad

**Doe Sprint A meteen** — 30 uur werk, geen content-debat, alles "moet" gefixt worden. Levert direct kwaliteits-lift.

**Doe daarna Sprint B + C parallel** — als jij content schrijft, kan iemand anders (of een toekomstige jou-met-tijd) de repo bouwen. Twee weken werk, fundamenteel anders product.

**Sprint D + E** kan in 6-12 maanden, naast launch. Zelfs zonder D+E is het product al verkoopbaar op €119 na Sprint C.

**Wat ik NIET zou doen:** alle 50 items in één keer aanpakken. Het is verleidelijk maar fragmenteert je aandacht. Sprint A is in de tijd dat je het rapport leest al uitvoerbaar.

---

## Bronnen — geverifieerde URLs uit het deep-research

Per cluster verzameld (volledige lijst in de individuele cluster-rapporten, hier de hoofd-categorieën):

**Anthropic officieel:**
- platform.claude.com/docs (Memory, Hooks, Skills, Sessions, Plugins, Compliance API, Workload Identity, Routines, Subagents)
- code.claude.com/docs (Headless, Keybindings, IDE-integratie)
- claude.com/blog (Routines launch, Skill-creator improvements)
- claudecertifications.com (Claude Certified Architect)

**Canon-bronnen:**
- Chip Huyen — AI Engineering (O'Reilly 2025)
- Eugene Yan — eugeneyan.com/writing/llm-patterns
- Hamel Husain — hamel.dev (LLM Evals FAQ, Field Guide)
- Latent Space — 2025 + 2026 AI Engineering Reading Lists
- Jason Liu — jxnl.co (Instructor, Systematically Improving RAG)
- Simon Willison — simonwillison.net/tags/llms
- Anthropic — Building Effective Agents essay

**Frameworks & papers:**
- LangGraph, CrewAI, AutoGen (multi-agent)
- Reflexion (Shinn et al., NeurIPS 2023, arXiv:2303.11366)
- RouteLLM (UC Berkeley, ICLR 2025, arXiv:2406.18665)
- ASTRIDE threat-modeling (arXiv:2512.04785)
- OWASP LLM Top-10 2025 + Agentic Top-10 (dec 2025)
- Magpie alignment data (ICLR 2025, arXiv:2406.08464)
- Late chunking (Jina, arXiv:2409.04701)
- Anthropic Contextual Retrieval (sept 2024)
- LazyGraphRAG (Microsoft Research, jun 2025)
- Golden Ratio Weighting (arXiv:2502.18049)

**Tools / vendor docs (geverifieerd):**
- Observability: Langfuse, LangSmith, Helicone (maintenance-mode mrt 2026!), Phoenix, Braintrust
- Frameworks: LangGraph, CrewAI, AutoGen, Mem0, Zep/Graphiti
- Voice: Vapi, Retell, Cartesia Sonic 3, ElevenLabs, Deepgram, OpenAI Realtime API GA
- RAG: pgvector, Pinecone, Qdrant, Weaviate, Vespa, voyage-3-large, Cohere v4, BGE-M3
- Cost: LiteLLM, Portkey, OpenRouter, RouteLLM
- Security: Garak, Promptfoo Red Team, PyRIT, NeMo Guardrails, Llama Guard 3, Guardrails AI, Presidio + GLiNER
- Fine-tuning: Unsloth, Together.ai, Fireworks, Modal, mergekit

---

## Index — waar elk uitbreidingsvoorstel vandaan komt

Per agent-rapport is opgeslagen — om de detail-context terug te halen:

- Cluster 1 (Fundamenten): agent `acad6a8aed96c1a94`
- Cluster 2 (Prompting): agent `ad620a9457c7b2cb5`
- Cluster 3 (Agent stack): agent `a2a493021186ced2d`
- Cluster 4 (Retrieval & Voice): agent `aa8ca396b05a18e02`
- Cluster 5 (Claude Mastery): agent `a0fb097fb41011d18`
- Cluster 6 (Bouwen): agent `af6a5bd1e16877293`
- Cluster 7 (Productie): agent `a15f52cd130c7b738`
- Cluster 8 (Praktijk & Referentie): agent `a8fbed748376d14f9`

Elk rapport bevat tweemaal de diepte van wat hier samengevat is. Stuur me terug naar één van die agent-ID's en ik kan per module zelfs dieper.

---

*Einde Master Expansion Plan v1.0 · ~3.500 woorden · gebaseerd op 8 parallelle deep-research agents · 100+ geverifieerde bronnen.*
