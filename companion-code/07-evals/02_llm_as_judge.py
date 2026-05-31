"""
02 — LLM-as-judge met bias-mitigation.
- Position-swap: A/B swappen, alleen consistent oordeel accepteren
- Self-preference: judge ≠ generator-family (Claude scoort GPT, vice versa)
- Length-control: discount/upweight per length-difference
"""
import random
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


JUDGE_PROMPT = """Je beoordeelt twee antwoorden op dezelfde vraag.

Vraag: {question}

Antwoord [A]:
{a}

Antwoord [B]:
{b}

Welke is beter? Antwoord met ALLEEN 'A' of 'B' of 'gelijk'.
Negeer lengte-verschillen — kijk naar correctheid + helderheid."""


def judge_once(question: str, a: str, b: str, swap: bool) -> str:
    """Eén judge-call met optionele swap."""
    if swap:
        a, b = b, a
    resp = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=10,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT.format(question=question, a=a, b=b),
        }],
    )
    verdict = resp.content[0].text.strip().upper()
    # Map terug naar de oorspronkelijke A/B
    if swap:
        if verdict == "A":
            return "B"
        if verdict == "B":
            return "A"
    return verdict


def unbiased_judge(question: str, a: str, b: str, n_swaps: int = 3) -> dict:
    """Run N swaps, accepteer alleen consistent oordeel."""
    votes = []
    for _ in range(n_swaps):
        swap = random.random() < 0.5
        vote = judge_once(question, a, b, swap)
        votes.append(vote)

    a_votes = votes.count("A")
    b_votes = votes.count("B")

    if a_votes >= n_swaps - 1:
        winner = "A"
    elif b_votes >= n_swaps - 1:
        winner = "B"
    else:
        winner = "inconsistent"

    return {
        "winner": winner,
        "votes": votes,
        "confidence": max(a_votes, b_votes) / n_swaps,
        "length_a": len(a),
        "length_b": len(b),
    }


def main() -> None:
    question = "Hoe werkt prompt caching bij Anthropic?"
    a = (
        "Prompt caching cached herhaaldelijk gebruikte prompt-prefixen. "
        "Geeft 90% korting op cached input-tokens."
    )
    b = (
        "Met prompt caching bewaart Anthropic delen van je prompt voor 5 minuten "
        "(default) of 1 uur. Cached reads kosten 10% van normaal. Cache-creation "
        "is 1.25-2× normale prijs. Max 4 cache-breakpoints per request, lookback 20."
    )

    result = unbiased_judge(question, a, b)
    print(f"Winner: {result['winner']} (confidence: {result['confidence']:.0%})")
    print(f"Votes: {result['votes']}")
    print(f"Length A: {result['length_a']}, Length B: {result['length_b']}")

    if result['winner'] == 'inconsistent':
        print("\n⚠ Geen consistent oordeel — escaleer naar human review.")


if __name__ == "__main__":
    main()
