from typing import List, Dict, Any

from core.state import DecisionState


class EthicalConstraints:
    """
    Enforces ethical, risk, and safety constraints
    before probabilistic collapse.
    """

    def filter(
        self,
        states: List[DecisionState],
        observer_context: Dict[str, Any],
    ) -> List[DecisionState]:
        allowed_states = []

        for state in states:
            if self._violates_constraints(state, observer_context):
                continue

            allowed_states.append(state)

        return allowed_states

    def _violates_constraints(
        self,
        state: DecisionState,
        observer_context: Dict[str, Any],
    ) -> bool:
        risk_tolerance = observer_context.get(
            "max_risk_level", "medium"
        )

        # Hard ethical exclusion
        if state.metadata.get("ethical_flag") is False:
            return True

        # Risk-based exclusion
        if (
            state.metadata.get("risk") == "high"
            and risk_tolerance == "low"
        ):
            return True

        return False
