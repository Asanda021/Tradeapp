from dataclasses import dataclass,field
from decimal import Decimal
@dataclass
class PaperValidatorV2:
    starting_cash:Decimal=Decimal("100"); cash:Decimal=field(init=False); trades:int=0; realized_pnl:Decimal=Decimal("0"); failures:int=0
    def __post_init__(self): self.cash=self.starting_cash
    def record_trade(self,pnl:Decimal): self.realized_pnl+=pnl; self.cash+=pnl; self.trades+=1
    def record_failure(self): self.failures+=1
    def healthy(self): return self.failures==0 and self.cash>=0
