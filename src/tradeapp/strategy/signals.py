from dataclasses import dataclass
from enum import Enum
from decimal import Decimal

class Signal(str, Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"

@dataclass(frozen=True)
class StrategySignal:
    strategy: str
    signal: Signal
    strength: Decimal
    reason: str

def sma_signal(closes: list[Decimal], fast: int = 5, slow: int = 20) -> StrategySignal:
    if len(closes) < slow:
        return StrategySignal("sma_cross",Signal.HOLD,Decimal("0"),"not enough data")
    f=sum(closes[-fast:])/Decimal(fast)
    s=sum(closes[-slow:])/Decimal(slow)
    if f > s:
        return StrategySignal("sma_cross",Signal.BUY,min(Decimal("1"),(f-s)/max(abs(s),Decimal("0.0000001"))),"fast average above slow average")
    if f < s:
        return StrategySignal("sma_cross",Signal.SELL,min(Decimal("1"),(s-f)/max(abs(s),Decimal("0.0000001"))),"fast average below slow average")
    return StrategySignal("sma_cross",Signal.HOLD,Decimal("0"),"averages aligned")
