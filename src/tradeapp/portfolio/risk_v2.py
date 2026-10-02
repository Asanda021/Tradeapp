from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class PortfolioRisk:
    equity: Decimal
    max_exposure: Decimal
    current_exposure: Decimal
    max_daily_loss: Decimal
    daily_loss: Decimal
    def permits(self, additional: Decimal=Decimal("0")) -> bool:
        if self.equity <= 0: return False
        return self.current_exposure + additional <= self.max_exposure and self.daily_loss <= self.max_daily_loss
@dataclass(frozen=True)
class PositionSizer:
    risk_fraction: Decimal = Decimal("0.02")
    def size(self, equity: Decimal, stop_distance: Decimal) -> Decimal:
        if equity <= 0 or stop_distance <= 0: return Decimal("0")
        return equity * self.risk_fraction / stop_distance
