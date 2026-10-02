from dataclasses import dataclass
from tradeapp.domain.models import AccountSnapshot

@dataclass(frozen=True)
class ReconciliationResult:
    ok: bool
    reason: str

@dataclass(frozen=True)
class PositionSnapshot:
    symbol: str
    quantity: float

class Reconciler:
    def compare_account(self, expected: AccountSnapshot, actual: AccountSnapshot) -> ReconciliationResult:
        ok = expected.currency == actual.currency and expected.available_cash == actual.available_cash and expected.equity == actual.equity
        return ReconciliationResult(ok, "account matches" if ok else "account mismatch")

    def compare_position(self, expected: PositionSnapshot, actual: PositionSnapshot) -> ReconciliationResult:
        ok = expected.symbol == actual.symbol and expected.quantity == actual.quantity
        return ReconciliationResult(ok, "position matches" if ok else "position mismatch")
