from dataclasses import dataclass

@dataclass(frozen=True)
class ControlledLiveEvidence:
    sandbox: bool = False
    market_data: bool = False
    paper: bool = False
    shadow: bool = False
    backtest: bool = False
    walk_forward: bool = False
    local_ai: bool = False
    news: bool = False
    recovery: bool = False
    e2e: bool = False
    windows: bool = False
    android: bool = False
    security: bool = False

    def missing(self) -> tuple[str, ...]:
        return tuple(name for name, ok in vars(self).items() if not ok)

    def complete(self) -> bool:
        return not self.missing()


@dataclass(frozen=True)
class ControlledLiveGate:
    enabled: bool = False
    manual_approval: bool = False
    emergency_stop_ready: bool = False
    max_notional: float = 0.0

    def permits(self, evidence: ControlledLiveEvidence, approved: bool,
                emergency_stop_ready: bool, notional: float) -> bool:
        return (
            self.enabled
            and self.manual_approval
            and approved
            and self.emergency_stop_ready
            and emergency_stop_ready
            and evidence.complete()
            and self.max_notional > 0
            and 0 < notional <= self.max_notional
        )
