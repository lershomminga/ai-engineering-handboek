# Opname-setup

Eenmalige setup (~1-2u), daarna kun je in één avond meerdere modules opnemen.

## Faceless-first (aanbevolen start)

Begin **zonder camera** — alleen scherm + stem. Dat haalt alle camera-, licht- en
"hoe zie ik eruit"-frictie weg. Je houdt één variabele over: audio. Faceless is een
bewezen format voor technische walkthroughs (veel top dev-kanalen begonnen zo).

**Je gezicht later toevoegen** kan op twee manieren — beide vereisen géén
her-opname van de kern:

1. **Bookend (makkelijkst):** neem later losse talking-head intro's/outro's op en
   plak ze vóór/na de bestaande screencast in de editor. De kern blijft intact.
2. **Cam-bubbel:** neem een aparte gezicht-track op en leg die als hoekje over de
   screencast (meer edit-werk).

Om dit later soepel te maken — doe nu drie dingen:
- **Bewaar de ruwe opnames** in volle resolutie (niet weggooien na upload).
- **Spreek in segmenten** met natuurlijke pauzes tussen beats → makkelijker om
  later een intro ertussen te knippen.
- **Geen "kijk-naar-mij"-taal** in de voiceover → de faceless-versie blijft tijdloos.

## Gear

Faceless = camera en licht zijn **optioneel**. De mic is alles.

| | Faceless-start (gratis-€150) | Later + gezicht (€100-400) |
|---|---|---|
| **Mic** ⭐ | USB-mic in stille kamer (Fifine/Samson ~€40) of earbuds-mic | Shure MV7 of Rode Wireless GO II |
| **Camera** | — niet nodig | Webcam 1080p (Logitech Brio) of telefoon als webcam |
| **Licht** | — niet nodig | Eén softbox of ring-light, raam vóór je |
| **Scherm** | Wat je hebt | Tweede monitor voor je script |

Bij faceless vergeven kijkers letterlijk geen beeld — er ís geen beeld behalve je
scherm. Dus: **stille kamer + een fatsoenlijke mic = 90% van je productiewaarde.**

## Software

Bij faceless kantelt de keuze richting OBS: Loom's grote voordeel was makkelijk
scherm-**plus**-camera-bubbel samenvoegen. Doe je alleen scherm + stem? Dan is OBS
net zo makkelijk én gratis.

- **Opnemen:** [OBS Studio](https://obsproject.com/) (gratis, alle platforms) —
  aanbevolen voor faceless. Alternatief: Loom Business+AI ($24/mnd, 1 maand,
  opzeggen) als je de auto-filler-word/stilte-verwijdering wilt om edit-tijd te
  besparen.
- **Editen:** DaVinci Resolve (gratis, krachtig) of CapCut (gratis, simpel).
- **Captions:** Whisper (lokaal, gratis) of de auto-captions van je editor.
  Captions zijn niet optioneel — veel kijkers kijken zonder geluid.

### Faceless-tooling samengevat

| Wil je… | Kies |
|---|---|
| €0, volledige controle, geduld | **OBS + DaVinci Resolve** ⭐ voor faceless |
| Snelste clean output, AI ruimt "uhh"s op | Loom Business+AI, 1 maand, download MP4's, opzeggen ($24) |

### OBS-settings (kopieer dit)

```
Output → Recording:
  Format: MP4
  Encoder: hardware (NVENC/QuickSync) als beschikbaar, anders x264
  Bitrate: 8000-12000 Kbps (1080p)
Video:
  Base + Output resolution: 1920×1080
  FPS: 30 (60 alleen als je veel scroll/animatie toont)
Audio:
  Sample rate: 48 kHz
  Mic: -filters → Noise Suppression (RNNoise) + Compressor
```

### Scene-layout

**Faceless (nu):** volledig scherm, geen cam-source. Eén scene in OBS: je
display-capture. Klaar.

```
┌─────────────────────────────────────────┐
│                                          │
│   SCHERM (handboek + companion-code)     │  ← 100% van het beeld
│                                          │
│                                          │
└─────────────────────────────────────────┘
```

**Later + gezicht:** voeg een cam-bubbel in de hoek toe (~15% van het beeld).
Een gezicht in de hoek verhoogt de "vertrouwen"-perceptie t.o.v. pure screencast —
maar is niet nodig om te beginnen.

```
┌─────────────────────────────────────────┐
│   SCHERM                                 │
│                              ┌────────┐  │
│                              │  CAM   │  │  ← optioneel, later
│                              └────────┘  │
└─────────────────────────────────────────┘
```

## Voorbereiding per opname (5 min)

1. **Sluit alles** — Slack, mail, notificaties (macOS: Focus, Windows: Focus Assist).
2. **Browser schoon** — incognito-venster met alleen het handboek + één tab met de
   companion-code. Geen bookmarks-balk met persoonlijke links.
3. **Terminal klaar** — companion-code-folder al `cd`'d, venv geactiveerd,
   `.env` ingevuld (toon 'm NIET in beeld — gebruik een dummy-key in opnames).
4. **Lettergrootte omhoog** — editor + terminal op ~18-20pt. Kijkers op mobiel.
5. **Script op tweede scherm** of geprint naast je.

## Editing-flow (per video ~1-2u)

1. Knip de eerste 3s en laatste "uhh klaar" eraf.
2. Verwijder lange stiltes (>2s) en grote "uhm"s — Resolve/CapCut hebben
   auto-silence-cut.
3. Voeg captions toe (Whisper → .srt → import).
4. Intro-kaart: 3s met module-titel + nummer (matcht de oranje accent-kleur #EA580C).
5. Export 1080p MP4, upload naar je host, plak de URL in `src/App.jsx`.

## Pacing-target

~130-150 woorden per minuut spreken. Sneller = kijkers haken af; trager = saai.
Een 20-min video = ~2.800 woorden gesproken. De beat-sheets zijn korter dan dat —
jij vult de rest met live demonstreren.

## Batch-strategie

Neem **2 modules per opname-sessie** op (warm-up + de echte). Vijf sessies = klaar.
Edit in een aparte batch (anders perfectioneer je tijdens opnemen en kost het 3×
zo lang). Eerst alles opnemen, dán alles editen.
