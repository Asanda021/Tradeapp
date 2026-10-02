from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class BacktestMetrics:
    total_return: Decimal
    max_drawdown: Decimal
    win_rate: Decimal
    profit_factor: Decimal

def calculate_metrics(starting: Decimal, ending: Decimal, equity_curve: list[Decimal], wins: int, losses: int, gross_profit: Decimal, gross_loss: Decimal) -> BacktestMetrics:
    if starting <= 0: raise ValueError('starting must be positive')
    peak=starting; max_dd=Decimal('0')
    for value in equity_curve:
        peak=max(peak,value)
        if peak>0: max_dd=max(max_dd,(peak-value)/peak)
    total=(ending-starting)/starting
    total_trades=wins+losses
    win_rate=Decimal(wins)/Decimal(total_trades) if total_trades else Decimal('0')
    profit_factor=gross_profit/gross_loss if gross_loss>0 else (Decimal('999') if gross_profit>0 else Decimal('0'))
    return BacktestMetrics(total,max_dd,win_rate,profit_factor)
