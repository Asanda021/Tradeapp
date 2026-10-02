from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
@dataclass(frozen=True)
class ShadowObservation:
    symbol:str; decision:str; reference_price:Decimal; hypothetical_fill:Optional[Decimal]=None
@dataclass
class ShadowValidator:
    observations:list[ShadowObservation]
    def add(self,item): self.observations.append(item)
    def count(self): return len(self.observations)
    def no_live_orders(self): return True
