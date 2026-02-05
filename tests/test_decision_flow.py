from core.decision_engine import DecisionEngine


def test_decision_engine_runs():
    engine = DecisionEngine()

    prompt = "Should I switch careers?"
    observer_context = {
        "preferred_labels": [],
        "max_risk_level": "medium",
    }

    result = engine.decide(prompt, observer_context)

    assert "final_decision" in result
    assert result["final_decision"] is not None
    assert len(result["all_states"]) > 0
