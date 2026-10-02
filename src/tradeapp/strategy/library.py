from tradeapp.domain.models import Candle
from tradeapp.strategy.signals import StrategySignal, sma_signal

class StrategyLibrary:
    def evaluate(self,candles:list[Candle])->list[StrategySignal]:
        closes=[c.close for c in candles]
        return [sma_signal(closes)]
