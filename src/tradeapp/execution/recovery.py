from dataclasses import dataclass
from tradeapp.execution.state import OrderState
@dataclass(frozen=True)
class RecoveryDecision:
    retry: bool
    safe_to_continue: bool
    reason: str
class ErrorRecovery:
    def decide(self, state: OrderState, attempts: int, max_attempts: int = 3) -> RecoveryDecision:
        if state is OrderState.REJECTED and attempts < max_attempts: return RecoveryDecision(True, False, "retry rejected order")
        if state is OrderState.PARTIAL: return RecoveryDecision(False, False, "reconcile partial fill before continuing")
        return RecoveryDecision(False, state in {OrderState.FILLED, OrderState.CANCELLED}, "state requires no recovery")
