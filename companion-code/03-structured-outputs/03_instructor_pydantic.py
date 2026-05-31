"""
03 — Instructor library: Pydantic-first met automatic retry.
3M+ downloads/maand, werkt met 15+ providers.
Beste DX voor Python-projecten die toch al Pydantic gebruiken.
"""
from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator
from anthropic import Anthropic
import instructor

load_dotenv()
# Wrap Anthropic-client met instructor
client = instructor.from_anthropic(Anthropic())


class ReviewAnalysis(BaseModel):
    sentiment: Literal["positief", "negatief", "neutraal"]
    confidence: float = Field(ge=0, le=1, description="0-1, hoe zeker")
    intensity: int = Field(ge=1, le=5)
    topics: list[str] = Field(max_length=5)
    refusal: str | None = Field(default=None,
                                 description="Vul in als je het niet kunt bepalen")

    @field_validator("topics")
    @classmethod
    def lowercase_topics(cls, v: list[str]) -> list[str]:
        """Custom validator — Instructor retried bij ValidationError."""
        return [t.lower().strip() for t in v]


def analyze(review: str) -> ReviewAnalysis:
    return client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        max_retries=3,  # ← automatic retry-with-validation-feedback
        response_model=ReviewAnalysis,
        messages=[{"role": "user", "content": f"Analyseer: {review}"}],
    )


def main() -> None:
    reviews = [
        "Snelle levering, prima kwaliteit",
        "Pakket beschadigd, slecht.",
    ]
    for r in reviews:
        result = analyze(r)
        print(f"\nReview: {r}")
        print(f"  Sentiment:  {result.sentiment}  (confidence: {result.confidence})")
        print(f"  Intensity:  {result.intensity}/5")
        print(f"  Topics:     {result.topics}")
        if result.refusal:
            print(f"  ⚠ Refusal: {result.refusal}")


if __name__ == "__main__":
    main()
