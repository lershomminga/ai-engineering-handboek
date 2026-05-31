"""
02 — Native structured outputs via output_config.format (GA Q1 2026).
Werkt op Claude 4.5/4.6/4.7/4.8. SDK transformeert ongeldige
JSON-Schema constraints automatisch naar runtime-equivalent.
"""
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

SCHEMA = {
    "type": "object",
    "properties": {
        "sentiment": {"type": "string", "enum": ["positief", "negatief", "neutraal"]},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "intensity": {"type": "integer", "minimum": 1, "maximum": 5},
        "topics": {"type": "array", "items": {"type": "string"}},
        "refusal": {"type": ["string", "null"]},
    },
    "required": ["sentiment", "confidence", "intensity", "topics", "refusal"],
}


def analyze(review: str) -> dict:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        output_config={
            "format": {"type": "json_schema", "schema": SCHEMA}
        },
        messages=[{"role": "user", "content": f"Analyseer deze review: {review}"}],
    )
    # resp.content[0].text is gegarandeerd schema-valide JSON
    return json.loads(resp.content[0].text)


def main() -> None:
    review = "Snelle levering, prima kwaliteit, 5 sterren waard!"
    print(f"Review: {review}")
    print(f"Result: {analyze(review)}")
    print("\nVoordeel boven tool-use-pattern:")
    print("- Geen 'extract_*' fake-tool naam meer nodig")
    print("- Cleaner API-call")
    print("- Maar: citations + structured outputs sluiten elkaar uit")
    print("  → gebruik tool-use als je beide tegelijk wilt")


if __name__ == "__main__":
    main()
