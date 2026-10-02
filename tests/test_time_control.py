from datetime import datetime, timedelta, timezone
import pytest
from tradeapp.domain.time_control import RunSchedule

def test_duration_controls_execution_window():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    s = RunSchedule(start, duration=timedelta(hours=8))
    assert s.is_active(start)
    assert s.is_active(start + timedelta(hours=7))
    assert not s.is_active(start + timedelta(hours=9))

def test_invalid_duration_rejected():
    with pytest.raises(ValueError):
        RunSchedule(datetime.now(timezone.utc), duration=timedelta(0))
