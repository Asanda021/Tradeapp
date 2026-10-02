from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class OptimizationResult:
    parameters: tuple[tuple[str,Decimal],...]
    score: Decimal
    out_of_sample_score: Decimal
def select_robust(candidates: list[OptimizationResult], min_oos: Decimal=Decimal("0")) -> OptimizationResult:
    valid=[c for c in candidates if c.out_of_sample_score>=min_oos]
    if not valid: raise ValueError("no robust candidate")
    return max(valid,key=lambda c:(c.out_of_sample_score,c.score))
