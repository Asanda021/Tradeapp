from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class CandidateEvidence:
    name:str
    oos:Decimal
    stability:Decimal
    drawdown:Decimal
    trades:int
class RobustStrategyLab:
    def filter(self,candidates:list[CandidateEvidence],min_oos:Decimal=Decimal("0"),max_drawdown:Decimal=Decimal(".2"),min_trades:int=30)->list[CandidateEvidence]:
        return [c for c in candidates if c.oos>=min_oos and c.stability>=Decimal(".6") and c.drawdown<=max_drawdown and c.trades>=min_trades]
