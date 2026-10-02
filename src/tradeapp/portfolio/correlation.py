from decimal import Decimal
def correlation_risk(matrix:dict[tuple[str,str],Decimal], positions:tuple[str,...])->Decimal:
    pairs=[matrix.get((a,b),matrix.get((b,a),Decimal(0))) for i,a in enumerate(positions) for b in positions[i+1:]]
    return sum(pairs,Decimal(0))/Decimal(len(pairs)) if pairs else Decimal(0)
