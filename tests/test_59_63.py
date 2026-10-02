from datetime import datetime,timezone
from decimal import Decimal
from tradeapp.adapters.http_exchange import BinanceSpotClient,ExchangeCredentials
from tradeapp.auth.connection import OAuthConfig,AccountConnectionService
from tradeapp.market.live import LiveMarketData
from tradeapp.strategy.engine import StrategyEngine
from tradeapp.domain.models import Candle

class FakeTransport:
    def __init__(self): self.calls=[]
    def request(self,method,url,headers,body=None):
        self.calls.append((method,url,headers))
        if "klines" in url: return [[0,"1","2","0.5","1.5","10"]]
        if "bookTicker" in url: return {"bidPrice":"1.0","askPrice":"1.1"}
        return {"balances":[]}

def test_connector_and_lock():
    t=FakeTransport(); c=BinanceSpotClient(ExchangeCredentials("key","secret"),transport=t)
    assert c.account()=={"balances":[]}
    try: c.place_order({"symbol":"BTCUSDT","side":"BUY","type":"MARKET"})
    except RuntimeError: pass
    else: raise AssertionError("live order must remain locked")

def test_market_normalization():
    m=LiveMarketData(BinanceSpotClient(ExchangeCredentials("k","s"),transport=FakeTransport()))
    assert m.candles("BTCUSDT")[0].close==Decimal("1.5")
    assert m.quote("BTCUSDT").ask==Decimal("1.1")

def test_auth_and_strategy():
    cfg=OAuthConfig("google","https://accounts.google.com/o/oauth2/v2/auth","client","https://app/callback",("openid","email"))
    assert "client_id=client" in cfg.authorization_url("state")
    assert AccountConnectionService().connected("binance","a1").state is not None
    candles=[Candle("BTCUSDT",datetime.now(timezone.utc),Decimal(i),Decimal(i+1),Decimal(i-1),Decimal(i),Decimal(10)) for i in range(1,25)]
    assert len(StrategyEngine().evaluate(candles))>=1
