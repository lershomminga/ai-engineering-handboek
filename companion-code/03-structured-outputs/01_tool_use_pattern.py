"""
01 — Structured output via tool use.
Werkt op ALLE Claude-versies. Definieer een 'fake' tool waarvan
de input_schema je gewenste output-schema is. Forceer met tool_choice.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

SCHEMA = {
    "type": "object",
    "properties": {
        "sentiment": {
            "type": "string",
            "enum": ["positief", "negatief", "neutraal"],
            "description": "Algemene tone van de review",
        },
        "confidence": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Hoe zeker ben je (0-1)",
        },
        "intensity": {
            "type": "integer",
            "minimum": 1,
            "maximum": 5,
            "description": "Hoe sterk de emotie (1=mild, 5=heftig)",
        },
        "topics": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Onderwerpen die de review aanstipt",
        },
        "refusal": {
            "type": ["string", "null"],
            "description": "Als je het niet kunt bepalen: vul hier waarom in",
        },
    },
    "required": ["sentiment", "confidence", "intensity", "topics", "refusal"],
}


def analyze(review: str) -> dict:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        tools=[
            {
                "name": "extract_review_sentiment",
                "description": "Extraheer sentiment van een review",
                "input_schema": SCHEMA,
            }
        ],
        tool_choice={"type": "tool", "name": "extract_review_sentiment"},
        messages=[{"role": "user", "content": review}],
    )
    # tool_use block heeft de gevalideerde input
    for block in resp.content:
        if block.type == "tool_use":
            return block.input
    return {"error": "no tool_use block"}


def main() -> None:
    reviews = [
        "Snelle levering, prima kwaliteit, 5 sterren waard!",
        "Pakket was beschadigd en customer service reageert niet.",
        "Het is gewoon ok. Werkt zoals beloofd.",
        "asdf qwerty zxcv",  # nonsense → refusal expected
    ]
    for r in reviews:
        print(f"\nReview: {r}")
        print(f"Extract: {analyze(r)}")


if __name__ == "__main__":
    main()
