from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class WalkForwardWindow:
    train_start:int; train_end:int; test_start:int; test_end:int
@dataclass(frozen=True)
class WalkForwardReport:
    windows:int
    stable:int
    oos_returns:tuple[Decimal,...]
    def passed(self,min_stability:Decimal=Decimal(".6"))->bool:
        return self.windows>0 and Decimal(self.stable)/Decimal(self.windows)>=min_stability
def build_windows(length:int,train:int,test:int,step:int)->tuple[WalkForwardWindow,...]:
    if min(length,train,test,step)<=0:return ()
    out=[]; start=0
    while start+train+test<=length:
        out.append(WalkForwardWindow(start,start+train,start+train,start+train+test)); start+=step
    return tuple(out)
