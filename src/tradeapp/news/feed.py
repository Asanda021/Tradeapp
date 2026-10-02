from dataclasses import dataclass
from datetime import datetime
@dataclass(frozen=True)
class NewsArticle:
    title:str; source:str; published_at:datetime; symbols:tuple[str,...]; sentiment:str="neutral"; credibility:float=1.0
class NewsFeed:
    def relevant(self, articles:list[NewsArticle], symbol:str)->tuple[NewsArticle,...]:
        return tuple(a for a in articles if symbol in a.symbols)
