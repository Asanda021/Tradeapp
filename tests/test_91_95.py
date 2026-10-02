from tradeapp.release.rc import ReleaseCandidateGate
from tradeapp.release.checklist import ReleaseChecklist,ReleaseEvidence
from tradeapp.report.release import ReleaseReport
from tradeapp.ui.windows_contract import DEFAULT_WINDOWS_CONTRACT
from tradeapp.ui.android_contract import DEFAULT_ANDROID_CONTRACT
from tradeapp.i18n.persian_final import tr
from tradeapp.monitoring.release_log import ReleaseAuditLog

def test_release_gate_and_checklist():
    e=ReleaseEvidence(sandbox=True,security=True)
    c=ReleaseChecklist(True,True,True,True,e)
    assert c.status()=="RC_WITH_EVIDENCE_GAPS"
    assert ReleaseCandidateGate(True,True,True,True,e.count()).passed()

def test_clients_and_report():
    assert DEFAULT_WINDOWS_CONTRACT.valid()
    assert DEFAULT_ANDROID_CONTRACT.valid()
    assert tr("emergency_stop")=="توقف اضطراری"
    r=ReleaseReport("RC",tuple(range(91,96)),True,True,True,("android",))
    assert not r.ready_for_controlled_live()

def test_release_log():
    log=ReleaseAuditLog(); log.record("build","passed")
    assert log.export()==(("build","passed"),)
