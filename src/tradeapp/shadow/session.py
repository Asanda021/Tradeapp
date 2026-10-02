from dataclasses import dataclass
@dataclass(frozen=True)
class ShadowDecision:
    symbol:str
    action:str
    hypothetical_price:float
    executed:bool=False
class ShadowSession:
    def record(self,symbol:str,action:str,price:float)->ShadowDecision:
        if price<=0: raise ValueError("price must be positive")
        return ShadowDecision(symbol,action,price,False)
