# Volgende stappen — geparkeerd

> Laatst bijgewerkt: 2026-05-31. Dit bestand is het geheugen tussen sessies.
> Lees dit eerst bij hervatten.

## Vóór echte launch nog checken (door Lars zelf)

- **Merknaam "Promptmeester" beschikbaarheid** — domein (promptmeester.nl),
  KvK/handelsnaam, social handles. Lars checkt dit bij echte launch en past de
  naam evt. aan. De rebrand is reversibel: naam zit in `src/App.jsx` (header +
  hero), `index.html`, `public/favicon.svg`, `package.json`, `README.md`,
  `CLAUDE.md`. Eén vind-vervang-pass volstaat voor een nieuwe naam.

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
