# 02 — Prompting Advanced

XML-prompts, self-consistency voting, extended thinking.

## Scripts

| # | Bestand | Wat doet het |
|---|---|---|
| 01 | `01_xml_tags.py` | XML-gestructureerde prompt met inputs/instructies/voorbeelden |
| 02 | `02_self_consistency.py` | 5 runs met temp=0.7 → majority-vote → accuracy-lift |
| 03 | `03_extended_thinking.py` | Adaptive Thinking met effort-niveaus, latency-vergelijking |

## Setup

```bash
pip install -r requirements.txt
python 01_xml_tags.py
```

Verwachte kosten: ~$0.05 voor alle drie samen.
