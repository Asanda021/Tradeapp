from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

class Sentiment(str,Enum):
    POSITIVE="positive"
    NEGATIVE="negative"
    NEUTRAL="neutral"

@dataclass(frozen=True)
class NewsItem:
    title:str
    source:str
    published_at:datetime
    symbols:tuple[str,...]
    sentiment:Sentiment
    credibility:Decimal
    severity:Decimal

@dataclass(frozen=True)
class NewsAssessment:
    sentiment:Sentiment
    impact:Decimal
    reasons:tuple[str,...]
