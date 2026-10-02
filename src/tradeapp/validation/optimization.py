from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class OptimizationResult:
    name: object
    in_sample: Decimal
    out_of_sample: Decimal
    stability: Decimal=Decimal("0")
    @property
    def out_of_sample_score(self)->Decimal: return self.out_of_sample
    @property
    def score(self)->Decimal: return self.in_sample
    def robust(self,min_oos:Decimal=Decimal("0"),min_stability:Decimal=Decimal("0"))->bool:
        return self.out_of_sample>=min_oos and self.stability>=min_stability
def select_robust(candidates:list[OptimizationResult],min_oos:Decimal=Decimal("0"),min_stability:Decimal=Decimal("0"))->OptimizationResult|None:
    valid=[c for c in candidates if c.robust(min_oos,min_stability)]
    return max(valid,key=lambda c:(c.out_of_sample,c.stability,c.in_sample),default=None)
def overfit_gap(result:OptimizationResult)->Decimal: return result.in_sample-result.out_of_sample
