# Promptmeester

**Leer bouwen met AI — in het Nederlands, vanaf nul.** Het interactieve handboek waarmee iedereen leert werken met Claude en AI: geen programmeer-achtergrond nodig. Van je eerste prompt tot complete AI-systemen die echt werk uit handen nemen. Single-page React-app, geen backend nodig.

![Vanaf nul](https://img.shields.io/badge/niveau-vanaf%20nul-orange) ![44 modules](https://img.shields.io/badge/modules-44-orange) ![Nederlandstalig](https://img.shields.io/badge/taal-NL-orange)

## Wat zit erin

**44 modules** in 10 categorieën, ~19.000 regels inhoud:

- **Fundamenten** — LLM's, Claude-modellen, tokens & context, API-keys, sampling
- **Prompting** — basics (POWER, v0→v4), advanced (XML, CoT, self-consistency), 16 patterns, structured outputs, evals
- **Capabilities** — Skills, Tools & MCP, Computer Use, agents, multi-agent orchestration, RAG, voice
- **Claude Mastery** — het Claude-universum, Claude Code (CLI), Cowork/Dispatch/Routines, Agent SDK
- **Bouwen** — automation (n8n), second brain, frontend (AI SDK), AI UX patterns, backend (FastAPI), deployment, gratis hosting
- **Productie** — security & prompt injection, guardrails, observability, prompt ops, kosten, fine-tuning, agent memory
- **Praktijk & Referentie** — cases per industrie, workflow checklist, 130+ oefeningen, schema's, 220+ termen woordenboek, bronnen

Plus een **[companion-code repo](./companion-code/)** met 57 paste-and-run bestanden in 10 priority-modules — van eerste API-call tot een complete capstone customer-support-agent.

## Interactieve features

- 🔗 **Hash-routing** — elke module heeft een deelbare URL
- ⌘K **Command palette** — fuzzy search door alle modules
- 📋 **Copy-knoppen** op elk codeblok
- 📑 **In-page TOC** met scroll-spy
- ✅ **Voortgang** — module-completion, oefening-checkboxes, streak-counter
- 🧪 **Quiz-modus** — 96 vragen over 32 modules
- 🤖 **AI-Tutor** — BYOK chat over de huidige module
- 🎨 **3 thema's** — dark / light / sepia
- 💾 **JSON export/import** van je voortgang
- 🖨️ **Print-stylesheet**

## Stack

- Vite 6 + React 18
- Tailwind CSS 3 (utility-first)
- lucide-react voor icons
- Persistentie via `localStorage` (geen backend)

## Aan de slag

```bash
npm install
npm run dev      # dev server op http://localhost:5175
npm run build    # productie-build naar dist/
npm run preview  # preview van de build
```

## Structuur

```
.
├── index.html
├── public/favicon.svg
├── src/
│   ├── main.jsx            # entry
│   ├── index.css           # Tailwind + print-styles
│   └── App.jsx             # alle inhoud in één file (~19.000 regels)
├── companion-code/         # 57 paste-and-run code-voorbeelden
├── AUDIT.md                # content-audit rapport
├── MASTER-EXPANSION-PLAN.md
├── CHANGELOG.md
├── tailwind.config.js
├── vite.config.js          # poort 5175, strictPort
├── vercel.json             # SPA-rewrites
└── netlify.toml
```

Alle modules zitten in één `App.jsx` — bewust, voor laagdrempeligheid. Zie [CONTRIBUTING.md](./CONTRIBUTING.md) voor de conventies.

## Deployen

Gratis te hosten op Vercel, Netlify, Cloudflare Pages of GitHub Pages. Zie [DEPLOY.md](./DEPLOY.md).

## Licentie

[MIT](./LICENSE) — vrij te gebruiken voor eigen projecten, interne trainingen en presentaties.

---

*Promptmeester — gemaakt zodat iedereen leert bouwen met AI, niet alleen programmeurs. Nederlandstalig, omdat materiaal op dit niveau in het Nederlands nergens anders bestaat. Begin bij nul, eindig met systemen die echt werk uit handen nemen.*
