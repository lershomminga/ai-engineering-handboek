# Bijdragen aan het Claude Engineering Handboek

Fijn dat je wilt bijdragen. Lees dit eerst — de architectuur is bewust ongebruikelijk.

## Het grote principe: één file

Alle 44 modules zitten in **`src/App.jsx`** (~19.400 regels). Dat is geen ongeluk:
het houdt de drempel laag (geen build-magie, geen file-hopping) en maakt full-text
zoeken triviaal. Niet opsplitsen zonder zwaarwegende reden.

## Conventies in App.jsx

- **Eén function-component per module** (`Welcome`, `Fundamentals`, `RAG`, …). De
  hoofdcomponent `ClaudeHandbook` regelt routing via `activeModule`-state en
  `getModuleContent(id, ...)`.
- **Module-IDs staan op twee plekken**: de `modules`-array bovenin `ClaudeHandbook`
  én de switch in `getModuleContent`. Bij een nieuwe module: beide updaten.
- **Helpers**: `H1`, `H2`, `H3`, `P`, `InlineCode`, `Pre`, `Callout` (kind:
  tip/warn/success), `Card`. Gebruik deze — niet je eigen markup.
- **Naam-collisie**: lucide-react exporteert een icon `Code`. Onze inline-code-helper
  heet daarom `InlineCode`. Niet hernoemen tenzij je ook de import aanpakt.
- **Theme als prop**: dark/light/sepia via een `theme`-object dat naar elke module
  wordt doorgegeven. Geen Tailwind dark-mode-class systeem.
- **Persistentie-keys** in `localStorage`: `completed`, `notes`, `exerciseProgress`,
  `themeMode`, `streak`, `quizScores`.

## Inhoud-regels

- **Nederlandstalig**, directe toon, niet té formeel.
- **Code in `<Pre>` blokken** als plain text (geen syntax highlighting).
- **Geen markdown-links in body** — gebruik gewone tekst of de helpers. De pipeline
  verminkt soms `[foo](http://foo)` tot rommel.
- **JSX-valkuilen**: letterlijke `>` en `<` in tekst → gebruik `{">"}` of `&gt;`.
  `$` in template-literals binnen `<Pre>` → escape als `\$`. Curly-braces in
  voorbeeld-JSON → wrap in `{`...`}` template-string.
- **Citeer cijfers**: een claim met getal hoort een bron te hebben.

## Companion-code

Elke folder in `companion-code/` heeft: README.md, requirements.txt (of
package.json), .env.example en genummerde scripts. Houd code **paste-and-run** —
binnen 5 minuten draaiend. Geen secrets in code, alleen via env-vars.

## Niet doen

- Geen nieuwe top-level files zonder reden.
- Geen TypeScript in de app (bewust JS gehouden).
- Geen routing-library (`activeModule`-state is genoeg).
- Geen secrets committen (`.env` staat in `.gitignore`).

## Workflow

1. `npm run dev` — controleer je wijziging visueel op poort 5175.
2. `npm run build` — moet slagen zonder errors. De bundle-warning (>500 kB) is
   verwacht voor een studieboek van deze omvang; negeer die.
3. Houd commits gericht; beschrijf in de message *wat* en *waarom*.
