# 01 — Fundamentals

Eerste calls naar Claude. Tokens tellen. Streaming.

## Scripts

| # | Bestand | Wat doet het |
|---|---|---|
| 01 | `01_first_call.py` | Minimale Claude-call, response printen |
| 02 | `02_streaming.py` | Streaming tokens, TTFT meten |
| 03 | `03_token_counting.py` | Vooraf tokens tellen, NL vs EN vergelijken |

## Setup

```bash
pip install -r requirements.txt
cp ../.env.example .env
# Vul ANTHROPIC_API_KEY in
python 01_first_call.py
```

Verwachte kosten: <$0.01 voor alle drie samen.
