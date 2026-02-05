# Usage Guide

## Running the Decision Engine

### Python Example
```python
from core.decision_engine import DecisionEngine

engine = DecisionEngine()
result = engine.decide(
    prompt="Should I start a new business?",
    observer_context={"max_risk_level": "high"}
)
API Usage
POST /decide

Request
{
  "prompt": "Should I relocate for a new job?",
  "observer_context": {
    "preferred_labels": ["Growth"],
    "max_risk_level": "medium"
  }
}
Response
{
  "final_decision": {...},
  "explanation": {...}
}
