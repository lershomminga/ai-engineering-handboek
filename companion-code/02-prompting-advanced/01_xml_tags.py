"""
01 — XML-gestructureerde prompt.
Claude is getraind met XML-tags. Maakt prompts duidelijk gestructureerd
en vermindert prompt-injection-risico (untrusted content kan gewrapped).
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

SYSTEM = """Je bent een product-classificatie-assistent voor een NL webshop.

<rol>
Je classificeert klant-vragen in één van vier categoriën:
billing, shipping, product_info, complaint
</rol>

<output_format>
{
  "category": "billing|shipping|product_info|complaint",
  "confidence": 0.0-1.0,
  "reason": "max 1 zin"
}
</output_format>

<examples>
<example>
<input>Wanneer komt mijn pakket?</input>
<output>{"category": "shipping", "confidence": 0.95, "reason": "Vraag over levertijd"}</output>
</example>
<example>
<input>De rits van mijn jas is kapot, ik wil geld terug.</input>
<output>{"category": "complaint", "confidence": 0.98, "reason": "Defect product + refund-verzoek"}</output>
</example>
</examples>

<rules>
- Antwoord ALTIJD in geldig JSON.
- Bij twijfel tussen 2 categoriën: kies de meest urgente.
- Confidence < 0.7 → markeer voor human review.
</rules>"""


def classify(question: str) -> str:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        system=SYSTEM,
        messages=[
            {"role": "user", "content": f"<input>{question}</input>"}
        ],
    )
    return resp.content[0].text


def main() -> None:
    questions = [
        "Mijn factuur klopt niet, ik wil refund",
        "Hoe groot is maat L precies?",
        "Bestelling besteld op 5 mei, nog niets ontvangen",
        "Hi hoe gaat het",  # edge case
    ]
    for q in questions:
        print(f"\nQ: {q}")
        print(f"A: {classify(q)}")


if __name__ == "__main__":
    main()
