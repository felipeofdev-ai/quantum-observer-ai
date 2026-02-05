from typing import Dict
from quantum_observer.core.superposition import DecisionSuperposition


class ObserverInfluence:
    """
    Applies observer preferences to a decision superposition
    without collapsing outcomes.

    This represents controlled human bias in the system.
    """

    def __init__(self, preferences: Dict[str, float]):
        """
        preferences example:
        {
            "risk_tolerance": 0.2,
            "emotional_weight": 0.5,
            "long_term_focus": 0.3
        }

        All values must be between 0 and 1.
        """
        self._validate_preferences(preferences)
        self.preferences = preferences

    def _validate_preferences(self, preferences: Dict[str, float]) -> None:
        for key, value in preferences.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(
                    f"Invalid preference value for '{key}': {value}. "
                    "Must be between 0 and 1."
                )

    def apply(self, superposition: DecisionSuperposition) -> None:
        """
        Reweights decision state probabilities based on observer preferences.
        """
        for state in superposition.states:
            bias = self._calculate_bias(state)
            adjusted_probability = state.probability * bias
            state.update_probability(adjusted_probability)

        superposition.normalize()

    def _calculate_bias(self, state) -> float:
        """
        Calculates a bias multiplier based on state attributes
        and observer preferences.
        """
        bias = 1.0

        if state.risk_level == "high":
            bias *= (1.0 - self.preferences.get("risk_tolerance", 0.0))

        if state.emotional_impact == "high":
            bias *= (1.0 + self.preferences.get("emotional_weight", 0.0))

        return max(bias, 0.01)
