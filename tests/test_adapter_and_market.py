from decimal import Decimal
from datetime import datetime, timezone
import pytest
from tradeapp.adapters.paper import PaperAdapter
from tradeapp.adapters.registry import AdapterRegistry
from tradeapp.domain.models import OrderRequest, Side
from tradeapp.market.normalizer import normalize_candle

def test_paper_adapter_and_registry():
    adapter = PaperAdapter(Decimal("100"))
    registry = AdapterRegistry()
    registry.register(adapter)
    assert registry.names() == ("paper",)
    result = adapter.submit_order(OrderRequest("BTCUSD", Side.BUY, Decimal("0.1")))
    assert result.status == "filled"
    assert result.filled_price is not None

def test_invalid_ohlc_rejected():
    with pytest.raises(ValueError):
        normalize_candle("BTCUSD", datetime.now(timezone.utc), 10, 5, 1, 4, 2)
