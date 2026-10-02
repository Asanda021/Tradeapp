from dataclasses import dataclass
@dataclass(frozen=True)
class DashboardSnapshot:
    connected: bool
    market: str
    equity: float
    pnl: float
    risk: float
    decision: str
    status: str
class DashboardService:
    def snapshot(self, connected: bool, market: str, equity: float, pnl: float, risk: float, decision: str, status: str) -> DashboardSnapshot:
        return DashboardSnapshot(connected, market, equity, pnl, risk, decision, status)
