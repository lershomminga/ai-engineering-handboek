"""
02 — Reflexion (Shinn et al., NeurIPS 2023, arXiv:2303.11366).
Actor probeert → Evaluator scoort → Reflector schrijft les → retry.
+22% AlfWorld, +11% HumanEval, +20% HotpotQA vs baseline ReAct.
"""
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


def reflexion(task: str, max_trials: int = 3) -> dict:
    """Returns final solution + reflection-history."""
    episodic_memory: list[str] = []

    for trial in range(1, max_trials + 1):
        print(f"\n=== Trial {trial} ===")

        # 1) ACTOR — probeert taak met reflecties uit eerdere trials
        reflections_str = "\n".join(f"- {r}" for r in episodic_memory) or "(geen)"
        attempt = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=f"Reflecties van eerdere pogingen:\n{reflections_str}",
            messages=[{"role": "user", "content": task}],
        ).content[0].text
        print(f"Actor:\n  {attempt[:200]}...")

        # 2) EVALUATOR — slaagde het?
        verdict = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=200,
            messages=[{
                "role": "user",
                "content": (
                    f"Taak: {task}\n\nPoging:\n{attempt}\n\n"
                    "Slaagde dit? Antwoord met JA of NEE + 1 zin reden."
                ),
            }],
        ).content[0].text.strip()
        print(f"Evaluator: {verdict}")

        if verdict.startswith("JA"):
            return {"success": True, "trial": trial, "answer": attempt,
                    "reflections": episodic_memory}

        # 3) REFLECTOR — wat ging fout? Schrijf een bondige les.
        reflection = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": (
                    f"De volgende poging faalde. Analyseer kort waarom en schrijf "
                    f"1 zin als 'les voor volgende keer':\n\nTaak: {task}\n\n"
                    f"Poging: {attempt}\n\nEvaluator: {verdict}"
                ),
            }],
        ).content[0].text.strip()
        print(f"Reflector: {reflection}")
        episodic_memory.append(reflection)

    return {"success": False, "trial": max_trials, "answer": None,
            "reflections": episodic_memory}


if __name__ == "__main__":
    task = (
        "Bedenk een naam voor een Nederlands AI-bedrijf dat zich richt op "
        "MKB-administratie. Eisen: max 2 lettergrepen, beschikbaar als .nl domein, "
        "evoceert vertrouwen en snelheid, geen Engelse woorden."
    )
    result = reflexion(task)
    print(f"\n=== Final ===")
    print(f"Success: {result['success']} na {result['trial']} trial(s)")
    if result['answer']:
        print(f"Answer: {result['answer']}")
