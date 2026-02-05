"""
Decision State definition.

A DecisionState represents a single possible outcome
within a quantum-inspired superposition of decisions.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class DecisionState:
    """
    Represents a single decision hypothesis.

    Attributes:
        outcome: The proposed action or decision.
        probability: Likelihood weight assigned to this state (0.0 to 1.0).
        context: Contextual data influencing this state.
        constraints_score: Compatibility score with hard constraints.
    """

    outcome: Any
    probability: float
    context: Dict[str, Any]
    constraints_score: float

    def validate(self) -> None:
        """
        Validates the integrity of the decision state.

        Raises:
            ValueError: If the state is invalid.
        """
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError("Probability must be between 0.0 and 1.0")

        if not 0.0 <= self.constraints_score <= 1.0:
            raise ValueError("Constraints score must be between 0.0 and 1.0")
