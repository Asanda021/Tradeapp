from dataclasses import dataclass
from decimal import Decimal
from tradeapp.adapters.base import TradingAdapter
from tradeapp.strategy.library import StrategyLibrary
@dataclass
class PaperSession:
    adapter:TradingAdapter
    symbol:str
    budget:Decimal
    def run_once(self):
        candles=list(self.adapter.candles(self.symbol,100))
        return StrategyLibrary().evaluate(candles)
