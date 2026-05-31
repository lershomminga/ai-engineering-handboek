# 10 — Capstone: Customer Support Agent · richtduur 30-45 min

De finale. Brengt alle eerdere video's samen. Dit is óók je sterkste verkoop-
argument: "dit ga je kunnen bouwen."

## 🎯 HOOK (0:00-0:40)
> *Zeg:* "Alles wat we in deze serie hebben gezien — prompting, structured output,
> RAG, agents, evals, security — komt hier samen in één project: een customer-
> support-agent die je écht in productie kunt zetten. Ik loop de architectuur door,
> de rubric waarmee je jezelf scoort, en hoe je begint met de starter-skeleton."
>
> *Toon:* de Capstone-README in `companion-code/10-capstone-support-agent/`.

## 📋 LEERDOELEN
De volledige data-flow snappen, weten hoe de modules samenkomen, en met de
starter-skeleton kunnen beginnen.

## 🎬 BEATS

**Beat 1 — Wat bouwen we (0:40-4:00)**
- *Zeg:* een agent die tickets ontvangt, classificeert, bij FAQ direct via RAG
  antwoordt, bij escalatie een draft schrijft voor human review, alles gelogd +
  cost-tracked.
- *Toon:* de README "Wat ga je bouwen?" + de modules-die-je-raakt-tabel.

**Beat 2 — De architectuur (4:00-12:00)** ← kern
- *Zeg + Toon:* open `ARCHITECTURE.md`. Loop de data-flow langs van boven naar
  beneden: Guardrails → Classify → Route → RAG → Generate → Action gate →
  Observability. Koppel elke laag terug aan de video waarin je 'm behandelde:
  "De RAG-laag — dat is video 7. De classify met structured output — video 3 en
  het structured-outputs-stuk."
- *Toon:* het ASCII-data-flow-diagram in ARCHITECTURE.md.

**Beat 3 — De rubric (12:00-18:00)**
- *Zeg:* "Hoe weet je dat je klaar bent? 10 criteria, 23 punten. Senior = 18+,
  productie-ready = 21+."
- *Toon:* de rubric-tabel. Loop de criteria langs, leg per criterium uit wat de
  pass-bar betekent (bijv. "RAG-quality ≥ 0.85 RAGAS faithfulness — dat meet je
  zoals in video 8").

**Beat 4 — De starter-skeleton (18:00-28:00)**
- *Zeg:* "Je begint niet met een leeg scherm. De skeleton heeft 12 genummerde
  TODO's in volgorde."
- *Toon:* `starter/app/main.py` — loop de TODO's langs. Toon de webhook-ingress,
  de `process_ticket`-pipeline met de TODO-markers. Open `starter/evals/cases.jsonl`
  — de 30 test-tickets (FAQ, escalate, spam, PII, injection).
- *⚠ Noem:* "Begin bij TODO 1 en werk in volgorde. Elke TODO bouwt op de vorige.
  Run de eval-suite na elke paar TODO's om te zien of je nog op koers zit."

**Beat 5 — Failure-modes (28:00-33:00)**
- *Zeg:* "Wat test de eval-suite? Niet alleen happy-path." Loop de failure-modes
  langs: PII-in-ticket, prompt-injection, hallucinated FAQ, provider-overload.
- *Toon:* de failure-modes-sectie in ARCHITECTURE.md.

**Beat 6 — Afsluiting van de serie (33:00-37:00)**
- *Zeg:* "Als je dit afbouwt heb je een portfolio-stuk dat in elk AI-engineer-
  sollicitatiegesprek indruk maakt. Deel het op GitHub, schrijf een blogpost over
  wat je leerde. Dat opent meer deuren dan welk certificaat dan ook."
- *Toon:* terug naar de Roadmap-portfolio-sectie + de interview-prep-rubric.

## 🔁 RECAP + CTA (37:00-38:30)
> *Zeg:* "Dat was de serie. Je hebt nu het volledige pad: van token tot productie-
> agent. Bouw de capstone, deel 'm, en kom terug naar het handboek als naslagwerk —
> de 220+ termen in het woordenboek en de companion-code staan altijd klaar.
> Succes, champion."
