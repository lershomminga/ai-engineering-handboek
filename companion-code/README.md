# Claude Engineering Handboek — Companion Code

Werkende, paste-and-run referentie-implementaties bij het handboek.
Elke folder hoort bij één of meer modules en bevat:

- **README.md** — wat doet deze code, hoe run je het
- **requirements.txt** of **package.json** — dependencies
- **.env.example** — welke secrets je nodig hebt
- **Genummerde scripts** — van basic → advanced binnen het thema

## Folder-overzicht

| Folder | Module | Inhoud |
|---|---|---|
| `01-fundamentals/` | Fundamenten · API Keys · Tokens | First call, streaming, token counting |
| `02-prompting-advanced/` | Prompting Advanced | XML, self-consistency, extended thinking |
| `03-structured-outputs/` | Structured Outputs | Tool use, native GA, Instructor |
| `04-tools-mcp/` | Tools & MCP | Function calling, MCP server, MCP client |
| `05-agents/` | Agents · Multi-agent | ReAct, Reflexion, Plan-and-Execute |
| `06-rag/` | RAG | Naive → hybrid → contextual → reranked |
| `07-evals/` | Evals | Basic eval, LLM-as-judge, Promptfoo CI |
| `08-backend-fastapi/` | Backend | Streaming + auth + rate-limit + cost-tracking |
| `09-cost-routing/` | Cost Optimization | Haiku-router, LiteLLM proxy, semantic cache |
| `10-capstone-support-agent/` | Capstone | Customer Support Agent — starter + solution |

## Quick start

```bash
# Eénmalig:
cp .env.example .env
# Vul je ANTHROPIC_API_KEY in

# Per folder:
cd 01-fundamentals
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python 01_first_call.py
```

## Globaal `.env.example`

```env
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...           # voor whisper/embeddings in sommige RAG-voorbeelden
VOYAGE_API_KEY=pa-...           # voor embeddings (gratis tier 50M tokens)
COHERE_API_KEY=...              # voor reranker
LANGFUSE_PUBLIC_KEY=pk-...      # voor observability
LANGFUSE_SECRET_KEY=sk-...

# Voor backend / fastapi:
JWT_SECRET=your-jwt-secret-min-32-chars
DATABASE_URL=postgresql://user:pass@localhost:5432/handbook
REDIS_URL=redis://localhost:6379
```

## Conventies

- **Python ≥ 3.11** voor alle scripts
- **TypeScript ≥ 5.4** waar relevant (08, gedeelten van 04)
- Elke script start met env-load (`from dotenv import load_dotenv; load_dotenv()`)
- Geen secrets in code — alleen via env-vars
- Comments in NL waar uitleg nodig, code-identifiers in EN

## Compatibiliteit

Getest tegen:
- Anthropic SDK `0.45+`
- Claude models: `haiku-4-5`, `sonnet-4-6`, `opus-4-7`
- Python 3.11 / 3.12 op macOS, Linux, Windows (WSL2 aanbevolen)
- Node 20+ voor TS-voorbeelden

## Bijdragen

Vond je een bug? Open een issue. Wil je een voorbeeld toevoegen?
Houd je aan de folder-structuur en voeg een README toe per nieuwe map.

## Licentie

MIT — voel je vrij om te gebruiken in je eigen projecten, internal trainings,
of presentaties. Attribution waarderend maar niet verplicht.
