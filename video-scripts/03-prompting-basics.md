# 03 — Prompting Basics · richtduur 15-25 min

De eerste écht waardevolle walkthrough. De v0→v4 live-iteratie is je sterkste beat
van de hele serie — daar zit de "aha".

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Ik ga één prompt nemen die op 38% accuraat zit, en hem live verbeteren
> naar 96% — in vier stappen. Geen magie, gewoon vier dingen die je elke keer
> toevoegt. Aan het eind weet je precies hoe je elke vage prompt aanscherpt."
>
> *Toon:* de PromptingBasics-module, scroll naar "Anatomie van een goede prompt: v0→v4".

## 📋 LEERDOELEN
De vijf basisprincipes, het POWER-framework, en — belangrijkst — het iteratie-
proces v0→v4 live ervaren.

## 🎬 BEATS

**Beat 1 — Waarom prompting de grootste hefboom is (0:30-2:00)**
- *Zeg:* "Voordat je RAG of fine-tuning aanraakt: 80% van je kwaliteit komt uit
  prompting. Het is de goedkoopste, snelste knop."
- *Toon:* de intro + de vijf basisprincipes.

**Beat 2 — POWER-framework (2:00-4:00)**
- *Zeg:* Persona, Output, Workflow, Examples, Restrictions — wat elk doet.
- *Toon:* de POWER-sectie.

**Beat 3 — DE LIVE-ITERATIE v0→v4 (4:00-14:00)** ← kern van de video
- *Zeg + Toon:* open een API-playground of de companion-code
  `02-prompting-advanced/01_xml_tags.py` als basis. Bouw de support-mail-
  classifier live op:
  - **v0** "vat samen" → run → laat de inconsistente output zien (38%)
  - **v1** + rol → run → "tone consistenter, lengte nog wisselend"
  - **v2** + format-constraint → run → "format compliant, urgentie nog fout"
  - **v3** + few-shot → run → "urgentie scherper door contrast tussen examples"
  - **v4** + restrictions/refusal → run → "96%, edge-cases afgevangen"
- *⚠ Noem:* bij elke stap expliciet: "Wat ging er stuk in de vorige versie?"
  Dat is de didactische kern — niet de eind-prompt, maar het *waarom* van elke stap.
- *Toon:* parallel het v0→v4-blok in de module zodat kijker het kan teruglezen.

**Beat 4 — Anti-patterns fix-zij-aan-zij (14:00-17:00)**
- *Zeg:* loop 4-5 anti-patterns langs. "'Schrijf niet saai' → het model weet niet
  wat saai is. Zeg wat je wél wilt: concrete metaforen, actieve werkwoorden."
- *Toon:* de anti-patterns-gallery.

**Beat 5 — Versioning (17:00-19:00)**
- *Zeg:* "Behandel prompts als code. Folder + semver + CHANGELOG."
- *Toon:* de versioning-sectie + folderstructuur.

## 🔁 RECAP + CTA (19:00-20:00)
> *Zeg:* "Pak vandaag een prompt uit je eigen werk en doe de v0→v4-oefening. Er
> staat een oefening onderaan de module. Volgende video: advanced — XML,
> chain-of-thought en wanneer extended thinking de moeite waard is."
> *Toon:* de oefening + de quiz-knop.
