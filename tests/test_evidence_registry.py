from tradeapp.validation.evidence_registry import EvidenceRecord, missing_gates, validate_record


def test_ci_cannot_become_real_world_evidence():
    record = EvidenceRecord("windows", "ci", "artifact.zip", True)
    assert validate_record(record) is False


def test_real_world_requires_artifact_and_verification():
    assert validate_record(EvidenceRecord("windows", "real_world", "", True)) is False
    assert validate_record(EvidenceRecord("windows", "real_world", "install-log.txt", True)) is True


def test_missing_gates_only_accept_verified_real_world_records():
    records = [
        EvidenceRecord("windows", "real_world", "install-log.txt", True),
        EvidenceRecord("android", "ci", "app.apk", True),
    ]
    missing = missing_gates(records)
    assert "windows" not in missing
    assert "android" in missing
    assert len(missing) == 14
