from dataclasses import dataclass
from enum import Enum
from decimal import Decimal
from statistics import mean, pstdev
from tradeapp.domain.models import Candle

class MarketRegime(str, Enum):
    TREND_UP = "trend_up"
    TREND_DOWN = "trend_down"
    RANGE = "range"
    HIGH_VOLATILITY = "high_volatility"
    LOW_VOLATILITY = "low_volatility"
    UNKNOWN = "unknown"

@dataclass(frozen=True)
class RegimeSnapshot:
    regime: MarketRegime
    volatility: Decimal
    trend_score: Decimal

def detect_regime(candles: list[Candle]) -> RegimeSnapshot:
    if len(candles) < 5:
        return RegimeSnapshot(MarketRegime.UNKNOWN, Decimal("0"), Decimal("0"))
    closes=[float(c.close) for c in candles]
    first,last=closes[0],closes[-1]
    avg=max(abs(mean(closes)), 1e-12)
    trend=Decimal(str((last-first)/avg))
    returns=[(b-a)/max(abs(a),1e-12) for a,b in zip(closes,closes[1:])]
    vol=Decimal(str(pstdev(returns) if len(returns)>1 else 0))
    if vol > Decimal("0.02"):
        regime=MarketRegime.HIGH_VOLATILITY
    elif vol < Decimal("0.002"):
        regime=MarketRegime.LOW_VOLATILITY
    elif trend > Decimal("0.01"):
        regime=MarketRegime.TREND_UP
    elif trend < Decimal("-0.01"):
        regime=MarketRegime.TREND_DOWN
    else:
        regime=MarketRegime.RANGE
    return RegimeSnapshot(regime,vol,trend)
