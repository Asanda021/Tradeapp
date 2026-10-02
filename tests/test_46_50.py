from decimal import Decimal
from tradeapp.adapters.sandbox_execution import SandboxExecutionAdapter
from tradeapp.domain.models import OrderRequest,Side
from tradeapp.execution.order_lifecycle import LifecycleState,OrderLifecycle
from tradeapp.paper.validator_v2 import PaperValidatorV2
from tradeapp.shadow.validation import ShadowObservation,ShadowValidator
from tradeapp.validation.production_readiness import ProductionReadiness
def test_sandbox():
 r=SandboxExecutionAdapter().submit_order(OrderRequest("BTC/USDT",Side.BUY,Decimal("1"))); assert r.status=="filled"
def test_lifecycle():
 assert OrderLifecycle("x",LifecycleState.REJECTED).can_retry(); assert OrderLifecycle("y",LifecycleState.PARTIAL).needs_reconciliation()
def test_paper():
 p=PaperValidatorV2(); p.record_trade(Decimal("2")); p.record_trade(Decimal("-1")); assert p.realized_pnl==Decimal("1") and p.healthy()
def test_shadow():
 s=ShadowValidator([]); s.add(ShadowObservation("BTC/USDT","HOLD",Decimal("100"))); assert s.count()==1 and s.no_live_orders()
def test_gate():
 assert ProductionReadiness(True,True,True,True,True).passed(); assert not ProductionReadiness(True,True,True,False,True).passed()
