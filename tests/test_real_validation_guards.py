import os
import pytest

REAL_VALIDATION = os.getenv("TRADEAPP_REAL_VALIDATION") == "1"

@pytest.mark.skipif(not REAL_VALIDATION, reason="real validation requires explicit opt-in")
def test_real_validation_requires_explicit_opt_in():
    assert REAL_VALIDATION
