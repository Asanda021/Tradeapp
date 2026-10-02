from tradeapp.domain.models import Candle
from tradeapp.strategy.indicators import ema,rsi
from tradeapp.strategy.signals import Signal,StrategySignal,sma_signal

class StrategyEngine:
    def evaluate(self,candles:list[Candle])->list[StrategySignal]:
        closes=[c.close for c in candles]
        if not closes: return []
        out=[sma_signal(closes)]
        if len(closes)>=21:
            fast,slow=ema(closes,9),ema(closes,21)
            sig=Signal.BUY if fast>slow else Signal.SELL if fast<slow else Signal.HOLD
            out.append(StrategySignal("ema_cross",sig,min(abs(fast-slow)/max(abs(slow),1),1),"EMA(9) above EMA(21)" if sig is Signal.BUY else "EMA(9) below EMA(21)" if sig is Signal.SELL else "EMAs aligned"))
            rv=rsi(closes); sig=Signal.BUY if rv<30 else Signal.SELL if rv>70 else Signal.HOLD
            out.append(StrategySignal("rsi",sig,min(abs(rv-50)/50,1),f"RSI={rv:.2f}"))
        return out
