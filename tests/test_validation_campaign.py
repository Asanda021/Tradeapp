from tradeapp.validation.acceptance import AcceptanceItem, default_campaign

def test_campaign_has_ten_real_world_gates():
    campaign = default_campaign()
    assert len(campaign.items) == 10
    assert campaign.status() == "VALIDATION_INCOMPLETE"

def test_verified_evidence_completes_campaign():
    campaign = default_campaign()
    campaign.items = [
        AcceptanceItem(i.key, i.title, i.automated, i.real_world_required, True, "test-evidence")
        for i in campaign.items
    ]
    assert campaign.automated_passed
    assert campaign.real_world_complete
    assert campaign.status() == "REAL_WORLD_VALIDATED"
