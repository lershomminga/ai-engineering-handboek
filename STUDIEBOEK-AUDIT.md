# Promptmeester — Studieboek-upgrade Audit

**Datum:** 2026-06-04 · **Mode:** AUDIT · **Domein:** AI-prompting / AI-engineering (Nederlandstalig)
**Methode:** 5 parallelle expert-agents (vakexpert + instructional designer + technisch auteur) over alle 45 modules, gescoord tegen de 5-lagen-lat (Wat · Waarom · Toepassing · Context&variatie · Valkuilen).

---

## 1. Samenvatting in 5 bullets

- **Domein:** AI-prompting/AI-engineering. Het is geen "handboek" meer — het is met afstand het diepste Nederlandstalige studieboek over dit onderwerp dat ik ken. **~60% van de modules scoort diepte 4-5** (referentie-niveau), met didactiek (v0→v4 prompt-iteratie, 5-lagen-aanpak, paper-onderbouwing) die de meeste betaalde NL-cursussen voorbijstreeft.
- **Staat nu:** De inhoudelijke diepte is niet het probleem. **De grootste zwakte is cross-module consistentie + feitelijke hygiëne**: prijzen, model-namen, API-feature-namen en speculatieve 2026-cijfers spreken elkaar tussen modules tegen. Voor een product dat je wilt verkopen is dít de prioriteit.
- **Grootste hefboom:** een **centrale "feiten-tabel"** (één bron van waarheid voor prijzen, modelnamen, API-namen) + een **term-linking-laag** (Glossary/Schemas/Cases zijn nu eilanden). Die twee ingrepen lossen het leeuwendeel van de meldingen in één klap op en verhogen de coherentie meer dan welke losse contenttoevoeging ook.
- **Echte bugs:** een handvol code-fouten die bij rendering of uitvoering crashen (dubbele Glossary-keys, `scipy...mcnemar` bestaat niet, kapotte Agent-SDK-import) + verzonnen Claude-Code-feiten (hook-events-tabel). Deze hebben **hoogste prioriteit** — zie §5.
- **Sterkste modules:** TokensContext, Fundamentals, RAG, ToolsMCP, Agents, Backend, Workflows, Security, Deployment, SecondBrain, PromptOps, FineTuning, Evals, AIUX (diepte 5). **Zwakste:** ClaudeDeep (2.5 — "feature-vitrine", mist de beloofde shifts), StructuredOutputs (3), Voice (3).

---

## 2. Content-kaart (dieptescore per module)

