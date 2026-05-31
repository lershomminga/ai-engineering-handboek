"""
03 — MCP client die via stdio met je server praat.
Demonstreert: list_tools, call_tool, list_resources, read_resource.
"""
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    # Spawn de server als subprocess via stdio
    params = StdioServerParameters(
        command="python",
        args=["02_minimal_mcp_server.py"],
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Lijst tools
            tools = await session.list_tools()
            print("=== Beschikbare tools ===")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Roep een tool aan
            print("\n=== call_tool('add_numbers', a=3, b=5) ===")
            result = await session.call_tool("add_numbers", {"a": 3, "b": 5})
            print(f"Result: {result.content[0].text}")

            # Resource
            print("\n=== read_resource('notes://list') ===")
            resource = await session.read_resource("notes://list")
            print(f"Content: {resource.contents[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
