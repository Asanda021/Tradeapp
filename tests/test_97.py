from decimal import Decimal

from tradeapp.monitoring.post_launch import (
    MonitoringSnapshot, PostLaunchMonitor
)

def snapshot(**changes):
    data = dict(
        equity=Decimal("100"), peak_equity=Decimal("100"),
        daily_loss=Decimal("0"), consecutive_losses=0,
        requests=100, errors=0,
    )
    data.update(changes)
    return MonitoringSnapshot(**data)

def test_normal_monitoring():
    result = PostLaunchMonitor().evaluate(snapshot())
    assert not result.halt
    assert result.severity == "NORMAL"

def test_risk_breaches_halt():
    result = PostLaunchMonitor().evaluate(
        snapshot(daily_loss=Decimal(".05"), consecutive_losses=3)
    )
    assert result.halt
    assert "daily loss limit" in result.reasons
    assert "consecutive loss limit" in result.reasons

def test_drawdown_and_error_rate_halt():
    result = PostLaunchMonitor().evaluate(
        snapshot(equity=Decimal("85"), peak_equity=Decimal("100"),
                 requests=10, errors=1)
    )
    assert result.halt
    assert "drawdown limit" in result.reasons
    assert "error rate limit" in result.reasons
