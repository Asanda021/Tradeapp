from decimal import Decimal
from tradeapp.ui.dashboard import DashboardService
from tradeapp.adapters.live import ExchangeAdapter, ExchangeConfig
from tradeapp.security.secret_store import SecretStore
from tradeapp.execution.order_manager import OrderManager
from tradeapp.domain.models import Side, OrderResult
from tradeapp.strategy.library_v2 import StrategyCatalog
def test_dashboard_snapshot(): assert DashboardService().snapshot(True,"BTC/USDT",100,2,.1,"HOLD","running").status=="running"
def test_exchange_is_sandbox_by_default(): assert ExchangeAdapter(ExchangeConfig("demo")).config.sandbox
def test_secret_store_does_not_keep_plain_secret(): s=SecretStore(); s.store("k","secret"); assert s.has("k") and "secret" not in s._digests["k"]
def test_order_manager(): assert OrderManager().position_delta(Side.BUY,Decimal("2"))==2
def test_strategy_catalog(): assert len(StrategyCatalog().enabled())>=6
