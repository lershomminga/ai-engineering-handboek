"""
03 — Adaptive Thinking met verschillende effort-niveaus.
Vergelijkt latency + accuracy per niveau op een complex puzzle.
"""
import time
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


PUZZLE = """Een boer moet een wolf, een geit en een kool oversteken van linker- naar
rechteroever. In de boot past de boer + 1 ding. Als hij weg is mag de wolf
niet bij de geit, en de geit niet bij de kool. Geef de exacte volgorde van
overzettingen. Format: 'X →' of '← Y'."""


def run_with_effort(effort: str) -> dict:
    """effort: low | medium | high | xhigh | max"""
    t = time.time()
    resp = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        effort=effort,
        messages=[{"role": "user", "content": PUZZLE}],
    )
    duration = time.time() - t
    return {
        "effort": effort,
        "duration_s": round(duration, 1),
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
        "answer": resp.content[-1].text[:200],  # eerst content is thinking, laatst is text
    }


def main() -> None:
    print(f"{'Effort':<10}{'Time':<10}{'In tok':<10}{'Out tok':<10}Answer (truncated)")
    print("-" * 80)
    for effort in ["low", "medium", "high"]:
        result = run_with_effort(effort)
        print(
            f"{result['effort']:<10}"
            f"{result['duration_s']!s:<10}"
            f"{result['input_tokens']:<10}"
            f"{result['output_tokens']:<10}"
            f"{result['answer'][:60]}..."
        )

    print("\nObservaties:")
    print("- effort=low: snel, bij simpele puzzles vaak voldoende")
    print("- effort=high: langzaam (10-30s) maar consistentere multi-step reasoning")
    print("- Cost: thinking-tokens tellen mee in output → meet je $-impact")


if __name__ == "__main__":
    main()
