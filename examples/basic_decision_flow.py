from core.decision_engine import DecisionEngine
from explainability.explanation import DecisionExplanation


def run_example() -> None:
    engine = DecisionEngine()
    explainer = DecisionExplanation()

    prompt = "Should I leave my current job to focus on software engineering?"

    observer_context = {
        "preferred_labels": ["Accelerated Growth"],
        "max_risk_level": "medium",
    }

    result = engine.decide(
        prompt=prompt,
        observer_context=observer_context,
    )

    explanation = explainer.explain(
        final_state=result["final_decision"],
        all_states=result["all_states"],
    )

    print("\n=== FINAL DECISION ===")
    print(result["final_decision"])

    print("\n=== EXPLANATION ===")
    print(explanation)


if __name__ == "__main__":
    run_example()
