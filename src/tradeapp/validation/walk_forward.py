from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class WalkForwardWindow:
    train_start:int; train_end:int; test_start:int; test_end:int
@dataclass(frozen=True)
class WalkForwardResult:
    windows:tuple[WalkForwardWindow,...]; stability:Decimal
class WalkForward:
    def split(self,length:int,train_size:int,test_size:int,step:int|None=None)->tuple[WalkForwardWindow,...]:
        if min(length,train_size,test_size)<=0: raise ValueError('sizes must be positive')
        step=step or test_size; result=[]; start=0
        while start+train_size+test_size<=length:
            result.append(WalkForwardWindow(start,start+train_size,start+train_size,start+train_size+test_size)); start+=step
        return tuple(result)
    def evaluate(self,returns:list[Decimal])->WalkForwardResult:
        if not returns: return WalkForwardResult((),Decimal('0'))
        positive=sum(1 for r in returns if r>0)
        return WalkForwardResult((),Decimal(positive)/Decimal(len(returns)))
