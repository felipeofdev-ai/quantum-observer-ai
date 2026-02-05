from typing import Dict, Any, List

from core.state import DecisionState
from core.superposition import SuperpositionEngine
from core.observer_influence import ObserverInfluence
from core.collapse import CollapseEngine


class DecisionEngine:
    """
    Coordinates the full decision lifecycle:
    superposition → observer influence → probabilistic collapse.
    """

    def __init__(self) -> None:
        self.superposition_engine = SuperpositionEngine()
        self.observer_influence = ObserverInfluence()
        self.collapse_engine = CollapseEngine()

    def decide(
        self,
        prompt: str,
        observer_context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Executes a full decision cycle and returns
        the collapsed decision along with traceability data.
        """

        # 1. Generate superposed decision states
        states: List[DecisionState] = self.superposition_engine.generate(
            prompt
        )

        # 2. Apply observer influence
        influenced_states = self.observer_influence.apply(
            states,
            observer_context
        )

        # 3. Collapse into a final decision
        final_state = self.collapse_engine.collapse(
            influenced_states
        )

        return {
            "final_decision": final_state,
            "all_states": influenced_states,
            "observer_context": observer_context,
            "prompt": prompt,
        }
