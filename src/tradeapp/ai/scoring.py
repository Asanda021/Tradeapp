from decimal import Decimal

def confidence(strategy_score: Decimal, agreement: Decimal, regime_ok: bool) -> Decimal:
    base=(strategy_score*Decimal("0.6"))+(agreement*Decimal("0.3"))+(Decimal("0.1") if regime_ok else Decimal("0"))
    return max(Decimal("0"),min(Decimal("1"),base))
