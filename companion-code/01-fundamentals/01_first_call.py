"""
01 — Minimale Claude-call.
Output: tekst-antwoord + usage-stats.
"""
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()  # Leest ANTHROPIC_API_KEY uit env


def main() -> None:
    resp = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        messages=[
            {"role": "user", "content": "Leg in 2 zinnen uit wat een token is."}
        ],
    )

    print("=== Antwoord ===")
    print(resp.content[0].text)
    print("\n=== Usage ===")
    print(f"Input tokens:  {resp.usage.input_tokens}")
    print(f"Output tokens: {resp.usage.output_tokens}")
    # Cost estimate (haiku-4-5: $1/1M in, $5/1M out)
    cost = (
        resp.usage.input_tokens * 1.00 / 1_000_000
        + resp.usage.output_tokens * 5.00 / 1_000_000
    )
    print(f"Cost (USD):    ${cost:.6f}")


if __name__ == "__main__":
    main()
