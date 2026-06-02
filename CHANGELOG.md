# Changelog

Alle noemenswaardige wijzigingen aan het Claude Engineering Handboek.
Formaat losjes gebaseerd op [Keep a Changelog](https://keepachangelog.com/).

## [2.1.0] — 2026-06-02 — "Educatieve diepte-laag + Promptmeester rebrand"

### Rebrand
- Merknaam **Promptmeester** (eigen woordmerk, Claude = onderwerp)
- Brede positionering: "iedereen leert bouwen met AI, vanaf nul" — geen
  programmeer-achtergrond vereist
- Fraunces "P" lettermark, hero "Word meester over AI", SEO herschreven

### Toegevoegd — leermechanismen (op basis van leerwetenschap)
- **Spaced repetition (SRS)** — SM-2-lite over quizvragen; kaarten geseed na
  quiz-voltooiing, herhaal-badge in header, review-overlay
- **Confidence-calibratie** — quiz vraagt zekerheid vóór onthulling; eindscherm
  toont zelfvertrouwen-vs-werkelijkheid + overmoed/onderschatting-insight
- **Interactieve widgets** — live tokenizer (token-tax NL/EN), temperature-
  visualizer (kansverdeling), kosten-calculator (model+volume+cache+batch)
- **Mastery-voortgang** — tweede metric "Beheersing" naast "Voortgang":
  gelezen → getoetst → beheerst, met per-module gekleurde dots in de sidebar

### Bugfix
- `useRef` ontbrak in React-import (gebruikt in SmoothText e.a.) — zou bij
  render crashen; toegevoegd
- Video-embed-infrastructuur (`VideoEmbed`) + 10 faceless-first opname-scripts
- Jaartal losgemaakt van merk-badge

## [2.0.0] — 2026-05-31 — "Master Expansion Plan"

De grootste uitbreiding tot nu toe. 8 parallelle deep-research agents brachten
elke module in kaart; daarna 8 sprints uitgevoerd. App.jsx ging van 15.246 → 19.365 regels.

### Toegevoegd — nieuwe modules
- **Structured Outputs** — tool-use, native GA (`output_config.format`), Instructor
- **Computer Use** — sandbox-harness, Docker-setup, screenshot-diff, action-replay
- **Multi-agent Orchestration** — LangGraph, framework-matrix, Verifier-Critic, budget-control
- **Agent SDK** — Python + TypeScript, hooks, sessions V2, deployment patterns
- **Voice & Speech** — Vapi, OpenAI Realtime, sub-300ms TTS, NL/GDPR-compliance
- **AI UX Patterns** — smooth-typing, branching, tool-call rendering, citations
- **Guardrails** — NeMo, Llama Guard 3, Presidio NL-config, defense-in-depth
- **Observability** — OTEL GenAI reference, Langfuse self-host, trace-linking
- **Prompt Ops** — versioning, registry, CI-gating, A/B-testing
- **Fine-tuning & Adaptation** — QLoRA (Unsloth), distillation, synthetic data
- **Agent Memory** — Tulving-taxonomie, Zep/Graphiti, conflict-resolution, GDPR-forget

### Toegevoegd — features
- Hash-routing met deelbare URLs per module
- ⌘K command palette (fuzzy search)
- Copy-knoppen op alle codeblokken
- In-page table-of-contents met scroll-spy
- Quiz-modus: 96 vragen over 32 modules
- AI-Tutor met BYOK (chat over huidige module)
- Sepia-thema (naast dark/light)
- Streak-counter + oefening-checkboxes
- JSON export/import van voortgang
- Print-stylesheet
- Prev/next-navigatie onderaan elke module
- **Companion-code repo** — 57 paste-and-run bestanden in 10 priority-modules

### Gewijzigd — bijgewerkt naar mei 2026
- Structured Outputs naar GA-API (was beta-header)
- Memory Tool naar `context-management-2025-06-27` / `memory_20250818`
- Prompt cache: 5-min default, 20-block lookback gotcha, automatic toggle
- API rate-limits + Admin API + exponential backoff (429 vs 529)
- MCP-ecosysteem cijfers (9.652 servers in Registry)
- Helicone gemarkeerd als maintenance-mode
- Glossary uitgebreid van 93 → 220+ termen
- Roadmap met Claude Certified Architect + quick-start paden + 10 portfolio-projecten
- 6 nieuwe schema-diagrammen
- Resources met NL-bronnen + community-events

### Verwijderd
- Gedupliceerde RAG-secties (Contextual Retrieval, GraphRAG, hybrid search stonden 2×)

## [1.2.0] — 2026-05 — "Visual redesign"
- Serif display-font (Fraunces) + warm cream-palet
- Hoofdstuk-nummering
- 5 densste hoofdstukken geherstructureerd (cards/callouts i.p.v. wall-of-text)
- Workflow Checklist & 20 Prompt-Wetten toegevoegd

## [1.1.0] — 2026 — "Content expansion"
- Major content-uitbreiding over 19 hoofdstukken (deep research)
- Fact-check pass + studieboek-vorm met openings & samenvattingen
- 5-laags Agent Development Kit model in Claude Code-hoofdstuk

## [1.0.0] — 2026 — "Initial release"
- Eerste versie van het Claude Engineering Handboek
