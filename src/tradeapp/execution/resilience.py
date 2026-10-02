from dataclasses import dataclass
from enum import Enum

class FailureMode(str, Enum):
    NETWORK = "network"
    TIMEOUT = "timeout"
    DUPLICATE = "duplicate"
    UNKNOWN = "unknown"

@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 2

    def __post_init__(self):
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")

@dataclass(frozen=True)
class ExecutionGuard:
    kill_switch: bool = False
    connected: bool = True
    reconciliation_required: bool = False

    def permits_new_order(self) -> bool:
        return self.connected and not self.kill_switch and not self.reconciliation_required

    def after_disconnect(self) -> "ExecutionGuard":
        return ExecutionGuard(self.kill_switch, False, True)
