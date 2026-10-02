from tradeapp.validation.safe_smoke import run_safe_smoke


def test_safe_smoke_gates_1_to_10_are_green_without_faking_real_world_evidence():
    result = run_safe_smoke()
    assert all(result.values())
    assert len(result) == 10
