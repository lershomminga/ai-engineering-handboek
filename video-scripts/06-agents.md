# 06 — Agents · richtduur 25-35 min

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Een agent is geen mysterie — het is een while-loop met een LLM erin. Ik
> bouw er live eentje, laat 'm crashen, en debug 'm. Daarna laat ik de twee
> patronen zien die het verschil maken tussen een demo en productie: Plan-and-
> Execute en Reflexion."
>
> *Toon:* de Agents-module + Schema #04 (agent loop).

## 📋 LEERDOELEN
De agent-loop, werkende ReAct-code, Reflexion, Plan-and-Execute, budget-control en
een debugging-toolkit.

## 🎬 BEATS

**Beat 1 — Workflow vs agent (0:30-3:00)**
- *Zeg:* het kernverschil — workflow = jij bepaalt de stappen, agent = LLM beslist
  runtime. "De meeste 'agents' zouden eigenlijk workflows moeten zijn."
- *Toon:* de workflow-vs-agent-sectie.

**Beat 2 — ReAct LIVE (3:00-12:00)** ← demo
- *Zeg + Toon:* `05-agents/01_react_agent.py` — run live. Loop door de Reason-Act-
  Observe-loop, laat de iteratie-logs zien op een multi-tool vraag.
- *⚠ Noem:* wijs op de `max_iter` én de `max_budget_usd` cap. "Zonder budget-cap
  kan een agent in een lus je rekening opblazen. Altijd beide caps."
- *Toon:* trigger bewust een edge-case waar de agent een extra iteratie nodig heeft.

**Beat 3 — Reflexion (12:00-20:00)**
- *Zeg:* Actor → Evaluator → Reflector. "Het agent leert van zijn eigen fouten
  binnen één run." +22% AlfWorld in het paper.
- *Toon:* `05-agents/02_reflexion_loop.py` — run op de naam-bedenk-taak. Laat zien
  hoe trial 2 beter is dan trial 1 dankzij de reflectie.

**Beat 4 — Plan-and-Execute (20:00-27:00)**
- *Zeg:* "Opus plant één keer (duur), Haiku executet elke stap (goedkoop). 3.6×
  sneller, 92% vs 78% completion."
- *Toon:* `05-agents/03_plan_execute.py` — run op de marketing-brief-taak. Laat het
  plan zien, dan de stap-voor-stap executie.

**Beat 5 — Debugging-toolkit (27:00-31:00)**
- *Zeg:* structured logging, traces (Langfuse/Phoenix), replay-harness.
- *Toon:* de debugging-toolkit-sectie + de tool-vergelijkingstabel.
- *⚠ Noem:* deadlock-detectie: hash de laatste 5 tool-calls, abort bij herhaling.

## 🔁 RECAP + CTA (31:00-32:00)
> *Zeg:* "Een agent zonder kennis hallucineert. Volgende video: RAG — we geven 'm
> jouw documenten, van naive search naar een productie-pipeline."
