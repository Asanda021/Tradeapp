from datetime import datetime,timezone
from decimal import Decimal
from tradeapp.news.models import NewsItem,Sentiment
from tradeapp.news.engine import NewsEngine
from tradeapp.strategy.lab import StrategyLab
from tradeapp.strategy.signals import StrategySignal,Signal

def test_strategy_lab_ranks():
    r=StrategyLab().rank([StrategySignal("a",Signal.BUY,Decimal(".2"),"a"),StrategySignal("b",Signal.BUY,Decimal(".8"),"b")])
    assert r[0].name=="b"

def test_news_assessment():
    n=NewsItem("positive","source",datetime.now(timezone.utc),("BTC",),Sentiment.POSITIVE,Decimal(".9"),Decimal(".8"))
    a=NewsEngine().assess([n],"BTC")
    assert a.sentiment is Sentiment.POSITIVE
