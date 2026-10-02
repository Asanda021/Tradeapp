from tradeapp.execution.reconciliation import Reconciler,PositionSnapshot
from tradeapp.execution.recovery import ErrorRecovery
from tradeapp.execution.state import OrderState
from tradeapp.ai.report import LocalReportAI
from tradeapp.monitoring.audit import AuditLog
from tradeapp.monitoring.alerts import AlertManager
from tradeapp.release.gate import ReleaseGate
def test_position_reconciliation():
    r=Reconciler(); assert r.compare_position(PositionSnapshot("BTC",1),PositionSnapshot("BTC",1)).ok; assert not r.compare_position(PositionSnapshot("BTC",1),PositionSnapshot("BTC",2)).ok
def test_recovery_partial(): assert not ErrorRecovery().decide(OrderState.PARTIAL,0).safe_to_continue
def test_local_report(): assert LocalReportAI().explain("HOLD",.8,["no signal"]).decision=="HOLD"
def test_audit_alert(): assert AuditLog().record("start","session").action=="start"; assert AlertManager().risk("x").level=="risk"
def test_live_gate_locked(): assert not ReleaseGate(True,True,True).can_enable_live()
