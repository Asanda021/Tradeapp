from dataclasses import dataclass
@dataclass
class CircuitBreaker:
    active: bool = False
    reason: str = ''
    def trip(self,reason:str)->None: self.active=True; self.reason=reason
    def reset(self)->None: self.active=False; self.reason=''
    def permits_trading(self)->bool: return not self.active
