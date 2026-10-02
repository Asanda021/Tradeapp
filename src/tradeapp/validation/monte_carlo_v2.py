from decimal import Decimal
import random
def simulate(returns:list[Decimal],iterations:int=1000,seed:int=42)->dict:
    if not returns or iterations<=0:return {"iterations":0,"median":Decimal("0"),"worst":Decimal("0")}
    rng=random.Random(seed); totals=[]
    for _ in range(iterations):
        total=Decimal("0")
        for _ in returns: total+=rng.choice(returns)
        totals.append(total)
    totals.sort()
    return {"iterations":iterations,"median":totals[len(totals)//2],"worst":totals[0]}
