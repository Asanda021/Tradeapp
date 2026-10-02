from decimal import Decimal
from tradeapp.news.models import NewsAssessment,NewsItem,Sentiment

class NewsEngine:
    """Deterministic scoring; real news feeds are added through adapters later."""
    def assess(self,items:list[NewsItem],symbol:str)->NewsAssessment:
        relevant=[x for x in items if symbol in x.symbols]
        if not relevant:
            return NewsAssessment(Sentiment.NEUTRAL,Decimal("0"),("no relevant news",))
        score=sum((x.credibility*x.severity*(Decimal("1") if x.sentiment is Sentiment.POSITIVE else Decimal("-1") if x.sentiment is Sentiment.NEGATIVE else Decimal("0")) for x in relevant),Decimal("0"))
        sentiment=Sentiment.POSITIVE if score>Decimal(".2") else Sentiment.NEGATIVE if score<Decimal("-.2") else Sentiment.NEUTRAL
        return NewsAssessment(sentiment,min(Decimal("1"),abs(score)),tuple(x.title for x in relevant))
