# Video-walkthroughs — productie-pakket

Alles wat je nodig hebt om 10 module-walkthroughs op te nemen, zónder eerst te
moeten bedenken wát je gaat zeggen. Elk script is een **beat-sheet**: talking
points + "toon-op-scherm"-cues, geen woord-voor-woord teleprompter (dat klinkt
robotachtig). Je improviseert de exacte zinnen — het script houdt je op koers.

> **Faceless-first.** Begin zonder camera: scherm + stem. Geen licht/camera-
> frictie, één variabele (audio). Je gezicht koppel je later toe via bookend-
> intro's. Zie `00-recording-setup.md` → "Faceless-first".

## De top-10 (volgorde van opnemen)

Begin met Welcome — die video verkoopt het hele product en oefent je presenteer-
ritme op laag-risico materiaal.

| # | Module | Script | Richtduur | Waarom video hier waarde toevoegt |
|---|--------|--------|----------:|-----------------------------------|
| 1 | Welcome | `01-welcome.md` | 4-6 min | Verkoopt het product, zet de toon |
| 2 | Roadmap | `02-roadmap.md` | 8-12 min | Leerpad visueel maken |
| 3 | Prompting Basics | `03-prompting-basics.md` | 15-25 min | Live een prompt van v0→v4 itereren |
| 4 | Prompting Advanced | `04-prompting-advanced.md` | 20-30 min | CoT/thinking live tonen |
| 5 | Tools & MCP | `05-tools-mcp.md` | 25-35 min | MCP-server bouwen + connecten live |
| 6 | Agents | `06-agents.md` | 25-35 min | Agent-loop live debuggen |
| 7 | RAG | `07-rag.md` | 30-40 min | Build-along met companion-code |
| 8 | Evals | `08-evals.md` | 20-30 min | LLM-as-judge live opzetten |
| 9 | Computer Use | `09-computer-use.md` | 15-25 min | De demo verkoopt zichzelf |
| 10 | Capstone | `10-capstone.md` | 30-45 min | Het hele plaatje samenbrengen |

**Totaal: ~3,5-5,5 uur ruwe opname** → na editing ~3-4,5u publiceerbaar. Dat is
de "5-10u walkthroughs" uit het advies, realistisch ingeschat.

## De videoplayer in het handboek

De app heeft een `VideoEmbed`-component. Activeren = één regel per module in de
`modules`-array bovenin `src/App.jsx`:

```js
{ id: "welcome", title: "Welkom", icon: Sparkles, category: "Start",
  lastUpdated: "2026-05-09",
  video: { url: "https://youtu.be/XXXXXXXXXXX", duration: "5:12" } },
```

Ondersteunde providers (auto-detect): **YouTube, Vimeo, Loom, Cloudflare Stream**,
of een directe `.mp4`-URL. De player rendert collapsed bovenaan de module; klik =
uitklappen (16:9, fullscreen-capable). Niets ingevuld = geen player.

### Welke host?

| Host | Kosten | Wanneer |
|------|--------|---------|
| **Cloudflare Stream** | ~$1 / 1000 min bekeken + $5/1000 min opgeslagen | Premium-gevoel, geen YouTube-branding, on-brand |
| **YouTube (unlisted)** | gratis | MVP / gratis-tier, maar "gratis-gevoel" + suggesties van anderen |
| **Loom** | gratis tot 25 video's | Snelst voor screen+cam, maar Loom-branding |
| **Vimeo Pro** | ~€20/mnd | Tussenweg, schoon, geen ads |

Aanbeveling: start op **Loom** (snelst om te beginnen), migreer naar **Cloudflare
Stream** zodra je betalende klanten hebt (premium-perceptie rechtvaardigt €99+).

## Hoe een script lezen

Elk script heeft deze secties:

- **🎯 HOOK** (eerste 30s) — waarom moet de kijker dít blijven kijken
- **📋 LEERDOELEN** — wat kun je na de video
- **🎬 BEATS** — genummerde segmenten met:
  - *Zeg:* de kern-talking-points (improviseer de exacte woorden)
  - *Toon:* wat er op het scherm gebeurt (welke module-sectie, welk codebestand)
  - *⚠ Noem:* een veelgemaakte fout om te benoemen
- **🔁 RECAP + CTA** — samenvatting + verwijzing naar volgende module/oefening

## Algemene presenteer-regels

1. **Hook binnen 15 seconden.** Geen "hoi, welkom, vandaag gaan we het hebben
   over…". Open met de pijn of de payoff.
2. **Toon, vertel niet.** Bij elk concept: schakel naar scherm + companion-code.
   Praten over code zonder code tonen = de helft van de waarde weg.
3. **Eén idee per beat.** Als je merkt dat een beat 8+ minuten wordt: splits 'm.
4. **Fouten zijn content.** Laat een tikfout staan en fix 'm live — dat is exact
   wat kijkers herkennen en waarderen.
5. **Energie > perfectie.** Eén take met enthousiasme verslaat vijf perfecte maar
   vlakke takes.

Zie `00-recording-setup.md` voor gear, OBS-settings, captions en editing-flow.
