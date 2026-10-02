from dataclasses import dataclass
from datetime import datetime
from tradeapp.news.models import NewsItem
@dataclass(frozen=True)
class NewsKey:
    title:str
    source:str
    published_at:datetime
def deduplicate(items:list[NewsItem])->list[NewsItem]:
    seen=set(); result=[]
    for item in items:
        key=NewsKey(item.title.strip().casefold(),item.source.strip().casefold(),item.published_at)
        if key not in seen:
            seen.add(key); result.append(item)
    return result
