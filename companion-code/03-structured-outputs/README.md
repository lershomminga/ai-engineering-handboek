# 03 — Structured Outputs

Drie patronen voor gegarandeerde JSON-output.

## Scripts

| # | Bestand | Pattern |
|---|---|---|
| 01 | `01_tool_use_pattern.py` | Tool use als schema-enforcement (werkt op alle Claude-versies) |
| 02 | `02_native_ga.py` | `output_config.format` GA-API (Claude 4.x) |
| 03 | `03_instructor_pydantic.py` | Instructor lib met Pydantic + automatic retry |

## Setup

```bash
pip install -r requirements.txt
python 01_tool_use_pattern.py
```
