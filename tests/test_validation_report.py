from tradeapp.validation.acceptance import AcceptanceItem, AcceptanceCampaign
from tradeapp.validation.report import build_report

def test_default_report_never_invents_real_world_evidence():
    report = build_report()
    assert report.live_locked is True
    assert report.real_world_missing
    assert report.status != "REAL_WORLD_VALIDATED"

def test_report_distinguishes_automated_and_real_world():
    campaign = AcceptanceCampaign([
        AcceptanceItem("auto", "automated", True, False, True, "ci"),
        AcceptanceItem("real", "real", False, True, False, ""),
    ])
    report = build_report(campaign)
    assert report.automated_missing == ()
    assert report.real_world_missing == ("real",)
    assert report.status == "AUTOMATED_VALIDATION_COMPLETE_REAL_EVIDENCE_MISSING"
