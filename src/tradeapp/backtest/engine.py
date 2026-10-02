from dataclasses import dataclass
from decimal import Decimal
from tradeapp.domain.models import Candle
from tradeapp.strategy.library import StrategyLibrary
from tradeapp.strategy.signals import Signal
@dataclass(frozen=True)
class BacktestResult:
    starting_cash:Decimal
    ending_cash:Decimal
    trades:int
    wins:int
    losses:int
    pnl:Decimal
class BacktestEngine:
    def run(self,candles:list[Candle],starting_cash:Decimal=Decimal('100'))->BacktestResult:
        if starting_cash<=0: raise ValueError('starting_cash must be positive')
        if not candles: return BacktestResult(starting_cash,starting_cash,0,0,0,Decimal('0'))
        cash=starting_cash; position=Decimal('0'); entry=Decimal('0'); trades=wins=losses=0
        for i in range(20,len(candles)):
            signals=StrategyLibrary().evaluate(candles[:i]); signal=next((s for s in signals if s.strategy=='sma_cross'),None); price=candles[i].close
            if signal and signal.signal is Signal.BUY and position==0: position=Decimal('1'); entry=price; cash-=price; trades+=1
            elif signal and signal.signal is Signal.SELL and position>0:
                pnl=price-entry; cash+=price; position=0
                if pnl>=0: wins+=1
                else: losses+=1
        ending=cash+position*candles[-1].close
        return BacktestResult(starting_cash,ending,trades,wins,losses,ending-starting_cash)
