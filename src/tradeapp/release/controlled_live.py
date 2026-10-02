from dataclasses import dataclass
@dataclass(frozen=True)
class ControlledLivePolicy:
    enabled: bool = False
    max_notional: float = 0.0
    manual_approval_required: bool = True
    emergency_stop_required: bool = True
    def permits(self, approved: bool, emergency_stop_ready: bool, notional: float) -> bool:
        return self.enabled and approved and emergency_stop_ready and self.max_notional > 0 and 0 < notional <= self.max_notional
