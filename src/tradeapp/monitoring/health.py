from dataclasses import dataclass
@dataclass(frozen=True)
class HealthSnapshot:
    market_data: bool
    exchange: bool
    risk: bool
    execution: bool
    def healthy(self)->bool: return all((self.market_data,self.exchange,self.risk,self.execution))
