from decimal import Decimal
from datetime import datetime, timezone
from tradeapp.backtest.professional import ProfessionalBacktest,TradeRecord
from tradeapp.validation.optimization import OptimizationResult,select_robust
from tradeapp.news.feed import NewsFeed,NewsArticle
from tradeapp.ai.local import LocalAI
from tradeapp.portfolio.correlation import correlation_risk
def test_metrics(): m=ProfessionalBacktest().metrics(Decimal("100"),Decimal("110"),[TradeRecord(Decimal("10")),TradeRecord(Decimal("-2"))]); assert m.total_return==Decimal(".1") and m.win_rate==Decimal(".5")
def test_robust_selection(): assert select_robust([OptimizationResult((("x",Decimal("1")),),Decimal("2"),Decimal("1"))]).out_of_sample_score==1
def test_news(): a=NewsArticle("x","s",datetime.now(timezone.utc),("BTC",)); assert NewsFeed().relevant([a],"BTC")== (a,)
def test_local_ai(): assert LocalAI().explain("HOLD",("reason",),2).confidence==1
def test_correlation(): assert correlation_risk({("A","B"):Decimal(".8")},("A","B"))==Decimal(".8")
