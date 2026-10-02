from tradeapp.monitoring.health import HealthSnapshot
from tradeapp.monitoring.notifications import NotificationCenter
from tradeapp.paper.long_run import LongPaperValidator
from tradeapp.shadow.session import ShadowSession
from tradeapp.validation.e2e import E2ERunner,FailureCase
from tradeapp.release.final_gate import FinalGate
def test_health(): assert HealthSnapshot(True,True,True,True).healthy()
def test_notifications(): assert NotificationCenter().publish("info","ok").message=="ok"
def test_paper(): assert LongPaperValidator().validate(5,10,1).completed
def test_shadow(): assert not ShadowSession().record("BTC","BUY",100).executed
def test_e2e(): assert E2ERunner().evaluate([FailureCase("disconnect",True)]).passed()
def test_gate_locked(): assert not FinalGate(True,True,True,True,True,1).ready()
