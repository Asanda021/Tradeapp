from tradeapp.release.live_gate import ControlledLiveEvidence, ControlledLiveGate

def test_phase_96_is_locked_by_default():
    gate = ControlledLiveGate()
    assert not gate.permits(ControlledLiveEvidence(), True, True, 1.0)

def test_phase_96_requires_all_evidence_and_controls():
    evidence = ControlledLiveEvidence(
        sandbox=True, market_data=True, paper=True, shadow=True,
        backtest=True, walk_forward=True, local_ai=True, news=True,
        recovery=True, e2e=True, windows=True, android=True, security=True,
    )
    gate = ControlledLiveGate(
        enabled=True, manual_approval=True,
        emergency_stop_ready=True, max_notional=10.0,
    )
    assert gate.permits(evidence, True, True, 1.0)
    assert not gate.permits(evidence, False, True, 1.0)
    assert not gate.permits(evidence, True, False, 1.0)
    assert not gate.permits(evidence, True, True, 11.0)

def test_phase_96_reports_missing_evidence():
    evidence = ControlledLiveEvidence(sandbox=True, security=True)
    missing = evidence.missing()
    assert "paper" in missing
    assert "android" in missing
    assert len(missing) == 11
