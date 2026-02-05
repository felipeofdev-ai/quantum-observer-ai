# Decision Model

## Overview

The decision model of Quantum Observer AI explains how multiple possible futures are evaluated, weighted, and collapsed into a single outcome through probabilistic reasoning and observer interaction.

---

## Decision State

Each possible future is represented as a structured decision state.

```python
DecisionState:
  id: string
  description: string
  probability: float
  risk_level: Low | Medium | High
  emotional_impact: Low | Medium | High
  entropy: float
  score: float
Superposition Generation
The decision prompt is analyzed semantically

Multiple coherent future scenarios are generated

Each scenario becomes a DecisionState

No option is prioritized initially

Entropy
Entropy measures uncertainty across all decision states.

High entropy means:

Outcomes are very different

There is no clear dominant option

The decision carries high uncertainty

Entropy is applied as a penalty during collapse.

Observer Influence
The observer influences the system by specifying:

Risk tolerance

Time horizon

Emotional priority

Constraints

These inputs dynamically adjust probabilities.

Collapse Logic (Conceptual)
Final Score =
  (Base Probability × Context Weight)
+ Observer Bias
- Entropy Penalty
The state with the strongest adjusted score survives the collapse.

Explainability
After collapse, the system explains:

Why this option survived

What factors mattered most

How observer input changed the outcome

Summary
This decision model ensures that uncertainty is respected until commitment occurs.
