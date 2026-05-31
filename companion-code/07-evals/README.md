# 07 — Evals

Code-based, LLM-as-judge, en CI-gating met Promptfoo.

## Bestanden

| # | Bestand | Wat |
|---|---|---|
| 01 | `01_basic_eval.py` | Code-based: regex/match-based assertions tegen golden set |
| 02 | `02_llm_as_judge.py` | LLM-as-judge met bias-mitigation (position-swap, length-control) |
| 03 | `promptfoo.yaml` | CI-config voor Promptfoo + GitHub Action |
| — | `golden_set.jsonl` | 10 testcases met expected outputs |

## Run

```bash
pip install -r requirements.txt
python 01_basic_eval.py

# Voor CI:
npm install -g promptfoo
promptfoo eval --config promptfoo.yaml
```
