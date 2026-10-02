from dataclasses import dataclass
from decimal import Decimal
from tradeapp.backtest.costs import ExecutionCostModel

@dataclass(frozen=True)
class ProfessionalMetrics:
    total_return:Decimal; max_drawdown:Decimal; win_rate:Decimal
    expectancy:Decimal; sharpe_like:Decimal; sortino_like:Decimal

@dataclass(frozen=True)
class TradeRecord:
    pnl:Decimal
    equity_after:Decimal|None=None

class ProfessionalBacktest:
    def metrics(self,starting:Decimal,ending:Decimal,trades:list[TradeRecord],costs:ExecutionCostModel|None=None)->ProfessionalMetrics:
        if starting<=0: raise ValueError("starting must be positive")
        if costs is not None: ending=ending-costs.fee(ending)
        returns=[t.pnl/starting for t in trades]
        wins=[r for r in returns if r>0]
        mean=sum(returns,Decimal(0))/Decimal(len(returns)) if returns else Decimal(0)
        variance=sum((r-mean)**2 for r in returns)/Decimal(len(returns)) if returns else Decimal(0)
        downside=[r for r in returns if r<0]
        downside_mean=sum((r*r for r in downside),Decimal(0))/Decimal(len(downside)) if downside else Decimal(0)
        curve=[starting]+[t.equity_after for t in trades if t.equity_after is not None]
        peak=curve[0]; max_dd=Decimal(0)
        for value in curve:
            peak=max(peak,value)
            if peak>0: max_dd=max(max_dd,(peak-value)/peak)
        return ProfessionalMetrics((ending-starting)/starting,max_dd,
            Decimal(len(wins))/Decimal(len(returns)) if returns else Decimal(0),mean,
            mean/variance.sqrt() if variance>0 else Decimal(0),
            mean/downside_mean.sqrt() if downside_mean>0 else Decimal(0))
