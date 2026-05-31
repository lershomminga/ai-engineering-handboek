# 09 — Cost Optimization (routing + caching)

## Scripts

| # | Bestand | Wat |
|---|---|---|
| 01 | `01_haiku_router.py` | Haiku classifier routeert SIMPLE/MEDIUM/COMPLEX |
| 02 | `02_litellm_proxy.yaml` | LiteLLM productie-config met fallback + budget |
| 03 | `03_semantic_cache.py` | Embedding-based cache met similarity-threshold |

## Run

```bash
pip install -r requirements.txt
python 01_haiku_router.py
```

Verwachte besparing op gemixt traffic: 60-85%.
