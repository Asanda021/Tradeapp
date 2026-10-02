from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class StrategyCandidate:
 name:str; family:str; score:Decimal; oos_score:Decimal
class StrategyLabV2:
 def rank(self,candidates): return tuple(sorted(candidates,key=lambda x:(x.oos_score,x.score),reverse=True))
 def robust(self,candidates): return tuple(c for c in self.rank(candidates) if c.oos_score>=Decimal("0"))
