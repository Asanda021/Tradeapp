from dataclasses import dataclass,field
from decimal import Decimal
from datetime import datetime,timezone

@dataclass
class PaperRun:
    starting_cash:Decimal
    cash:Decimal
    trades:int=0
    pnl:Decimal=Decimal("0")
    failures:list[str]=field(default_factory=list)
    started_at:datetime=field(default_factory=lambda:datetime.now(timezone.utc))
    def record(self,pnl:Decimal)->None:
        self.pnl+=pnl; self.cash+=pnl; self.trades+=1
    def fail(self,reason:str)->None: self.failures.append(reason)
    def healthy(self)->bool: return not self.failures and self.cash>=0

class LongPaperValidator:
    def __init__(self,min_trades:int=1): self.min_trades=min_trades
    def validate(self,run:PaperRun)->bool:
        return run.healthy() and run.trades>=self.min_trades
