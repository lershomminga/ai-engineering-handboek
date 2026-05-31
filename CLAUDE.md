# Claude Engineering Handboek

Interactief, Nederlandstalig studieboek (single-page React app) waarin alles staat over Claude / AI engineering: fundamenten, prompting, skills, MCP, agents, RAG, automation, frontend/backend, deployment, ecosystem, woordenboek.

> **Geparkeerd / hervatten:** zie `NEXT-STEPS.md` voor de huidige stand en de volgende stap (video-walkthroughs opnemen, faceless-first). Lees dat eerst bij het oppakken van werk.

## Stack

- Vite 6 + React 18
- Tailwind CSS 3 (utility-first; geen shadcn)
- lucide-react voor icons
- Persistentie via `localStorage` (geen backend)

## Scripts

- `npm run dev` — dev server op **poort 5175** (strictPort, opent browser automatisch — zie `vite.config.js`)
- `npm run build` — productie build naar `dist/`
- `npm run preview` — preview van de build

## Structuur

```
.
├── index.html              # HTML shell, link naar /favicon.svg
├── public/favicon.svg      # oranje vierkant + witte Sparkles
├── src/
│   ├── main.jsx            # entry, mount React
│   ├── index.css           # Tailwind directives + height:100%
│   └── App.jsx             # ALLE inhoud in één file (~19.000 regels, 45 modules na Master Expansion Plan mei 2026)
├── companion-code/         # 57 paste-and-run code-voorbeelden, 10 priority-modules
├── tailwind.config.js
├── postcss.config.js
├── vite.config.js          # poort 5175, strictPort, open: true
├── vercel.json             # SPA-rewrites voor Vercel deploy
├── netlify.toml            # Netlify build + redirects
├── README.md · LICENSE · CHANGELOG.md · CONTRIBUTING.md
└── DEPLOY.md               # gratis hosting handleiding
```

## Conventies in `App.jsx`

- **Eén file, vele functies.** Per module een eigen function-component (`Welcome`, `Roadmap`, `Fundamentals`, `ClaudeModels`, `ClaudeDeep`, `ClaudeCodeDeep`, `ClaudeCloud`, `Evals`, `SecondBrain`, `HostingFree`, `Security`, `CostOpt`, ...). De hoofdcomponent `ClaudeHandbook` regelt routing via `activeModule` state en `getModuleContent(id, ...)`.
- **Categorieën** in de zijbalk: Start, Fundamenten, Prompting, Capabilities, **Claude Mastery**, Bouwen, **Productie**, Ecosysteem, **Praktijk**, Referentie.
- **Bundle warning:** Vite waarschuwt dat de bundel > 500 kB is. Dat is verwacht voor een studieboek met deze hoeveelheid inhoud op één pagina. Geen actie nodig tenzij je code-splitting wilt invoeren.
- **Theme als prop.** Dark/light/sepia wordt afgehandeld door een `theme` object (kleurklassen) dat naar elke module wordt doorgegeven. `themeMode` cyclet door de drie. Geen Tailwind dark-mode-class systeem.
- **Helpers in `App.jsx`:** `H1`, `H2`, `H3`, `P`, `InlineCode`, `Pre` (met copy-knop), `Callout` (kind: tip/warn/success), `Card`. Plus losse componenten: `CommandPalette`, `TableOfContents`, `Quiz`, `AISandbox`.
- **Belangrijke naam-collisie:** lucide-react exporteert een icon `Code`. Onze inline-code helper heet daarom `InlineCode` (niet `Code`). Niet hernoemen tenzij je ook de import aanpakt.
- **JSX-valkuilen:** letterlijke `>`/`<` in tekst → `{">"}` of `&gt;`. `$` in template-literals binnen `<Pre>` → escape als `\$`. Voorbeeld-JSON met curly braces → wrap in template-string.
- **Persistentie keys:** `completed`, `notes`, `exerciseProgress`, `themeMode`, `streak`, `quizScores` in `localStorage`. (`darkMode` was de oude key — wordt nog gemigreerd naar `themeMode`.)
- **Module IDs** zitten gehardcoded in de `modules` array bovenin `ClaudeHandbook` én in de switch in `getModuleContent`. Bij een nieuwe module: beide updaten.
- **Hash-routing:** `activeModule` ↔ `window.location.hash` (`#/module-id`). Quiz-data in `QUIZZES` object; bij nieuwe module-quiz: daar een entry toevoegen.

## Inhoud-regels

- Nederlandstalig, directe toon, niet té formeel.
- Code in `<Pre>` blokken als plain text (geen syntax highlighting).
- Geen externe links als markdown — gebruik gewone tekst (zie `Resources`-sectie). Markdown links worden door de pipeline soms verminkt tot `[foo.com](http://foo.com)`.

## Niet doen

- Geen nieuwe top-level files toevoegen zonder reden — hou het bij de bestaande structuur.
- Geen TypeScript — bewust JS gehouden voor laagdrempeligheid.
- Geen routing-library — `activeModule` state is genoeg.
