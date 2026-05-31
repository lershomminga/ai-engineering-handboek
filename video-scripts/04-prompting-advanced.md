# 04 — Prompting Advanced · richtduur 20-30 min

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Chain-of-thought, extended thinking, self-consistency — iedereen noemt
> ze, bijna niemand weet wanneer je ze écht moet inzetten of wat ze kosten. Ik
> laat het live zien, met de cijfers erbij, zodat je niet blind tokens verbrandt."
>
> *Toon:* de PromptingAdvanced-module.

## 📋 LEERDOELEN
XML-structurering, CoT vs adaptive thinking (met cost/latency-afweging),
self-consistency, en de prompt-improver.

## 🎬 BEATS

**Beat 1 — XML-tags (0:30-4:00)**
- *Zeg:* "Claude is getraind met XML-tags. Het scheidt instructies van data en
  verlaagt prompt-injection-risico."
- *Toon:* companion-code `02-prompting-advanced/01_xml_tags.py` — run 'm live,
  laat de gestructureerde classifier-output zien op 3-4 inputs incl. een edge-case.

**Beat 2 — Chain-of-thought (4:00-7:00)**
- *Zeg:* wanneer CoT helpt (multi-step reasoning) en wanneer niet (simpele lookup
  → ruis). Op moderne modellen is de winst soms ~0 — laat dat zien.
- *Toon:* de CoT-sectie + de cost/quality-matrix.

**Beat 3 — Self-consistency LIVE (7:00-13:00)**
- *Zeg:* "Vijf runs met temperature 0.7, dan majority-vote. 5-15% accuracy-winst
  op classificatie en wiskunde."
- *Toon:* companion-code `02-prompting-advanced/02_self_consistency.py` — run 'm,
  laat de 5 verschillende antwoorden zien + de vote + de confidence.
- *⚠ Noem:* "Doe dit NIET bij yes/no-vragen — daar wint plain majority niks. En
  het is 5× de kosten, dus alleen voor taken waar accuracy telt."

**Beat 4 — Extended / Adaptive Thinking (13:00-19:00)**
- *Zeg:* effort-levels (low→max), wat ze kosten in tokens + latency.
- *Toon:* companion-code `02-prompting-advanced/03_extended_thinking.py` — run met
  low/medium/high op dezelfde puzzle, laat de latency- en token-verschillen zien.
- *⚠ Noem:* "max is zelden de juiste keuze — thinking-tokens tellen mee in je
  output-budget én -kosten. Begin laag, verhoog tot het nét genoeg is."

**Beat 5 — Prompt-improver tool (19:00-22:00)**
- *Zeg:* Anthropic's eigen tool die XML-standaardiseert, CoT injecteert, examples
  verrijkt. +30% gerapporteerd op multilabel classificatie.
- *Toon:* de prompt-improver-sectie. "Goede first-pass — geen vervanging voor
  eval-gedreven iteratie."

## 🔁 RECAP + CTA (22:00-23:00)
> *Zeg:* "Volgende: Tools & MCP — we bouwen live een MCP-server en connecten 'm
> aan Claude."
