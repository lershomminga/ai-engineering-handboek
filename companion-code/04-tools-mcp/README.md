# 04 — Tools & MCP

Function calling + minimale MCP server + MCP client.

## Scripts

| # | Bestand | Wat |
|---|---|---|
| 01 | `01_function_calling.py` | Basis function-calling met 3 tools |
| 02 | `02_minimal_mcp_server.py` | FastMCP server met 2 tools + 1 resource |
| 03 | `03_mcp_client.py` | Client die je MCP server aanspreekt |

## Run

```bash
pip install -r requirements.txt

# Test function-calling direct (geen MCP nodig):
python 01_function_calling.py

# Voor MCP:
# Terminal 1:
python 02_minimal_mcp_server.py    # start MCP server op stdio
# Terminal 2:
python 03_mcp_client.py            # connect en gebruik
```
