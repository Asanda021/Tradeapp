from dataclasses import dataclass
from decimal import Decimal
from tradeapp.domain.models import OrderRequest, OrderResult, Side
@dataclass(frozen=True)
class Position:
    symbol: str
    quantity: Decimal
class OrderManager:
    def position_delta(self, side: Side, quantity: Decimal) -> Decimal:
        return quantity if side is Side.BUY else -quantity
    def accept(self, result: OrderResult) -> bool:
        return result.status in {"submitted", "partial", "filled"}
