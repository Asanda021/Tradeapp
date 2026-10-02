from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"

class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"

@dataclass(frozen=True)
class Candle:
    symbol: str
    timestamp: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal

@dataclass(frozen=True)
class Quote:
    symbol: str
    timestamp: datetime
    bid: Decimal
    ask: Decimal

@dataclass(frozen=True)
class OrderRequest:
    symbol: str
    side: Side
    quantity: Decimal
    order_type: OrderType = OrderType.MARKET
    limit_price: Optional[Decimal] = None

@dataclass(frozen=True)
class OrderResult:
    order_id: str
    symbol: str
    side: Side
    quantity: Decimal
    status: str
    filled_price: Optional[Decimal] = None

@dataclass(frozen=True)
class AccountSnapshot:
    account_id: str
    currency: str
    available_cash: Decimal
    equity: Decimal
