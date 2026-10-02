from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class ShadowObservation:
    symbol:str
    decision:str
    confidence:Decimal
    would_execute:bool
    reason:str
class ShadowValidator:
    def __init__(self): self.observations:list[ShadowObservation]=[]
    def record(self,observation:ShadowObservation)->None:
        if observation.would_execute: raise ValueError("shadow observation cannot execute")
        self.observations.append(observation)
    def summary(self)->dict:
        return {"observations":len(self.observations),"executed":0,"buy":sum(x.decision=="buy" for x in self.observations),"sell":sum(x.decision=="sell" for x in self.observations)}
