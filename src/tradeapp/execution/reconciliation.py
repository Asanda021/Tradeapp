from dataclasses import dataclass
from tradeapp.domain.models import AccountSnapshot
@dataclass(frozen=True)
class ReconciliationResult:
    ok:bool
    reason:str
class Reconciler:
    def compare_account(self,expected:AccountSnapshot,actual:AccountSnapshot)->ReconciliationResult:
        ok=expected.currency==actual.currency and expected.available_cash==actual.available_cash and expected.equity==actual.equity
        return ReconciliationResult(ok,'account matches' if ok else 'account mismatch')
