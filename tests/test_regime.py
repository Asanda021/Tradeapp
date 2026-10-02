from datetime import datetime, timezone, timedelta
from decimal import Decimal
from tradeapp.domain.models import Candle
from tradeapp.market.regime import detect_regime, MarketRegime

def make(values):
    now=datetime.now(timezone.utc)
    return [Candle("X",now+timedelta(minutes=i),Decimal(v),Decimal(v),Decimal(v),Decimal(v),Decimal("1")) for i,v in enumerate(values)]

def test_detects_uptrend():
    r=detect_regime(make([100,101,102,103,104,105,106]))
    assert r.regime is MarketRegime.TREND_UP
