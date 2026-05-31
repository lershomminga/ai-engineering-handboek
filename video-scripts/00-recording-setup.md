# Opname-setup

Eenmalige setup (~1-2u), daarna kun je in één avond meerdere modules opnemen.

## Gear (minimaal → beter)

| | Minimaal (gratis-€100) | Beter (€100-400) |
|---|---|---|
| **Mic** | Telefoon-earbuds mic of laptop-mic in stille kamer | Rode Wireless GO II of een USB-mic (Shure MV7) |
| **Camera** | Telefoon op een boekenstapel/statief | Webcam 1080p (Logitech Brio) of telefoon als webcam |
| **Licht** | Raam vóór je (niet achter!) | Eén softbox of ring-light |
| **Scherm** | Wat je hebt | Tweede monitor voor je script |

De mic is verreweg het belangrijkst. Slechte beeld vergeven kijkers; slechte
audio klikken ze weg.

## Software

- **Opnemen:** [OBS Studio](https://obsproject.com/) (gratis, alle platforms) of
  Camtasia (betaald, makkelijker editen). Voor screen+cam tegelijk: Loom (snelst).
- **Editen:** DaVinci Resolve (gratis, krachtig) of CapCut (gratis, simpel).
- **Captions:** Whisper (lokaal, gratis) of de auto-captions van je editor.
  Captions zijn niet optioneel — veel kijkers kijken zonder geluid.

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

```
┌─────────────────────────────────────────┐
│                                          │
│   SCHERM (handboek + companion-code)     │  ← 85% van het beeld
│                                          │
│                              ┌────────┐  │
│                              │  CAM   │  │  ← gezicht in hoek, ~15%
│                              └────────┘  │
└─────────────────────────────────────────┘
```

Gezicht hoeft niet groot — maar wél aanwezig. Een gezicht in de hoek verdubbelt
de "vertrouwen"-perceptie t.o.v. pure screencast.

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
