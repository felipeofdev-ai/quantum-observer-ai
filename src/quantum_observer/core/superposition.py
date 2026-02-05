from typing import List
from quantum_observer.core.state import DecisionState


class DecisionSuperposition:
    """
    Maintains a collection of DecisionStates coexisting in superposition.

    This class guarantees probabilistic consistency and exposes
    global uncertainty metrics without collapsing outcomes.
    """

    def __init__(self, states: List[DecisionState]):
        if not states:
            raise ValueError("Superposition must contain at least one DecisionState.")

        self.states = states
        self._validate_probabilities()

    def _validate_probabilities(self) -> None:
        total_probability = sum(state.probability for state in self.states)

        if not 0.99 <= total_probability <= 1.01:
            raise ValueError(
                f"Invalid probability distribution. Sum is {total_probability:.4f}, "
                "expected approximately 1.0."
            )

    def normalize(self) -> None:
        """
        Normalizes probabilities so that their sum equals 1.
        Useful after reweighting operations.
        """
        total = sum(state.probability for state in self.states)
        if total == 0:
            raise ValueError("Cannot normalize probabilities with total sum zero.")

        for state in self.states:
            state.update_probability(state.probability / total)

    def total_entropy(self) -> float:
        """
        Computes the total entropy of the superposition.
        """
        return sum(state.entropy for state in self.states)

    def ranked_states(self) -> List[DecisionState]:
        """
        Returns states ordered by probability (descending),
        without collapsing the superposition.
        """
        return sorted(self.states, key=lambda s: s.probability, reverse=True)

    def explain(self) -> List[dict]:
        """
        Returns an explainable representation of all states.
        """
        return [state.explain() for state in self.states]
