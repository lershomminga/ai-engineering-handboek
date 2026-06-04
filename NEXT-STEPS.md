# Volgende stappen — geparkeerd

> Laatst bijgewerkt: 2026-05-31. Dit bestand is het geheugen tussen sessies.
> Lees dit eerst bij hervatten.

## Vóór echte launch nog checken (door Lars zelf)

- **Merknaam "Promptmeester" beschikbaarheid** — domein (promptmeester.nl),
  KvK/handelsnaam, social handles. Lars checkt dit bij echte launch en past de
  naam evt. aan. De rebrand is reversibel: naam zit in `src/App.jsx` (header +
  hero), `index.html`, `public/favicon.svg`, `package.json`, `README.md`,
  `CLAUDE.md`. Eén vind-vervang-pass volstaat voor een nieuwe naam.

## Studieboek-audit Fase 1 (correctheid) — AFGEROND juni 2026

Volledig audit-rapport: `STUDIEBOEK-AUDIT.md`. Fase 1 (4 blokken) uitgevoerd + gepusht:
- Blok 1: crash-bugs (Glossary-dupes, mcnemar→statsmodels, Agent-SDK import)
- Blok 2: prijzen + modelnamen → één canon (Opus $5/$25, Sonnet $3/$15, Haiku $1/$5; sonnet-4-7→4-6)
- Blok 3: verzonnen Claude-Code-feiten (hook-events 27→9, env-vars→stdin, subagent-velden, AgentSDK hooks)
- Blok 4: consistentie + verouderd (GraphRAG, OTEL, Huyen, Fly, Hetzner, Swarm→Agents SDK, AI SDK v5, n8n scheduleTrigger, Cloudflare CPU, FineTuning 70B)

## Studieboek-audit Fase 2 (coherentie) — AFGEROND juni 2026

- Blok A: WorkflowChecklist aanvinkbaar (echte toggles via `exerciseProgress`,
  voortgangsbalk + per-categorie teller)
- Blok B: Glossary `related`-veld klikbaar (term-linking-laag → zoek-filter)
- Blok C: Exercises ↔ companion-code gelinkt (`EXERCISE_REPOS`-map, paste-and-run-regel per hoofdstuk)
- Blok D: Deployment-module ontdubbeld (ondiepe Monitoring/Kosten/Veiligheid weg,
  diepere versies behouden, prompt-injection-Callout verplaatst)

## Studieboek-audit Fase 3 (didactiek) — DEELS afgerond juni 2026

- Rekentools (4 interactieve widgets) live + live-geverifieerd + gepusht:
  CacheBreakEvenWidget, ModelRouterWidget, RoiWidget (→ CostOpt),
  LatencyBudgetWidget (→ Deployment). Wiskunde live nagerekend, klopt.
- **Crash-fix (Categorie A):** Deployment-module crashte volledig op
  `gen_ai is not defined` — losse JSX-expressie `{gen_ai.agent.name}` in de
  OTEL-tekst i.p.v. in een string. Build ving dit niet. Nu gewrapt in InlineCode.
- **Smoke-test:** alle 44 modules in de browser gecheckt — allemaal renderen,
  geen lege/gecrashte modules, console schoon. (Methode: hash-sweep + main-len/heads.)

## Studieboek-audit Fase 4 (Categorie E + feiten) — AFGEROND juni 2026

- Nieuw `PeildatumNote`-component (centrale `PEILDATUM`-constante) bij alle
  speculatieve cijfer-clusters: ClaudeModels-benchmarks, Fundamentals HalluLens,
  Roadmap-salarissen (2×), Ecosystem n8n-stats, ClaudeCloud Managed Agents,
  Voice-boetes, TokensContext cache "auto"-toggle.
- Feitelijke fixes: Ecosystem 80.8%→87.6% SWE-bench (consistent met ClaudeModels);
  cache_control "auto" gemarkeerd als niet-gegarandeerd (alleen "ephemeral" gedoc.).
- MultiAgent framework-stars hadden al inline-disclaimer.

Voice barge-in-sectie: AFGEROND (juni 2026) — "Barge-in: de gebruiker mag je
onderbreken" in de Voice-module (detectie/stop/cancel/context-truncate + code +
echo-cancellatie + backchannel-tuning).

**Nog te doen (laatste audit-item):** ClaudeDeep herschrijven rond denk-shifts
(substantiële content-herstructurering van één module). Dit is het énige
resterende item uit het hele audit-plan. Centrale feiten-tabel: gedeprioriteerd
(canon staat al in TokensContext + Glossary).

## Educatieve diepte-laag (toegevoegd juni 2026)

Vier leermechanismen live, getest en gepusht:
1. **Spaced repetition** — SM-2-lite over quizvragen, geseed na quiz, herhaal-badge
2. **Confidence-calibratie** — zekerheid vóór onthulling + calibratie-eindscherm
3. **Interactieve widgets** — tokenizer, temperature-visualizer, kosten-calculator
4. **Mastery-voortgang** — "Beheersing"-metric (gelezen→getoetst→beheerst) + sidebar-dots

