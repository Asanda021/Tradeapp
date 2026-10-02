from dataclasses import dataclass
from decimal import Decimal
from tradeapp.ai.scoring import confidence
from tradeapp.news.models import NewsAssessment,Sentiment
from tradeapp.strategy.council import StrategyCouncil
from tradeapp.strategy.signals import Signal,StrategySignal
@dataclass(frozen=True)
class Decision:
    signal:Signal
    confidence:Decimal
    reasons:tuple[str,...]
class DecisionEngine:
    def decide(self,signals:list[StrategySignal],news:NewsAssessment)->Decision:
        council=StrategyCouncil().decide(signals)
        conf=confidence(council.score.copy_abs(),council.agreement,True)
        if news.sentiment is Sentiment.NEGATIVE and news.impact>=Decimal('.7') and council.signal is Signal.BUY:return Decision(Signal.HOLD,conf,('high-impact negative news blocks a buy',)+council.reasons)
        if news.sentiment is Sentiment.POSITIVE and news.impact>=Decimal('.7') and council.signal is Signal.SELL:return Decision(Signal.HOLD,conf,('high-impact positive news blocks a sell',)+council.reasons)
        return Decision(council.signal,conf,council.reasons)
