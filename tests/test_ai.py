from decimal import Decimal
from tradeapp.ai.explainer import LocalExplainer
from tradeapp.strategy.council import CouncilDecision
from tradeapp.strategy.signals import Signal

def test_local_explainer_is_free_and_deterministic():
    e=LocalExplainer().explain(CouncilDecision(Signal.HOLD,Decimal("0"),Decimal("0"),("x",)))
    assert "عدم معامله" in e.title