Mogelijke vervolg-edu-ideeën (uit eerdere analyse, nog niet gedaan):
misconceptie-kaarten per module · faded/completion-code in companion-code ·
diagnostische pretest · self-explanation prompts (typ-het-zelf vóór samenvatting).

## Waar staan we

Het merk is **Promptmeester** (richting A: eigen woordmerk, Claude = onderwerp).
Positionering: breed/toegankelijk — "iedereen leert bouwen met AI, vanaf nul,
geen programmeer-achtergrond nodig". Geen persoonlijke auteursnaam toegevoegd
(woordmerk-pad gekozen); kan later een "door [naam]"-regel krijgen.

Het hele **Master Expansion Plan is uitgevoerd, gecommit en gepusht** naar
`origin/main` (`github.com/lershomminga/ai-engineering-handboek`). Stand:

- 45 modules, ~19.400 regels in `src/App.jsx`
- Companion-code repo (`companion-code/`, 57 bestanden, 10 priority-modules)
- Volledige interactieve laag: hash-routing, ⌘K-palette, quiz (96 vragen),
  AI-Tutor (BYOK), 3 thema's, in-page TOC, copy-knoppen, streak, JSON-sync
- Project-docs compleet: README, LICENSE, CHANGELOG, CONTRIBUTING, SEO-meta
- **Video-infrastructuur klaar** (`VideoEmbed`-component) + 10 opname-scripts +
  faceless-first setup-gids in `video-scripts/`

Build slaagt, dev-server draait op poort 5175. Werktree schoon.

## Wat geparkeerd is: de video-walkthroughs opnemen

**Besluit genomen:** faceless-first (scherm + stem, geen camera). Gezicht later
toevoegen via bookend-intro's, zonder de kern opnieuw op te nemen.

**Tooling-keuze (jij kiest bij hervatten):**
- **OBS Studio + DaVinci Resolve** — gratis, aanbevolen voor faceless. OBS-settings
  staan in `video-scripts/00-recording-setup.md`.
- **Loom Business+AI** — $24, 1 maand, dan opzeggen. Alleen als je wilt dat AI
  automatisch "uhh"s + stiltes wegknipt. Gratis Loom valt af (5-min cap, geen download).

**De 10 scripts** staan klaar in `video-scripts/01-…md` t/m `10-…md`. Beat-sheets,
beginnen met Welcome (laagste risico). Richtduur totaal: ~3,5-5,5u ruwe opname.

### Drie dingen om faceless-opnames "gezicht-later-klaar" te houden
1. Bewaar de ruwe opnames in volle resolutie (niet weggooien na upload).
2. Spreek in segmenten met natuurlijke pauzes tussen beats.
3. Geen "kijk-naar-mij"-taal in de voiceover.

## Hoe een opgenomen video koppelen (als je een MP4 hebt)

1. Upload naar host: **Cloudflare Stream** (premium, geen branding, ~$1/1000 min)
   of **YouTube unlisted** (gratis). De `VideoEmbed` detecteert beide automatisch
   (ook Vimeo, Loom, directe mp4).
2. In `src/App.jsx`, in de `modules`-array bovenin `ClaudeHandbook`, voeg toe aan
   de betreffende module:
   ```js
   video: { url: "https://youtu.be/XXXX", duration: "5:12" }
   ```
3. `npm run build` om te verifiëren, dan committen + pushen.

## Openstaande hulp die ik kan bieden bij hervatten

- **YouTube-beschrijvingen** per video schrijven (SEO-titel + beschrijving +
  hoofdstuk-tijdstempels + thumbnail-tekst, copy-paste-klaar) — geen Chrome nodig.
- **Live-deploy verifiëren** via Chrome — checken of de VideoEmbed-player rendert.
- **OBS-downloadpagina openen** via Chrome zodat je meteen kunt installeren.
- **GitHub repo vindbaar maken** — description + topics (claude, ai-engineering,
  nederlands, llm) — als je dat alsnog wilt.

## Verkooppositie (referentie)

- Nu (handboek + companion-code + scripts): **€169-189 lifetime** verdedigbaar.
- Mét opgenomen video's erin: **€99-149** boost → richting €249-299.
- Plus cohort/community (live element): €299+.

## Achtergronddocumenten

- `MASTER-EXPANSION-PLAN.md` — het volledige plan + Top-50 (uitgevoerd)
- `AUDIT.md` — oorspronkelijke discovery
- `Master-Expansion-Plan.pdf` / `Upgrade-Roadmap.pdf` — geprinte versies
- `video-scripts/README.md` — top-10 lijst + hosts + hoe activeren
- `video-scripts/00-recording-setup.md` — gear, OBS-settings, faceless-first
