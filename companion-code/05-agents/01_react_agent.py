"""
01 — ReAct agent: Reason → Act → Observe → loop.
Met 3 tools en max_iterations + budget_usd cap.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

TOOLS = [
    {"name": "search", "description": "Web-search met query",
     "input_schema": {"type": "object", "properties": {"q": {"type": "string"}}, "required": ["q"]}},
    {"name": "calculator", "description": "Eval math expressie",
     "input_schema": {"type": "object", "properties": {"expr": {"type": "string"}}, "required": ["expr"]}},
    {"name": "get_weather", "description": "Weer per stad",
     "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}},
]

# Mock tool-implementaties
def run_tool(name: str, inp: dict) -> str:
    if name == "search":
        return f"Mock-search results for '{inp['q']}': lorem ipsum..."
    if name == "calculator":
        try:
            return str(eval(inp["expr"]))
        except Exception as e:
            return f"Error: {e}"
    if name == "get_weather":
        return f"In {inp['city']}: 18°C bewolkt"
    return "Unknown tool"


def react_loop(task: str, max_iter: int = 10, max_budget_usd: float = 0.50) -> str:
    msgs = [{"role": "user", "content": task}]
    spent = 0.0
    PRICES = {"input": 3.0 / 1e6, "output": 15.0 / 1e6}  # Sonnet 4.6

    for i in range(max_iter):
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=TOOLS,
            messages=msgs,
        )
        spent += resp.usage.input_tokens * PRICES["input"]
        spent += resp.usage.output_tokens * PRICES["output"]

        if spent > max_budget_usd:
            return f"⚠ Budget {max_budget_usd} bereikt na {i + 1} iteraties"

        msgs.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason == "end_turn":
            print(f"[done after {i + 1} iter, ${spent:.4f}]")
            return resp.content[-1].text

        # Voer alle tools uit
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                out = run_tool(block.name, block.input)
                print(f"  [iter {i + 1}] {block.name}({block.input}) → {out}")
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": out,
                })
        msgs.append({"role": "user", "content": results})

    return f"Max {max_iter} iterations exceeded"


if __name__ == "__main__":
    print(react_loop("Wat is 23 × 47, en het weer in Amsterdam vandaag?"))
