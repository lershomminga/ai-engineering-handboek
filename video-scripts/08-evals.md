# 08 — Evals · richtduur 20-30 min

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Een prompt die op jouw ene voorbeeld werkt is geen werkende prompt. Een
> prompt die op 50 cases 95% haalt — dat is productie. Wie geen evals heeft,
> opereert blind. Ik laat je live zien hoe je ze opzet, inclusief de bias-valkuilen
> die de meeste teams negeren."
>
> *Toon:* de Evals-module.

## 📋 LEERDOELEN
De drie eval-soorten, golden sets, LLM-as-judge met bias-mitigation, en CI-gating.

## 🎬 BEATS

**Beat 1 — Drie soorten evals (0:30-3:00)**
- *Zeg:* code-based (assertions), model-graded (LLM-as-judge), human.
- *Toon:* de drie-soorten-sectie.

**Beat 2 — Golden set + basic eval LIVE (3:00-10:00)**
- *Zeg:* "Een gold-set is jouw waarheid. 50-200 cases met verwachte outputs."
- *Toon:* `07-evals/golden_set.jsonl` (10 cases), dan `01_basic_eval.py` — run live.
  Laat de per-case ✓/✗ zien + de accuracy + de bootstrap-CI.
- *⚠ Noem:* "50 cases is vaak onder-powered. De sample-size-calculator laat zien:
  voor 3% verschil betrouwbaar detecteren heb je ~1000 cases nodig."

**Beat 3 — LLM-as-judge + bias LIVE (10:00-18:00)**
- *Zeg:* "Judges hebben bias. Position-bias: A vs B, de volgorde beïnvloedt het
  oordeel. Empirisch bewezen."
- *Toon:* `02_llm_as_judge.py` — run live. Laat de position-swap zien: 3 runs met
  geshuffelde volgorde, alleen consistent oordeel telt.
- *⚠ Noem:* self-preference bias — "laat Claude geen Claude-output beoordelen
  zonder ensemble. En length-bias: judges geven langere antwoorden vaak hogere
  scores zonder reden."

**Beat 4 — CI-gating (18:00-24:00)**
- *Zeg:* "Prompts als code betekent: regression-test bij elke PR."
- *Toon:* `07-evals/promptfoo.yaml` + de GitHub Actions YAML in de module. Leg de
  threshold-gate uit (>= 0.85, geen regressie vs main).

**Beat 5 — RAGAS voor RAG (24:00-27:00)**
- *Zeg:* faithfulness, answer relevance, context precision/recall — kort.
- *Toon:* de RAGAS-sectie. "Sluit aan op de RAG-video: zo meet je die pipeline."

## 🔁 RECAP + CTA (27:00-28:00)
> *Zeg:* "Volgende video — de leukste: Computer Use. Claude die letterlijk je
> scherm bestuurt."
