from dataclasses import dataclass, field
from decimal import Decimal

@dataclass(frozen=True)
class MonitoringLimits:
    max_daily_loss: Decimal = Decimal(".05")
    max_drawdown: Decimal = Decimal(".10")
    max_consecutive_losses: int = 3
    max_error_rate: Decimal = Decimal(".10")

@dataclass(frozen=True)
class MonitoringSnapshot:
    equity: Decimal
    peak_equity: Decimal
    daily_loss: Decimal
    consecutive_losses: int
    requests: int
    errors: int

@dataclass(frozen=True)
class MonitoringDecision:
    halt: bool
    reasons: tuple[str, ...]
    severity: str

class PostLaunchMonitor:
    def evaluate(self, snapshot: MonitoringSnapshot,
                 limits: MonitoringLimits = MonitoringLimits()) -> MonitoringDecision:
        reasons: list[str] = []
        if snapshot.equity <= 0:
            reasons.append("invalid equity")
        if snapshot.daily_loss >= limits.max_daily_loss:
            reasons.append("daily loss limit")
        if snapshot.peak_equity > 0:
            drawdown = (snapshot.peak_equity - snapshot.equity) / snapshot.peak_equity
            if drawdown >= limits.max_drawdown:
                reasons.append("drawdown limit")
        if snapshot.consecutive_losses >= limits.max_consecutive_losses:
            reasons.append("consecutive loss limit")
        if snapshot.requests > 0 and Decimal(snapshot.errors) / Decimal(snapshot.requests) >= limits.max_error_rate:
            reasons.append("error rate limit")
        severity = "HALT" if reasons else "NORMAL"
        return MonitoringDecision(bool(reasons), tuple(reasons), severity)

@dataclass
class MonitoringAudit:
    events: list[tuple[str, str]] = field(default_factory=list)

    def record(self, event: str, detail: str) -> None:
        self.events.append((event, detail))

    def export(self) -> tuple[tuple[str, str], ...]:
        return tuple(self.events)
