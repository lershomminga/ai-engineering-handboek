"""
02 — Streaming met TTFT-meting.
Laat zien hoe perceived speed verschilt: TTFT vs total.
"""
import os
import time
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


def main() -> None:
    t_start = time.time()
    t_first_token: float | None = None
    total_text = ""

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[
            {"role": "user", "content": "Schrijf een hard-boiled detective opening van 4 zinnen."}
        ],
    ) as stream:
        for text in stream.text_stream:
            if t_first_token is None:
                t_first_token = time.time()
            print(text, end="", flush=True)
            total_text += text

    t_end = time.time()

    print("\n\n=== Latency ===")
    print(f"TTFT  (time-to-first-token): {(t_first_token - t_start) * 1000:.0f} ms")
    print(f"Total response time:         {(t_end - t_start) * 1000:.0f} ms")
    print(f"Tokens/sec (output, approx): {len(total_text.split()) / (t_end - t_start):.1f}")


if __name__ == "__main__":
    main()
