from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from core.decision_engine import DecisionEngine
from explainability.explanation import DecisionExplanation


app = FastAPI(
    title="Quantum Observer AI",
    description="Quantum-inspired decision engine with observer-aware reasoning",
    version="0.1.0",
)

engine = DecisionEngine()
explainer = DecisionExplanation()


class DecisionRequest(BaseModel):
    prompt: str
    observer_context: Dict[str, Any]


class DecisionResponse(BaseModel):
    final_decision: Dict[str, Any]
    explanation: Dict[str, Any]


@app.post("/decide", response_model=DecisionResponse)
def decide(request: DecisionRequest):
    result = engine.decide(
        prompt=request.prompt,
        observer_context=request.observer_context,
    )

    explanation = explainer.explain(
        final_state=result["final_decision"],
        all_states=result["all_states"],
    )

    return {
        "final_decision": result["final_decision"].dict(),
        "explanation": explanation,
    }