| # | Module | Diepte | Categorie |
|---|--------|:------:|-----------|
| Start | Welcome | 3 | oriëntatie, licht didactisch |
| Start | Roadmap | 5 | carrièrepad, zeer rijk |
| Fund | Fundamentals | 5 | referentie |
| Fund | ClaudeModels | 4 | sterk, prijs-inconsistenties |
| Fund | TokensContext | 5 | beste van het boek |
| Fund | ApiKeys | 4 | diepgaand |
| Prompt | PromptingBasics | 5 | v0→v4 = top instructional design |
| Prompt | PromptingAdvanced | 5 | paper-onderbouwd |
| Prompt | PromptPatterns | 4 | array↔matrix-mismatch |
| Prompt | StructuredOutputs | 3 | kortst, naam-chaos |
| Prompt | Evals | 4.5 | graduate-niveau |
| Cap | Skills | 4 | sterk |
| Cap | ToolsMCP | 5 | referentie |
| Cap | ComputerUse | 4 | sterk op security |
| Cap | Agents | 5 | de "hub" |
| Cap | MultiAgent | 4 | Swarm verouderd |
| Cap | Workflows | 5 | uitstekend |
| Cap | RAG | 5 | referentie |
| Cap | Voice | 3 | dun op Claude-relevantie, mist barge-in |
| Mastery | ClaudeDeep | 2.5 | **zwakste** — mist "shifts" |
| Mastery | ClaudeCodeDeep | 4 | rijk, maar verzonnen feiten |
| Mastery | ClaudeCloud | 3.5 | veel onverifieerbare datums |
| Mastery | AgentSDK | 5 | referentie |
| Bouwen | Automation | 5 | ROI-test, n8n-internals |
| Bouwen | SecondBrain | 5 | buitengewoon |
| Bouwen | Frontend | 4.5 | AI SDK v3↔v5-mix |
| Bouwen | AIUX | 5 | production-grade snippets |
| Bouwen | Backend | 5 | productie-grade |
| Bouwen | Deployment | 5 | breed, dubbele secties |
| Bouwen | HostingFree | 4 | concreet |
| Prod | Security | 5 | OWASP compleet, echte CVE's |
| Prod | Guardrails | 4.5 | Colang-versie fout |
| Prod | Observability | 5 | OTEL compleet |
| Prod | PromptOps | 5 | compleet + praktisch |
| Prod | CostOpt | 5 | CostWidget ingebouwd |
| Prod | FineTuning | 5 | 70B/4090-claim fout |
| Prod | Memory | 4 | correcte headers |
| Eco | Ecosystem | 5 | zeer actueel |
| Prakt | Cases | 5 | 12 verticals, asymmetrisch |
| Prakt | WorkflowChecklist | 4 | checklist vinkt niet aan |
| Prakt | Exercises | 4 | telling klopt niet |
| Ref | Schemas | 4 | statisch, niet klikbaar |
| Ref | Glossary | 4 | dubbele entries (bug) |
| Ref | Resources | 4 | Huyen-jaartal fout |

**Gemiddelde diepte ≈ 4,4 / 5.** Voor een NL-studieboek uitzonderlijk hoog.

---

## 3. Gap-analyse — terugkerende patronen (i.p.v. 45 losse tabellen)

