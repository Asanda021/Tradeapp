from dataclasses import dataclass
from tradeapp.release.live_gate import ControlledLiveEvidence, ControlledLiveGate

@dataclass(frozen=True)
class ControlledLivePreflight:
    evidence: ControlledLiveEvidence
    gate: ControlledLiveGate
    approved: bool = False
    emergency_stop_ready: bool = False
    notional: float = 0.0

    def missing(self) -> tuple[str, ...]:
        return self.evidence.missing()

    def permits(self) -> bool:
        return self.gate.permits(
            self.evidence, self.approved, self.emergency_stop_ready, self.notional
        )

    def status(self) -> str:
        return "PERMITTED" if self.permits() else "BLOCKED"
