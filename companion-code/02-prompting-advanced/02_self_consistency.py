"""
02 — Self-consistency: N runs met temp > 0, majority-vote.
Verhoogt accuracy 5-15% op classificatie + wiskunde-taken.
"""
import asyncio
from collections import Counter
from dotenv import load_dotenv
from anthropic import AsyncAnthropic

load_dotenv()
client = AsyncAnthropic()


PROMPT = """Bereken stap-voor-stap, geef alleen het eindantwoord als getal.

Probleem: Een trein vertrekt om 09:15 uit A en rijdt 80 km/u.
Een andere trein vertrekt om 09:45 uit B (120 km verderop, dezelfde route,
tegenovergesteld) met 100 km/u. Op welk tijdstip ontmoeten ze elkaar?

Antwoord met alleen het tijdstip in HH:MM formaat. Geen uitleg."""


async def run_once() -> str:
    resp = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=50,
        temperature=0.7,  # > 0 voor variatie
        messages=[{"role": "user", "content": PROMPT}],
    )
    return resp.content[0].text.strip()


async def main() -> None:
    n_samples = 5
    answers = await asyncio.gather(*[run_once() for _ in range(n_samples)])

    print(f"=== {n_samples} runs (temp=0.7) ===")
    for i, a in enumerate(answers, 1):
        print(f"  Run {i}: {a}")

    # Majority-vote (normaliseer eerst)
    normalized = [a.replace(" ", "").upper() for a in answers]
    counts = Counter(normalized)
    winner, votes = counts.most_common(1)[0]
    print(f"\n=== Majority-vote: {winner} ({votes}/{n_samples}) ===")
    print(f"Confidence: {votes / n_samples:.0%}")

    if votes < n_samples * 0.6:
        print("⚠ Lage consensus — overweeg menselijke review.")


if __name__ == "__main__":
    asyncio.run(main())
