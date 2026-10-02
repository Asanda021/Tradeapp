from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class ProfessionalMetrics:
    total_return: Decimal
    max_drawdown: Decimal
    win_rate: Decimal
    expectancy: Decimal
    sharpe_like: Decimal
    sortino_like: Decimal
@dataclass(frozen=True)
class TradeRecord:
    pnl: Decimal
class ProfessionalBacktest:
    def metrics(self, starting: Decimal, ending: Decimal, trades: list[TradeRecord]) -> ProfessionalMetrics:
        if starting <= 0: raise ValueError("starting must be positive")
        returns=[t.pnl/starting for t in trades]
        wins=[r for r in returns if r>0]
        mean=sum(returns,Decimal(0))/Decimal(len(returns)) if returns else Decimal(0)
        variance=(sum((r-mean)**2 for r in returns)/Decimal(len(returns))) if returns else Decimal(0)
        downside=[r for r in returns if r<0]
        downside_mean=sum((r*r for r in downside),Decimal(0))/Decimal(len(downside)) if downside else Decimal(0)
        return ProfessionalMetrics(
            (ending-starting)/starting,
            Decimal(0),
            Decimal(len(wins))/Decimal(len(returns)) if returns else Decimal(0),
            mean,
            mean/variance.sqrt() if variance>0 else Decimal(0),
            mean/downside_mean.sqrt() if downside_mean>0 else Decimal(0),
        )
