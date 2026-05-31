"""
01 — Function calling met 3 tools: get_weather, calculator, search_wiki.
Toont volledige tool-use loop tot stop_reason == "end_turn".
"""
from dotenv import load_dotenv
from anthropic import Anthropic
import json

load_dotenv()
client = Anthropic()

TOOLS = [
    {
        "name": "get_weather",
        "description": "Geef het huidige weer voor een stad in Nederland",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
    {
        "name": "calculator",
        "description": "Bereken een wiskundige expressie",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
        },
    },
    {
        "name": "search_wiki",
        "description": "Zoek een feit op Wikipedia",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
]


def execute_tool(name: str, args: dict) -> str:
    """Mock tool-implementaties — vervang door echte API-calls."""
    if name == "get_weather":
        return f"In {args['city']}: 18°C, bewolkt, lichte wind"
    if name == "calculator":
        try:
            # SAFETY: in productie, GEEN eval. Gebruik bv. simpleeval.
            return str(eval(args["expression"]))
        except Exception as e:
            return f"Error: {e}"
    if name == "search_wiki":
        return f"Wikipedia: {args['query']} is een Nederlands begrip..."
    return f"Unknown tool: {name}"


def run_agent(user_msg: str, max_iter: int = 10) -> str:
    messages = [{"role": "user", "content": user_msg}]

    for i in range(max_iter):
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason == "end_turn":
            return resp.content[-1].text

        # Verwerk alle tool_use blocks parallel
        tool_results = []
        for block in resp.content:
            if block.type == "tool_use":
                output = execute_tool(block.name, block.input)
                print(f"  [iter {i}] {block.name}({block.input}) → {output}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": tool_results})

    return "Max iterations exceeded"


def main() -> None:
    questions = [
        "Wat is het weer in Amsterdam?",
        "Bereken 234 * 89 + 1234 en zoek wat 'Eemshaven' is.",
        "Bereken (15 + 27) en kijk of het weer in Utrecht regen heeft.",
    ]
    for q in questions:
        print(f"\nQ: {q}")
        print(f"A: {run_agent(q)}")


if __name__ == "__main__":
    main()
