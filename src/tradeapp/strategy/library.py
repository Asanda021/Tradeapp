from tradeapp.domain.models import Candle
from tradeapp.strategy.signals import StrategySignal, Signal, sma_signal
from tradeapp.strategy.indicators import rsi, ema

class StrategyLibrary:
    def evaluate(self,candles:list[Candle])->list[StrategySignal]:
        closes=[c.close for c in candles]
        signals=[sma_signal(closes)]
        if len(closes)>=15:
            value=rsi(closes)
            if value < 30:
                signals.append(StrategySignal("rsi",Signal.BUY,min((30-value)/30,1),"RSI is oversold"))
            elif value > 70:
                signals.append(StrategySignal("rsi",Signal.SELL,min((value-70)/30,1),"RSI is overbought"))
            else:
                signals.append(StrategySignal("rsi",Signal.HOLD,0,"RSI is neutral"))
        if len(closes)>=10:
            fast=ema(closes[-10:],5)
            slow=ema(closes,10)
            if fast>slow:
                signals.append(StrategySignal("ema",Signal.BUY,min((fast-slow)/max(abs(slow),1e-12),1),"EMA trend is positive"))
            elif fast<slow:
                signals.append(StrategySignal("ema",Signal.SELL,min((slow-fast)/max(abs(slow),1e-12),1),"EMA trend is negative"))
            else:
                signals.append(StrategySignal("ema",Signal.HOLD,0,"EMA is flat"))
        return signals
