from tradeapp.release.evidence import EvidenceLedger, EvidenceRecord
from tradeapp.release.preflight import ControlledLivePreflight
from tradeapp.release.live_gate import ControlledLiveEvidence, ControlledLiveGate
from tradeapp.validation.acceptance import default_campaign
from tradeapp.ui.windows_contract import DEFAULT_WINDOWS_CONTRACT
from tradeapp.ui.android_contract import DEFAULT_ANDROID_CONTRACT
from tradeapp.validation.e2e_runner import E2ETradeFlow

def test_campaign_has_fifteen_gates():
    assert len(default_campaign().items) == 15

def test_windows_and_android_contracts_are_valid():
    assert DEFAULT_WINDOWS_CONTRACT.valid()
    assert DEFAULT_ANDROID_CONTRACT.valid()

def test_e2e_paper_flow():
    result = E2ETradeFlow().run(True, True, True, True, True)
    assert result.passed

def test_evidence_ledger_requires_real_evidence():
    ledger = EvidenceLedger((EvidenceRecord("windows"), EvidenceRecord("android", True, "apk")))
    assert not ledger.complete()
    assert ledger.missing() == ("windows",)

def test_controlled_live_preflight_stays_blocked_by_default():
    preflight = ControlledLivePreflight(
        evidence=ControlledLiveEvidence(),
        gate=ControlledLiveGate(),
    )
    assert preflight.status() == "BLOCKED"
    assert not preflight.permits()
