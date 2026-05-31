"""
01 — Basic code-based eval tegen golden set.
Substring-match assertions, accuracy + bootstrap-CI.
"""
import json
import numpy as np
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


def run_eval(model: str = "claude-haiku-4-5") -> dict:
    cases = [json.loads(l) for l in Path(__file__).parent.joinpath("golden_set.jsonl").read_text().splitlines()]

    results = []
    for case in cases:
        resp = client.messages.create(
            model=model,
            max_tokens=200,
            messages=[{"role": "user", "content": case["input"]}],
        )
        answer = resp.content[0].text.lower()
        correct = case["expected"].lower() in answer
        results.append({
            "input": case["input"],
            "expected": case["expected"],
            "actual": answer[:80],
            "correct": correct,
        })

    n_correct = sum(1 for r in results if r["correct"])
    accuracy = n_correct / len(results)

    # Bootstrap 95% CI
    scores = np.array([1 if r["correct"] else 0 for r in results])
    boot = [np.mean(np.random.choice(scores, size=len(scores), replace=True))
            for _ in range(1000)]
    ci_lo, ci_hi = np.percentile(boot, [2.5, 97.5])

    return {
        "model": model,
        "n_cases": len(results),
        "n_correct": n_correct,
        "accuracy": accuracy,
        "ci_95": (ci_lo, ci_hi),
        "results": results,
    }


def main() -> None:
    print("Running eval...\n")
    out = run_eval()

    for r in out["results"]:
        symbol = "✓" if r["correct"] else "✗"
        print(f"  {symbol} {r['input'][:50]}... → expected '{r['expected']}'")

    print(f"\n=== Summary ===")
    print(f"Model:    {out['model']}")
    print(f"Accuracy: {out['accuracy']:.1%} ({out['n_correct']}/{out['n_cases']})")
    print(f"95% CI:   [{out['ci_95'][0]:.2f}, {out['ci_95'][1]:.2f}]")


if __name__ == "__main__":
    main()
