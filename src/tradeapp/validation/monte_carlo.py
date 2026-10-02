from decimal import Decimal
from random import Random
class MonteCarlo:
    def resample(self,returns:list[Decimal],runs:int=100,seed:int=7)->list[Decimal]:
        if runs<=0 or not returns: return []
        rng=Random(seed); out=[]
        for _ in range(runs):
            equity=Decimal('1')
            for _ in returns: equity*=Decimal('1')+rng.choice(returns)
            out.append(equity-Decimal('1'))
        return out
