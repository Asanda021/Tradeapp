from dataclasses import dataclass
from decimal import Decimal
from tradeapp.strategy.signals import Signal, StrategySignal

@dataclass(frozen=True)
class StrategyScore:
    name: str
    score: Decimal
    signal: Signal

class StrategyLab:
    """Ranks available signals without changing live rules automatically."""
    def rank(self, signals: list[StrategySignal]) -> list[StrategyScore]:
        ranked=[StrategyScore(s.strategy,s.strength,s.signal) for s in signals]
        return sorted(ranked,key=lambda x:x.score,reverse=True)
