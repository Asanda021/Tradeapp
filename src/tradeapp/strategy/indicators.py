from decimal import Decimal

def ema(values:list[Decimal],period:int)->Decimal:
    if not values or period<=0: raise ValueError("invalid EMA input")
    k=Decimal("2")/Decimal(period+1)
    result=values[0]
    for value in values[1:]: result=(value*k)+(result*(Decimal("1")-k))
    return result

def rsi(values:list[Decimal],period:int=14)->Decimal:
    if len(values)<=period: return Decimal("50")
    gains=[]; losses=[]
    for a,b in zip(values[-period-1:],values[-period:]):
        d=b-a
        gains.append(max(d,Decimal("0"))); losses.append(max(-d,Decimal("0")))
    avg_gain=sum(gains,Decimal("0"))/Decimal(period)
    avg_loss=sum(losses,Decimal("0"))/Decimal(period)
    if avg_loss==0: return Decimal("100") if avg_gain else Decimal("50")
    rs=avg_gain/avg_loss
    return Decimal("100")-(Decimal("100")/(Decimal("1")+rs))
