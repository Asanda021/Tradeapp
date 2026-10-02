from dataclasses import dataclass
from enum import Enum
class LifecycleState(str,Enum):
    CREATED="created"; SUBMITTED="submitted"; PARTIAL="partial"; FILLED="filled"; CANCELLED="cancelled"; REJECTED="rejected"
@dataclass(frozen=True)
class OrderLifecycle:
    order_id:str; state:LifecycleState; attempts:int=0
    def can_retry(self): return self.state==LifecycleState.REJECTED and self.attempts<2
    def needs_reconciliation(self): return self.state in {LifecycleState.PARTIAL,LifecycleState.FILLED}
