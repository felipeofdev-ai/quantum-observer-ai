from typing import List, Dict, Any

from core.state import DecisionState


class ObserverInfluence:
    """
    Applies observer context and bias to a set of decision states
    without collapsing them.
    """

    def apply(
        self,
        states: List[DecisionState],
        observer_context: Dict[str, Any],
    ) -> List[DecisionState]:
        if not states:
            return []

        influenced_states: List[DecisionState] = []

        for state in states:
            adjusted_probability = self._apply_bias(
                state.probability,
                observer_context,
                state.label,
            )

            influenced_states.append(
                DecisionState(
                    label=state.label,
                    description=state.description,
                    probability=adjusted_probability,
                    metadata={
                        **state.metadata,
                        "observer_applied": True,
                    },
                )
            )

        return self._normalize(influenced_states)

    def _apply_bias(
        self,
        probability: float,
        observer_context: Dict[str, Any],
        label: str,
    ) -> float:
        """
        Simple bias model based on observer preferences.
        """
        preferences = observer_context.get("preferred_labels", [])

        if label in preferences:
            return min(probability * 1.2, 1.0)

        return probability

    def _normalize(
        self,
        states: List[DecisionState],
    ) -> List[DecisionState]:
        total = sum(state.probability for state in states)

        if total == 0:
            return states

        return [
            DecisionState(
                label=state.label,
                description=state.description,
                probability=state.probability / total,
                metadata=state.metadata,
            )
            for state in states
        ]
