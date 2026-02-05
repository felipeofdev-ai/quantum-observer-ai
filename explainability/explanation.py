from typing import List, Dict, Any

from core.state import DecisionState


class DecisionExplanation:
    """
    Generates human-readable explanations for
    probabilistic and observer-influenced decisions.
    """

    def explain(
        self,
        final_state: DecisionState,
        all_states: List[DecisionState],
    ) -> Dict[str, Any]:
        ranked_states = sorted(
            all_states,
            key=lambda s: s.probability,
            reverse=True,
        )

        return {
            "selected_decision": self._explain_final(final_state),
            "alternatives": self._explain_alternatives(
                ranked_states,
                final_state,
            ),
            "uncertainty_summary": self._entropy_summary(
                all_states
            ),
        }

    def _explain_final(
        self,
        state: DecisionState,
    ) -> str:
        return (
            f"The selected decision '{state.label}' emerged "
            f"with a probability of {state.probability:.2f} "
            f"after observer influence and uncertainty weighting."
        )

    def _explain_alternatives(
        self,
        states: List[DecisionState],
        final_state: DecisionState,
    ) -> List[str]:
        explanations = []

        for state in states:
            if state.label == final_state.label:
                continue

            explanations.append(
                f"Alternative '{state.label}' remained viable "
                f"with probability {state.probability:.2f} "
                f"but was deprioritized during collapse."
            )

        return explanations

    def _entropy_summary(
        self,
        states: List[DecisionState],
    ) -> str:
        avg_uncertainty = sum(
            state.entropy for state in states
        ) / len(states)

        return (
            f"Average system uncertainty at collapse time "
            f"was {avg_uncertainty:.2f}, indicating "
            f"{'high' if avg_uncertainty > 0.6 else 'moderate'} ambiguity."
        )
