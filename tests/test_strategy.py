from decimal import Decimal
from tradeapp.strategy.signals import sma_signal,Signal,StrategySignal
from tradeapp.strategy.council import StrategyCouncil

def test_sma_signal_buy():
    s=sma_signal([Decimal(x) for x in range(1,30)])
    assert s.signal is Signal.BUY

def test_council_holds_conflicting_signals():
    d=StrategyCouncil().decide([
        StrategySignal("a",Signal.BUY,Decimal("0.5"),"up"),
        StrategySignal("b",Signal.SELL,Decimal("0.5"),"down"),
    ])
    assert d.signal is Signal.HOLD
