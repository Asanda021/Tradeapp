from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4
from tradeapp.adapters.base import TradingAdapter
from tradeapp.domain.models import AccountSnapshot, Candle, OrderRequest, OrderResult, Quote, Side

class PaperAdapter(TradingAdapter):
    name = "paper"
    def __init__(self, cash: Decimal = Decimal("100.00")) -> None:
        self.cash = cash
        self.last_prices: dict[str, Decimal] = {}
        self.orders: list[OrderResult] = []
    def account(self) -> AccountSnapshot:
        return AccountSnapshot("paper-account", "USD", self.cash, self.cash)
    def quote(self, symbol: str) -> Quote:
        price = self.last_prices.get(symbol, Decimal("100"))
        return Quote(symbol, datetime.now(timezone.utc), price - Decimal("0.01"), price + Decimal("0.01"))
    def candles(self, symbol: str, limit: int = 100) -> list[Candle]:
        if limit <= 0:
            raise ValueError("limit must be positive")
        q = self.quote(symbol)
        return [Candle(symbol, q.timestamp, q.ask, q.ask, q.bid, q.bid, Decimal("0")) for _ in range(limit)]
    def submit_order(self, request: OrderRequest) -> OrderResult:
        if request.quantity <= 0:
            raise ValueError("quantity must be positive")
        quote = self.quote(request.symbol)
        price = request.limit_price or (quote.ask if request.side is Side.BUY else quote.bid)
        result = OrderResult(str(uuid4()), request.symbol, request.side, request.quantity, "filled", price)
        self.last_prices[request.symbol] = price
        self.orders.append(result)
        return result
    def cancel_order(self, order_id: str) -> bool:
        return any(o.order_id == order_id for o in self.orders)
