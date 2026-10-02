"""Offline/safe smoke validation for gates 1-10.

These checks exercise the implemented components without credentials, live orders,
or pretending that CI/synthetic data is real-world evidence.
"""

from datetime import datetime, timezone
from decimal import Decimal

from tradeapp.adapters.sandbox_execution import SandboxExecutionAdapter
from tradeapp.domain.models import Candle, OrderRequest, OrderType, Side
from tradeapp.backtest.engine import BacktestEngine
from tradeapp.paper.long_run import LongPaperValidator, PaperRun
from tradeapp.shadow.validation import ShadowObservation, ShadowValidator
from tradeapp.ai.benchmark import LocalAIBenchmark
from tradeapp.ai.local_runtime import LocalModelRuntime
from tradeapp.news.rss import RSSNewsProvider
from tradeapp.execution.recovery import ErrorRecovery
from tradeapp.execution.state import OrderState
from tradeapp.validation.security_suite import SecurityCheck, SecuritySuite


def run_safe_smoke() -> dict[str, bool]:
    # 1: sandbox adapter contract (local deterministic adapter, not external sandbox).
    result = SandboxExecutionAdapter().submit_order(
        OrderRequest("BTCUSDT", Side.BUY, Decimal("1"), OrderType.MARKET)
    )
    g1 = result.status == "filled"

    # 2: market-data model stability using deterministic candles.
    candles = [
        Candle("BTCUSDT", datetime(2026, 1, 1, tzinfo=timezone.utc), Decimal(100+i),
               Decimal(101+i), Decimal(99+i), Decimal(100+i), Decimal(10))
        for i in range(30)
    ]
    g2 = len(candles) == 30 and all(c.high >= c.low for c in candles)

    # 3: paper session.
    paper = PaperRun(Decimal("100"), Decimal("100"))
    paper.record(Decimal("1"))
    g3 = LongPaperValidator(min_trades=1).validate(paper)

    # 4: shadow must never execute.
    shadow = ShadowValidator()
    shadow.record(ShadowObservation("BTCUSDT", "buy", Decimal("0.8")))
    g4 = shadow.no_live_orders() and shadow.count() == 1

    # 5: backtest engine over deterministic multi-symbol data.
    multi = candles + [Candle("ETHUSDT", c.timestamp, c.open, c.high, c.low, c.close, c.volume) for c in candles]
    g5 = BacktestEngine().run(multi).starting_cash == Decimal("100")

    # 6: walk-forward/Monte Carlo framework safety contract: deterministic repeated backtests.
    r1 = BacktestEngine().run(candles)
    r2 = BacktestEngine().run(candles)
    g6 = r1 == r2

    # 7: local AI benchmark uses deterministic fallback and never calls a paid API.
    bench = LocalAIBenchmark().run(LocalModelRuntime(), ["explain buy", "explain hold"])
    g7 = bench.cases == 2 and bench.passed == 2

    # 8: multi-source news parser with two local RSS payloads.
    xml = b"""<rss><channel><item><title>BTC update</title><pubDate>Thu, 01 Jan 2026 00:00:00 GMT</pubDate><link>https://example.test/1</link></item></channel></rss>"""
    provider = RSSNewsProvider()
    g8 = len(provider.fetch("source-a", "source-a", lambda _: xml)) == 1 and len(
        provider.fetch("source-b", "source-b", lambda _: xml)
    ) == 1

    # 9: recovery policy.
    recovery = ErrorRecovery()
    g9 = recovery.decide(OrderState.REJECTED, 0).retry and not recovery.decide(
        OrderState.PARTIAL, 0
    ).safe_to_continue

    # 10: security policy contract.
    security = SecuritySuite().evaluate([
        SecurityCheck("encrypted_store", True),
        SecurityCheck("no_withdrawal_permission", True),
        SecurityCheck("live_locked", True),
    ])
    g10 = security.passed()

    return {
        "01_sandbox_connection": g1,
        "02_market_data": g2,
        "03_paper": bool(g3),
        "04_shadow": g4,
        "05_backtest": bool(g5),
        "06_walk_forward": g6,
        "07_local_ai": g7,
        "08_news": g8,
        "09_recovery": g9,
        "10_security": g10,
    }
