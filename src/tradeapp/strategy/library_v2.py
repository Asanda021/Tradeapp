from dataclasses import dataclass
from tradeapp.strategy.signals import Signal
@dataclass(frozen=True)
class StrategySpec:
    name: str
    timeframe: str
    family: str
    enabled: bool = True
class StrategyCatalog:
    def __init__(self):
        self.strategies = [
            StrategySpec("sma_cross","1h","trend"),
            StrategySpec("ema_cross","1h","trend"),
            StrategySpec("rsi","15m","momentum"),
            StrategySpec("breakout","1h","breakout"),
            StrategySpec("bollinger_reversion","15m","mean_reversion"),
            StrategySpec("vwap","15m","volume"),
        ]
    def enabled(self) -> tuple[StrategySpec,...]: return tuple(s for s in self.strategies if s.enabled)
