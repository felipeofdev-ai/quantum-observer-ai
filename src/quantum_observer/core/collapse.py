import random
from typing import Dict, Any
from quantum_observer.core.superposition import DecisionSuperposition
from quantum_observer.core.state import DecisionState


class ProbabilisticCollapseEngine:
    """
    Collapses a decision superposition into a single DecisionState.

    Collapse is probabilistic, entropy-aware, and fully explainable.
    """

    def collapse(self, superposition: DecisionSuperposition) -> Dict[str, Any]:
        """
        Executes probabilistic collapse and returns the selected state
        along with an explanation of why it survived.
        """
        weighted_states = self._apply_entropy_penalty(superposition.states)

        chosen_state = self._weighted_random_choice(weighted_states)

        return {
            "final_state": chosen_state.explain(),
            "collapse_reasoning": self._explain_collapse(weighted_states, chosen_state),
        }

    def _apply_entropy_penalty(
        self, states: list[DecisionState]
    ) -> list[DecisionState]:
        """
        Penalizes states with higher entropy before collapse.
        """
        adjusted_states = []

        for state in states:
            penalty = 1.0 / (1.0 + state.entropy)
            adjusted_probability = state.probability * penalty

            adjusted_state = DecisionState(
                id=state.id,
                description=state.description,
                probability=adjusted_probability,
                risk_level=state.risk_level,
                emotional_impact=state.emotional_impact,
                metadata=state.metadata,
            )

            adjusted_states.append(adjusted_state)

        # Normalize after penalty
        total = sum(s.probability for s in adjusted_states)
        for s in adjusted_states:
            s.update_probability(s.probability / total)

        return adjusted_states

    def _weighted_random_choice(
        self, states: list[DecisionState]
    ) -> DecisionState:
        """
        Selects a state using weighted randomness.
        """
        probabilities = [s.probability for s in states]
        return random.choices(states, weights=probabilities, k=1)[0]

    def _explain_collapse(
        self,
        states: list[DecisionState],
        chosen_state: DecisionState,
    ) -> Dict[str, Any]:
        """
        Generates a transparent explanation of the collapse.
        """
        return {
            "method": "entropy-penalized probabilistic collapse",
            "selected_state_id": chosen_state.id,
            "final_probability": round(chosen_state.probability, 4),
            "considered_states": [
                {
                    "id": s.id,
                    "final_probability": round(s.probability, 4),
                    "entropy": round(s.entropy, 4),
                }
                for s in states
            ],
        }
