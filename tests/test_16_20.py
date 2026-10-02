from decimal import Decimal
from tradeapp.validation.walk_forward import WalkForward
from tradeapp.validation.monte_carlo import MonteCarlo
from tradeapp.execution.engine import ExecutionEngine
from tradeapp.execution.state import OrderState
from tradeapp.adapters.paper import PaperAdapter
from tradeapp.domain.models import OrderRequest,Side
from tradeapp.security.keys import ApiKeyRecord,KeyPolicy

def test_walk_forward_windows(): assert len(WalkForward().split(100,60,20))==2
def test_monte_carlo_is_seeded(): assert MonteCarlo().resample([Decimal('.01'),Decimal('-.01')],5)==MonteCarlo().resample([Decimal('.01'),Decimal('-.01')],5)
def test_paper_execution():
    d=ExecutionEngine(PaperAdapter()).submit(OrderRequest('BTC',Side.BUY,Decimal('1'))); assert d.state is OrderState.FILLED
def test_live_is_disabled():
    class Fake: name='live'
    d=ExecutionEngine(Fake()).submit(OrderRequest('BTC',Side.BUY,Decimal('1'))); assert d.state is OrderState.REJECTED
def test_key_policy_blocks_withdrawal():
    try: KeyPolicy.validate(ApiKeyRecord('x','abc',True,True)); assert False
    except ValueError: assert True
