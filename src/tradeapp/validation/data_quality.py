from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class DataQuality:
    samples:int
    missing:int
    duplicates:int
    invalid:int
    def score(self)->Decimal:
        if self.samples<=0:return Decimal("0")
        bad=self.missing+self.duplicates+self.invalid
        return max(Decimal("0"),Decimal("1")-Decimal(bad)/Decimal(self.samples))
    def acceptable(self,threshold:Decimal=Decimal(".995"))->bool:return self.score()>=threshold
