"""
02 — Minimale MCP server met FastMCP.
Stelt 2 tools + 1 resource beschikbaar via stdio transport.
Run: python 02_minimal_mcp_server.py
Test met Claude Desktop (configureer in claude_desktop_config.json) of via
script 03_mcp_client.py.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("handbook-demo")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Tel twee getallen op."""
    return a + b


@mcp.tool()
def get_note(note_id: str) -> dict:
    """Haal een note op uit de mock-database."""
    notes = {
        "1": {"title": "Eerste idee", "body": "Build een MCP server"},
        "2": {"title": "Tweede idee", "body": "Schrijf erover in het handboek"},
    }
    return notes.get(note_id, {"error": "not_found"})


@mcp.resource("notes://list")
def list_notes() -> str:
    """Lijst van alle beschikbare note-IDs."""
    return "Available notes: 1, 2"


if __name__ == "__main__":
    # Default transport = stdio (voor Claude Desktop)
    mcp.run()
