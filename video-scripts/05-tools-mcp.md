# 05 — Tools & MCP · richtduur 25-35 min

Veel live coding. De "ik bouw een MCP-server in 50 regels en connect 'm" is je
demo-moment.

## 🎯 HOOK (0:00-0:30)
> *Zeg:* "Een LLM die alleen praat is een speeltje. Een LLM die tools gebruikt is
> een medewerker. Ik laat je zien hoe function-calling werkt, en daarna bouwen we
> een echte MCP-server die je aan Claude koppelt — live, in een paar minuten."
>
> *Toon:* de ToolsMCP-module.

## 📋 LEERDOELEN
Function-calling-loop, de drie MCP-primitives, een eigen MCP-server bouwen +
connecten, en de Tool Search Tool voor grote tool-sets.

## 🎬 BEATS

**Beat 1 — Function calling van binnen (0:30-8:00)**
- *Zeg:* de loop: model vraagt tool → jij voert uit → resultaat terug → herhaal
  tot end_turn.
- *Toon:* companion-code `04-tools-mcp/01_function_calling.py` — run live met 3
  tools (weather, calculator, search). Laat de iteratie-logs zien: je ziet Claude
  meerdere tools achter elkaar aanroepen.
- *⚠ Noem:* "Silent failures zijn de #1 productie-bug: een tool returnt null en de
  agent merkt het niet. Geef altijd gestructureerde errors terug."

**Beat 2 — Wat is MCP (8:00-11:00)**
- *Zeg:* Model Context Protocol — open standaard, 9.652+ servers. Drie primitives:
  tools (acties), resources (data), prompts (templates).
- *Toon:* de MCP-intro + de 3-primitives-sectie + Schema #08 (MCP architecture).

**Beat 3 — BOUW EEN MCP-SERVER LIVE (11:00-22:00)** ← demo-moment
- *Zeg + Toon:* open `04-tools-mcp/02_minimal_mcp_server.py`. Loop door FastMCP:
  `@mcp.tool()` decorators, een resource. Run 'm op stdio.
- *Toon:* dan `03_mcp_client.py` in een tweede terminal — list_tools, call_tool,
  read_resource. Je ziet de twee processen praten.
- *Bonus:* als je Claude Desktop hebt, toon hoe je de server in
  `claude_desktop_config.json` zet en 'm in een echt gesprek gebruikt.

**Beat 4 — Transport: stdio vs Streamable HTTP (22:00-25:00)**
- *Zeg:* "SSE is dood sinds maart 2026. Lokaal = stdio (snelst). Remote =
  Streamable HTTP."
- *Toon:* de transport-sectie + de migration-snippet.

**Beat 5 — Tool Search Tool (25:00-29:00)**
- *Zeg:* "Heb je 50+ tools? Schemas vreten context. Tool Search laadt ze on-demand."
- *Toon:* de Tool Search-sectie met de Anthropic-benchmark-cijfers.

**Beat 6 — Security (29:00-32:00)**
- *Zeg:* OWASP MCP Top-10, CVE-2025-6514, vetting van 3rd-party servers.
- *Toon:* de security-checklist.

## 🔁 RECAP + CTA (32:00-33:00)
> *Zeg:* "Je hebt nu tools. Volgende: agents — we zetten die tools in een loop en
> debuggen 'm live."
