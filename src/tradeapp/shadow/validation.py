from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class ShadowObservation:
    symbol:str; decision:str; confidence:Decimal; would_execute:bool=False; reason:str=""
class ShadowValidator:
    def __init__(self,observations=None): self.observations=list(observations or [])
    def record(self,observation:ShadowObservation)->None:
        if observation.would_execute: raise ValueError("shadow observation cannot execute")
        self.observations.append(observation)
    def add(self,observation:ShadowObservation)->None: self.record(observation)
    def count(self)->int: return len(self.observations)
    def no_live_orders(self)->bool: return all(not x.would_execute for x in self.observations)
    def summary(self)->dict:
        return {"observations":len(self.observations),"executed":0,"buy":sum(x.decision.lower()=="buy" for x in self.observations),"sell":sum(x.decision.lower()=="sell" for x in self.observations)}
