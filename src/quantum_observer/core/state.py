from dataclasses import dataclass, field
from typing import Dict, Any
import math


@dataclass
class DecisionState:
    """
    Represents a single possible future in a decision superposition.

    A DecisionState is immutable in meaning but mutable in probability
    as observer interaction and contextual weighting are applied.
    """

    id: str
    description: str

    # Core probabilistic attributes
    probability: float  # Must be between 0 and 1
    entropy: float = field(init=False)

    # Qualitative attributes (used for explainability)
    risk_level: str = "medium"
    emotional_impact: str = "neutral"

    # Arbitrary metadata for extensibility
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self._validate_probability()
        self.entropy = self._calculate_entropy()

    def _validate_probability(self):
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError(
                f"Invalid probability {self.probability}. "
                "Probability must be between 0 and 1."
            )

    def _calculate_entropy(self) -> float:
        """
        Calculates Shannon entropy contribution for this decision state.

        Entropy is highest when probability is near 0.5 and lowest at 0 or 1.
        """
        if self.probability in (0.0, 1.0):
            return 0.0

        return -self.probability * math.log2(self.probability)

    def update_probability(self, new_probability: float) -> None:
        """
        Updates the probability of the state and recalculates entropy.
        Intended to be called after observer interaction or reweighting.
        """
        self.probability = new_probability
        self._validate_probability()
        self.entropy = self._calculate_entropy()

    def explain(self) -> Dict[str, Any]:
        """
        Returns a transparent, serializable explanation of the decision state.
        """
        return {
            "id": self.id,
            "description": self.description,
            "probability": round(self.probability, 4),
            "entropy": round(self.entropy, 4),
            "risk_level": self.risk_level,
            "emotional_impact": self.emotional_impact,
            "metadata": self.metadata,
        }
