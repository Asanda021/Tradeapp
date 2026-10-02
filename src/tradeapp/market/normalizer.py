from decimal import Decimal
from tradeapp.domain.models import Candle

def normalize_candle(symbol, timestamp, open_, high, low, close, volume) -> Candle:
    o, h, l, c, v = [Decimal(str(x)) for x in (open_, high, low, close, volume)]
    if h < max(o, c) or l > min(o, c) or l > h:
        raise ValueError("invalid OHLC values")
    if v < 0:
        raise ValueError("volume cannot be negative")
    return Candle(symbol, timestamp, o, h, l, c, v)
