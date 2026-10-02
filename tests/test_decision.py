from decimal import Decimal
from tradeapp.decision.engine import DecisionEngine
from tradeapp.news.models import NewsAssessment,Sentiment
from tradeapp.strategy.signals import StrategySignal,Signal
def test_high_impact_negative_news_blocks_buy():
    d=DecisionEngine().decide([StrategySignal('x',Signal.BUY,Decimal('1'),'buy')],NewsAssessment(Sentiment.NEGATIVE,Decimal('.9'),('bad',))); assert d.signal is Signal.HOLD
