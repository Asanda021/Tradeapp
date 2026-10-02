from tradeapp.validation.evidence_policy import EvidenceStatus, REAL_WORLD_GATES, validate_real_world_evidence

def test_real_world_evidence_requires_real_source_for_every_gate():
    statuses = tuple(EvidenceStatus(gate, True, "real_world", "verified") for gate in REAL_WORLD_GATES)
    assert validate_real_world_evidence(statuses) == ()

def test_ci_evidence_does_not_count_as_real_world():
    statuses = tuple(EvidenceStatus(gate, True, "ci", "build passed") for gate in REAL_WORLD_GATES)
    assert validate_real_world_evidence(statuses) == REAL_WORLD_GATES
