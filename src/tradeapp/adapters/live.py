from dataclasses import dataclass
from tradeapp.domain.models import Candle, Quote, OrderRequest, OrderResult
@dataclass(frozen=True)
class ExchangeConfig:
    provider: str
    sandbox: bool = True
class ExchangeAdapter:
    name = "exchange"
    def __init__(self, config: ExchangeConfig): self.config = config
    def normalize_quote(self, symbol: str, bid: float, ask: float) -> Quote:
        from datetime import datetime, timezone
        from decimal import Decimal
        return Quote(symbol, datetime.now(timezone.utc), Decimal(str(bid)), Decimal(str(ask)))
    def submit_order(self, request: OrderRequest) -> OrderResult:
        raise RuntimeError("real exchange connector is not configured")
