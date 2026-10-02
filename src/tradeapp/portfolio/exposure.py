from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class PositionExposure:
    symbol: str
    notional: Decimal
    weight: Decimal
@dataclass(frozen=True)
class PortfolioSnapshot:
    equity: Decimal
    positions: tuple[PositionExposure,...]
    cash_weight: Decimal
    def concentration(self)->Decimal:
        return max((p.weight for p in self.positions),default=Decimal('0'))
