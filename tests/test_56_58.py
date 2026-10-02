from decimal import Decimal
from tradeapp.portfolio.risk_v2 import PortfolioRisk,PositionSizer
from tradeapp.release.controlled_live import ControlledLivePolicy
from tradeapp.release.production import ProductionChecklist
def test_risk_and_position_size():
    r=PortfolioRisk(Decimal("100"),Decimal("20"),Decimal("5"),Decimal("5"),Decimal("1"))
    assert r.permits(Decimal("10")); assert not r.permits(Decimal("16"))
    assert PositionSizer().size(Decimal("100"),Decimal("2"))==Decimal("1")
def test_live_locked_by_default():
    assert not ControlledLivePolicy().permits(True,True,1)
def test_production_checklist():
    c=ProductionChecklist(True,True,True,True,True,True,True)
    assert c.ready()
    assert not ProductionChecklist(True,True,True,True,True,True,False).ready()
