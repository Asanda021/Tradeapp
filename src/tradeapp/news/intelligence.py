from dataclasses import dataclass
from datetime import datetime,timezone
@dataclass(frozen=True)
class NewsSignal:
    symbol:str
    sentiment:float
    relevance:float
    credibility:float
    severity:float
    freshness:float
    source:str
    def score(self)->float:return self.sentiment*self.relevance*self.credibility*self.severity*self.freshness
class NewsIntelligence:
    def assess(self,items:list[NewsSignal],symbol:str)->float:
        relevant=[x for x in items if x.symbol.upper()==symbol.upper()]
        return sum(x.score() for x in relevant)
