from dataclasses import dataclass,field
from decimal import Decimal
@dataclass
class Campaign:
    name:str
    sessions:int=0
    trades:int=0
    pnl:Decimal=Decimal("0")
    failures:list[str]=field(default_factory=list)
    def record_session(self,trades:int,pnl:Decimal): self.sessions+=1; self.trades+=trades; self.pnl+=pnl
    def fail(self,reason:str): self.failures.append(reason)
    def valid(self,min_sessions:int=10)->bool: return self.sessions>=min_sessions and not self.failures
@dataclass(frozen=True)
class CampaignGate:
    sessions:int
    failures:int
    pnl:Decimal
    def passed(self,min_sessions:int=10)->bool: return self.sessions>=min_sessions and self.failures==0
