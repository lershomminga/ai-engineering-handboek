"""
01 — Multi-model routing met Haiku als classifier.
Bespaart 60-85% op gemixt traffic vs naive Sonnet-everywhere.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

ROUTER_PROMPT = """Classificeer deze user-vraag:

SIMPLE   = directe lookup, classificatie, korte feiten (<200 output-tokens)
MEDIUM   = reasoning, multi-step, code-generatie (200-2000 output-tokens)
COMPLEX  = multi-file refactor, agent-loop, lange reasoning chains

Antwoord met ALLEEN het label."""

MODEL_MAP = {
    "SIMPLE":  "claude-haiku-4-5",
    "MEDIUM":  "claude-sonnet-4-6",
    "COMPLEX": "claude-opus-4-7",
}

# Pricing per 1M
PRICES = {
    "claude-haiku-4-5":  {"in": 0.80, "out": 4.00},
    "claude-sonnet-4-6": {"in": 3.00, "out": 15.00},
    "claude-opus-4-7":   {"in": 15.00, "out": 75.00},
}


def classify_complexity(user_msg: str) -> str:
    r = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=10,
        system=ROUTER_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    label = r.content[0].text.strip().upper()
    return label if label in MODEL_MAP else "MEDIUM"


def smart_call(user_msg: str, max_tokens: int = 1024) -> dict:
    label = classify_complexity(user_msg)
    model = MODEL_MAP[label]
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": user_msg}],
    )
    cost = (
        resp.usage.input_tokens * PRICES[model]["in"]
        + resp.usage.output_tokens * PRICES[model]["out"]
    ) / 1_000_000
    return {
        "label": label,
        "model": model,
        "answer": resp.content[0].text,
        "cost_usd": cost,
    }


def main() -> None:
    test_messages = [
        ("Wat is 2+2?", "SIMPLE expected"),
        ("Schrijf een Python-functie die fibonacci berekent met memoization.", "MEDIUM"),
        ("Refactor mijn hele Django-codebase om SQLAlchemy te gebruiken in plaats van Django ORM, behoud alle queries en migraties.", "COMPLEX"),
        ("Hi", "SIMPLE"),
    ]
    total_smart = 0.0
    total_naive = 0.0

    for msg, expected in test_messages:
        result = smart_call(msg, max_tokens=300)
        # Vergelijking: naive = altijd Sonnet
        naive_cost = (200 * PRICES["claude-sonnet-4-6"]["in"]
                     + 300 * PRICES["claude-sonnet-4-6"]["out"]) / 1_000_000
        total_smart += result["cost_usd"]
        total_naive += naive_cost

        print(f"\nQ: {msg[:60]}...")
        print(f"  → routed to {result['model']} (cost: ${result['cost_usd']:.6f})")

    print(f"\n=== Totaal voor {len(test_messages)} requests ===")
    print(f"Smart routing: ${total_smart:.6f}")
    print(f"Naive Sonnet:  ${total_naive:.6f}")
    print(f"Besparing:     {(1 - total_smart / total_naive):.0%}")


if __name__ == "__main__":
    main()
