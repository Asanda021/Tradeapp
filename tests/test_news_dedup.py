from datetime import datetime,timezone
from decimal import Decimal
from tradeapp.news.dedup import deduplicate
from tradeapp.news.models import NewsItem,Sentiment
def test_duplicate_news_removed():
    t=datetime.now(timezone.utc); x=NewsItem('Same','S',t,('BTC',),Sentiment.NEUTRAL,Decimal('1'),Decimal('1')); assert len(deduplicate([x,x]))==1
