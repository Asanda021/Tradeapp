from dataclasses import dataclass
from decimal import Decimal
from tradeapp.strategy.signals import Signal, StrategySignal

@dataclass(frozen=True)
class CouncilDecision:
    signal: Signal
    score: Decimal
    agreement: Decimal
    reasons: tuple[str,...]

class StrategyCouncil:
    def decide(self, signals: list[StrategySignal]) -> CouncilDecision:
        if not signals:
            return CouncilDecision(Signal.HOLD,Decimal("0"),Decimal("0"),("no strategy signals",))
        score=sum((s.strength if s.signal is Signal.BUY else -s.strength if s.signal is Signal.SELL else Decimal("0") for s in signals),Decimal("0"))
        agreement=Decimal(sum(1 for s in signals if s.signal is not Signal.HOLD))/Decimal(len(signals))
        signal=Signal.BUY if score > Decimal("0.2") else Signal.SELL if score < Decimal("-0.2") else Signal.HOLD
        return CouncilDecision(signal,min(Decimal("1"),abs(score)/Decimal(len(signals))),agreement,tuple(s.reason for s in signals))
