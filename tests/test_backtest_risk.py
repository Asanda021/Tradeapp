from decimal import Decimal
from tradeapp.risk.policy import RiskEngine
def test_risk_blocks_daily_loss():
    d=RiskEngine().approve(Decimal('100'),Decimal('100'),Decimal('10'),Decimal('.05'),Decimal('0'),0); assert not d.allowed
def test_risk_caps_trade_size():
    d=RiskEngine().approve(Decimal('100'),Decimal('100'),Decimal('10'),Decimal('0'),Decimal('0'),0); assert d.allowed and d.quantity==Decimal('2')