De agents leverden per module 5-lagen-checks; de bevindingen clusteren in vijf patronen. De volledige per-module-details staan in de agent-rapporten (agent-ID's onderaan).

### 3a. De laag die het vaakst ontbreekt: **Valkuilen + Context-koppeling**
De meeste modules dekken Wat/Waarom/Toepassing uitstekend. Waar het wringt:
- **ClaudeDeep** heeft 0 valkuilen (Memory-privacy, Computer-use-risico, Artifact-leakage onbenoemd).
- **Voice** mist de #1 voice-valkuil: **barge-in / interruption-handling** + endpointing als latency-knop.
- **StructuredOutputs** mist `max_tokens`-truncatie die JSON afkapt ondanks schema-garantie, en latency-impact van constrained decoding.
- **HostingFree** mist een security-callout: de voorbeeld-Worker is een **open proxy op je Anthropic-key** (geen auth/rate-limit).

### 3b. Modules die als "hub" werken maar niet doorlinken (🔗)
- **Agents** is feitelijk de hub; MultiAgent/AgentSDK/Memory herhalen losse claims (15×-multiplier, 92%/78%, memory-header) zónder kruislink.
- **Schemas** + **Glossary** + **Cases** zijn eilanden: termen (RRF, HNSW, RoPE) linken nergens naar hun definitie/module.
- **Exercises** mapt 1-op-1 op de companion-code-modules maar verwijst er niet naar.
- **AIUX** is de theorie bij de Frontend-oefening maar koppelt niet.

### 3c. Inconsistente interactiviteit
- **WorkflowChecklist** heeft een "checklist" met decoratieve, níet-aanvinkbare vakjes — terwijl **Exercises** (zelfde boek) wél persistente toggles heeft. Hergebruik dat patroon.
- **Welcome** belooft "Markeer per rij waar je nu staat" in de competentie-matrix maar die is statisch.

### 3d. Dubbele/overlappende secties (module-structuur-werk)
- **Deployment**: Monitoring, Kosten en Veiligheid staan elk **twee keer** (twee sprints op elkaar geplakt).
- **Security ↔ Guardrails**: forse overlap (OWASP-mapping, Llama Guard, NeMo). Eén = concepten+incidenten, ander = implementatie, met kruislink.
- **CostOpt ↔ Backend ↔ Workflows**: rate-limit, semantic cache, routing staan 2-3×.
- **FineTuning ↔ CostOpt**: twee distillation-secties die niet van elkaar weten.
- **Voice**: twee bijna-identieke latency-budget-secties.

### 3e. Ontbrekende leerdoelen/samenvatting (🔗 module-structuur)
**WorkflowChecklist** heeft een voorbeeldige "als je maar 3 dingen onthoudt"-afsluiting. **Welcome, Roadmap, Ecosystem, AIUX** missen een expliciet leerdoelen-blok vooraf — goedkope, consistente didactische winst.

---

## 4. Cursus-upgrade kansen — geprioriteerd per type

Alleen kansen die nog **niet** bestaan (Quiz, Exercises, companion-code, Schemas, SRS, mastery en 3 widgets zijn al aanwezig). De sterkste, getagd:

### 🧮 Rekentools (sterkste categorie — sluit aan op bestaande widget-laag)
1. **ROI-calculator (Automation):** input freq/week · min/taak · accuracy · setup-uren · onderhoud → output break-even-dagen + €/maand. *De meest gevraagde tool voor de doelgroep.*
2. **Model-router-besparing (ClaudeModels):** input calls/maand + mix-% simple/medium/complex → kosten naïef-Sonnet vs router.
3. **Cache break-even (TokensContext):** system-prompt-tokens + calls/uur + TTL → break-even-punt + besparing%. Formule staat al in de tekst.
4. **Latency-budget-builder (Voice):** kies STT/LLM/TTS → totale perceived latency, stitched vs native.
5. **API/GPU break-even (FineTuning):** API-€/maand vs GPU-€/uur → break-even-volume voor self-host.
6. **Sample-size-rekentool (Evals):** effect-size + confidence → vereiste N (Cochran-code staat er al, maak 'm interactief).
7. **Self-consistency cost/accuracy (PromptingAdvanced):** N runs + prijs/call + accuracy-bump → kosten vs single-call.
8. **A/B Bayesian-stop (PromptOps):** success/fail per variant → P(challenger wint) + doorlopen/stoppen.
9. **Tier-calculator (ApiKeys):** verwachte RPM+ITPM → benodigde tier + cumulatieve spend.

### 🖼️ Visualisaties / interactief (term-linking is de #1 hefboom)
- **Schemas + Glossary + Cases termen klikbaar** → hover/scroll naar Glossary-definitie. *Grootste didactische winst van het hele boek.*
- **pass@k ↔ pass^k visualizer (Evals):** schuif per-trial success → live curves.
- **U-curve lost-in-the-middle (TokensContext):** naald-positie → retrieval-accuracy.
- **RRF-fusie-widget (RAG):** sleep ranks → gefuseerde score live.
- **Hook-lifecycle-timeline (ClaudeCodeDeep):** wanneer vuurt elk *echt* event over één tool-call.
- **Memory-type sorteerwidget (Memory):** "waar landt dit feit?" → working/episodic/semantic/procedural.
- **Cron-builder (ClaudeCloud):** dropdowns → cron-string + leesbare zin.
- **Schema 10 (multi-agent) + 11 (eval-CI) als Mermaid** — de enige twee waar Mermaid de ASCII echt verbetert (vertakkingen).

### ✏️ Opdrachten (link naar companion-code = quick win)
- **Elke Exercises-set linken naar de bijbehorende companion-code-module** (01-fundamentals … 10-capstone) + per opdracht een inklapbaar "klaar als…"-acceptatiecriterium. Lost meteen het "lerende weet niet wanneer 't goed is"-gat op.
- **PromptingBasics:** geef v0 + golden-set van 5 mails, laat lezer naar v2 itereren in de AISandbox.
- **Security:** schrijf je defense-in-depth system prompt, laat een ander 'm proberen te breken.
- **Guardrails:** redact 5 NL-PII-strings met Presidio + custom BSN-recognizer.

### ✅ Zelftoetsen (uitbreiden bestaand Quiz-systeem)
- **ClaudeCodeDeep "echt of verzonnen hook-event?"** — dwingt meteen het opschonen van de foutieve tabel af.
- **Patroon/techniek-matching:** symptoom → prompt-pattern (PromptPatterns) en symptoom → prompt-techniek (PromptingAdvanced) als quiz-items.
- **Compliance-matching (Cases):** vertical → kader (AVG/MDR/Solvency II/EEOC).
- **Significantie-intuïtie (Evals):** "0.82→0.79 bij N=100 — significant?"

### 🔗 Module-structuur (coherentie)
- Centrale **feiten-tabel** (prijzen/modelnamen/API-namen) waarnaar alle modules verwijzen.
- **ClaudeDeep herpositioneren** rond de 3 denk-shifts (chat→agent, prompt→context, doen→delegeren) i.p.v. feature-vitrine.
- Leerdoelen-blok vooraf in Welcome/Roadmap/Ecosystem/AIUX.

---

## 5. ⚠️ Correctheids- & actualiteitsissues (HOOGSTE PRIORITEIT)

### Categorie A — Echte bugs (crashen bij render/uitvoering) — FIX EERST
| # | Module | Regel | Probleem |
|---|--------|------|----------|
| A1 | Glossary | 11480/11535, 11493/11541, 11499/11545, 11565/11688 | **4 dubbele term-entries** (HNSW, pgvector, Reranker, Constitutional Classifiers) → React duplicate-key-warnings + dubbel zichtbaar |
| A2 | Evals | 12485 | **`scipy.stats.contingency.mcnemar` bestaat niet** → code crasht. Moet `statsmodels.stats.contingency_tables.mcnemar` |
| A3 | Agents | 6900 | **`import { Agent } from "@anthropic-ai/agent-sdk"` + `new Agent()`** bestaat niet; spreekt AgentSDK-module tegen die expliciet waarschuwt "NIET `anthropic.agents`". Moet `query()` / `@anthropic-ai/claude-agent-sdk` |

### Categorie B — Verzonnen/onjuiste Claude-Code-feiten (geloofwaardigheidsrisico)
| # | Module | Regel | Probleem |
|---|--------|------|----------|
| B1 | ClaudeCodeDeep | 13363 | **Hook-events-tabel "~27 events" grotendeels gefabriceerd.** Echte set ≈ 9 (PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStop, SessionStart, SessionEnd, PreCompact). Spreekt zichzelf tegen met regel 13002 |
| B2 | ClaudeCodeDeep | 13429 | **Hook env-vars (`CLAUDE_TOOL_*`) vrijwel allemaal verzonnen** — hooks krijgen JSON op stdin (de module zegt dat zelf correct op 12999). Alleen `CLAUDE_PROJECT_DIR` bestaat |
| B3 | ClaudeCodeDeep | 13571 | **Subagent "15 frontmatter-velden"** — officieel ≈ 4 (name, description, tools, model). Botst met regel 12969 |
| B4 | AgentSDK | 18679 | Hook-lijst "alle 7 types" bevat **`PostToolUseFailure` (bestaat niet)**, mist SubagentStop/Notification |
| B5 | Guardrails | 19168 | **Colang 1.0-syntax gelabeld als "Colang 2.0"** + **Llama Guard als `text-classification`** aangeroepen (is generatief → `text-generation`) |

### Categorie C — Interne tegenstrijdigheden (één bron-van-waarheid maken)
| # | Onderwerp | Conflict |
|---|-----------|----------|
| C1 | **Opus-prijs** | $15/$75 (ClaudeModels 3459) vs $5/$25 (ClaudeModels 3769 + TokensContext 4159). CostWidget = canon |
| C2 | **Modelnamen** | `sonnet-4-6` vs `sonnet-4-7`, `opus-4-6` vs `opus-4-7` door elkaar (Workflows, Backend, Skills, ClaudeCodeDeep) |
| C3 | **Tokenprijzen in code** | Automation 8651 + CostOpt 15801 rekenen Haiku $1/$5; CostWidget = $0.80/$4.00 |
| C4 | **Native structured outputs naam** | `output_config.format` vs `output_schema` vs beta-header `structured-outputs-2025-11-13` (StructuredOutputs + PromptPatterns) |
| C5 | **thinking/effort API-vorm** | `thinking={"type":"adaptive","effort":...}` (PromptingAdvanced 5133) vs los `effort="high"` (ClaudeModels 3955) |
| C6 | **OTEL GenAI-status** | "stabiel v1.36+" (Observability 18192) vs "experimental" (Workflows 7742) |
| C7 | **GraphRAG-cijfers** | "80% vs 50%" (RAG 8027) vs "91% vs 34%" (RAG 8303) — binnen dezelfde module |
| C8 | **Chip Huyen jaartal** | "2024" (Resources 11832) vs "2025" (11919). 2025 is correct |
| C9 | **brew-install** | `brew install anthropics/claude/claude` (ClaudeDeep 12668) vs `brew install --cask claude-code` (ClaudeCodeDeep 12753) |
| C10 | **Fly.io free tier** | "geen free tier" (HostingFree 15174) vs "beperkt free" (Deployment 10314) |
| C11 | **Exercises-telling** | "130+/100 vaardigheden" beloofd, feitelijk 57 opdrachten |
| C12 | **Hetzner** | CX11 €4.13 (HostingFree) vs CX22 (SecondBrain) — CX11 uitgefaseerd |

### Categorie D — Verouderde feiten
| # | Module | Probleem |
|---|--------|----------|
| D1 | MultiAgent (18104) | **OpenAI Swarm** als levende optie — is vervangen door OpenAI Agents SDK. Cognition-blogpost gedateerd "juni 2024" → is 2025 |
| D2 | Frontend (9252) | **AI SDK v3-syntax** (`ai/react`, `m.content`, `toDataStreamResponse`, `maxSteps`) in eerste voorbeeld; v5 elders. `MockLanguageModelV1` → V2 |
| D3 | Automation/SecondBrain | **`n8n-nodes-base.cron`** gedeprecieerd → `scheduleTrigger` |
| D4 | Backend (9978) | `prompt-caching-2024-07-31` beta-header — caching is GA, geen header nodig |
| D5 | Deployment/HostingFree | Cloudflare Worker "10ms CPU free" — verhoogd sinds 2024 |
| D6 | FineTuning (19543) | **"70B full FT op één RTX 4090"** kan niet (past niet in 24GB); code traint 8B. $1500/4090-claim slaat op 8B |

### Categorie E — Onverifieerbaar-precieze claims → label als "schatting/vendor/check docs"
- Speculatieve toekomst-benchmarks: GPT-5.4/5.2, Gemini 3.1, "Opus 4.7 87.6% SWE-bench" (ClaudeModels 3666); SWE-bench 80.8% (Ecosystem 10943); HalluLens per-model-% (Fundamentals 3403)
- Managed Agents endpoints/pricing ($0.08/uur) + klantnamen Notion/Rakuten/Sentry/Asana (ClaudeCloud 14105)
- Exacte launch-datums Cowork/Dispatch/Routines (ClaudeCloud)
- Versienummers v2.1.141 / v2.1.83 (ClaudeCodeDeep)
- Salary-cijfers (Roadmap), ROI-cijfers (Cases), n8n $40M ARR / 183k stars (Ecosystem), €147M voice-boetes (Voice), framework-stars (MultiAgent) — allemaal als "gerapporteerd/peildatum" hedgen
- Skills token-budgetten (6223/6228), Tool Search accuracy-cijfers
- `cache_control={"type":"auto"}` (TokensContext 4118) — verifieer of dit echt bestaat

### ✅ Wat WÉL correct geverifieerd is (geruststelling)
OWASP LLM Top-10 2025-categorieën · EchoLeak CVE-2025-32711 · CVE-2025-6514 (mcp-remote) · Memory-tool-header `context-management-2025-06-27` + `memory_20250818` · Batch API 50% · cache-TTL (5m default sinds maart 2026, 1.25×/2× writes) · EU AI Act-datums + 7% boete · BSN 11-proef-gewichten · Helicone maintenance-mode (Observability + CostOpt + Ecosystem) · Contextual Retrieval 49%/67% · RRF k=60 · paper-IDs (Reflexion, Zep, G-Eval, Step-Back, Lost-in-the-Middle) · MCP SSE-deprecation 2025-03-26.

---

## 6. Prioritering & roadmap

### Quick wins (hoge impact, lage inspanning) — ~1 dag
1. **Fix Categorie A** (3 bugs) — Glossary de-dupe, mcnemar→statsmodels, Agent-SDK-import.
2. **Fix Categorie C** prijzen + modelnamen via één find-replace-pass naar de CostWidget-waarden + één modelnaam-conventie.
3. **Fix C8/C9/C11/C12** (Huyen-jaartal, brew, Exercises-telling, Hetzner).
4. **WorkflowChecklist aanvinkbaar maken** (hergebruik Exercises-toggle).
5. **Helicone-warning** ook in Resources.

### Kernupgrades (hoge impact, hoge inspanning) — de ruggengraat
1. **Centrale feiten-tabel** + alle modules eraan koppelen (lost C1-C5 structureel op).
2. **Hook-events + subagent-velden herschrijven** naar de echte set (B1-B4) + speculatie-disclaimers bij alle versienummers/datums (Categorie E).
3. **Term-linking-laag** (Schemas/Glossary/Cases → definities/modules).
4. **3-4 nieuwe rekentools** (ROI, model-router, cache break-even, latency-budget).
5. **Exercises ↔ companion-code koppelen** + acceptatiecriteria per opdracht.
6. **Deployment ontdubbelen** + Security/Guardrails afbakenen.

### Moonshots (ambitieus, later)
1. **ClaudeDeep herschrijven** rond de denk-shifts (van vitrine naar intellectuele kern).
2. **Voice verdiepen**: barge-in/endpointing als aparte sectie.
3. **Interactieve concept-visualisaties** (pass@k, lost-in-the-middle U-curve, RRF-fusie, Mermaid voor schema 10/11).
4. **Cron-builder + memory-sorteerwidget** als nieuwe widget-familie.

### Gefaseerd plan (module-voor-module, reviewbaar)
- **Fase 1 (correctheid):** Quick wins 1-5. *Eén bron van waarheid + geen crashes/verzonnen feiten.*
- **Fase 2 (coherentie):** Kernupgrade 1-3 + 5-6. *Eilanden verbinden, dubbelingen weg.*
- **Fase 3 (didactiek):** Kernupgrade 4 + Moonshots 1-2. *Rekentools + ClaudeDeep + Voice.*
- **Fase 4 (premium-glans):** Moonshots 3-4.

---

## Eerlijke slotsom

De inhoud is al top-tier voor de NL-markt — diepte 4,4/5 gemiddeld is uitzonderlijk. **Wat het nog van "uitstekend studieboek" naar "verkoopbaar premium-product" tilt is geen extra content, maar feitelijke betrouwbaarheid en interne consistentie.** Een koper die twee verschillende Opus-prijzen of een verzonnen hook-tabel ontdekt, verliest vertrouwen in de rest — ook in de 90% die wél klopt. Fase 1 (één dag) is daarom verreweg de belangrijkste investering: het beschermt de geloofwaardigheid van het hele boek.

---

*Agent-rapporten (volledige per-module-details) — cluster A: `a7fb52a7926ab5d1f` · B: `a9c07b0f3d539a529` · C: `a1194504a6b7e1259` · D: `a4f9a2f13ed4ee573` · E: `a4c7c262308b92526`. Stuur me naar een ID voor diepere detail per module.*
