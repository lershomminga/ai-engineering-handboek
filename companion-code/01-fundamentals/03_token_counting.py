"""
03 — Token counting met de Anthropic API.
Vergelijkt NL vs EN voor dezelfde zin → toont 'token-tax'.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

PAIRS = [
    ("EN", "The Anthropic API offers prompt caching to reduce costs."),
    ("NL", "De Anthropic API biedt prompt caching om kosten te verminderen."),
    ("EN", "arbeidsongeschiktheidsverzekering"),  # NL-woord in EN-zin
    ("NL", "arbeidsongeschiktheidsverzekering"),
    ("EN", "long-form professional translation services"),
    ("NL", "uitgebreide professionele vertaaldiensten"),
]


def count_tokens(text: str) -> int:
    resp = client.messages.count_tokens(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": text}],
    )
    return resp.input_tokens


def main() -> None:
    print(f"{'Lang':<6}{'Tokens':<10}{'Chars':<10}{'Tok/Char':<12}Text")
    print("-" * 80)
    for lang, text in PAIRS:
        tokens = count_tokens(text)
        print(f"{lang:<6}{tokens:<10}{len(text):<10}{tokens / len(text):<12.3f}{text}")

    print("\nObservaties:")
    print("- NL kost typisch 1.3-1.8× meer tokens per gelijke betekenis.")
    print("- Lange NL-samenstellingen ('arbeidsongeschiktheids...') = veel sub-tokens.")
    print("- Strategie voor productie: schrijf system-prompt in EN, vraag output in NL.")


if __name__ == "__main__":
    main()
