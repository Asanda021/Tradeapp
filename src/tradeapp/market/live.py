from datetime import datetime,timezone
from decimal import Decimal
from tradeapp.domain.models import Candle,Quote
from tradeapp.adapters.http_exchange import BinanceSpotClient

class LiveMarketData:
    def __init__(self,client:BinanceSpotClient): self.client=client
    def candles(self,symbol:str,interval:str="1m",limit:int=200)->list[Candle]:
        rows=self.client.klines(symbol,interval,limit)
        return [Candle(symbol.upper(),datetime.fromtimestamp(int(r[0])/1000,tz=timezone.utc),Decimal(str(r[1])),Decimal(str(r[2])),Decimal(str(r[3])),Decimal(str(r[4])),Decimal(str(r[5]))) for r in rows]
    def quote(self,symbol:str)->Quote:
        data=self.client.transport.request("GET",f"{self.client.base_url}/api/v3/ticker/bookTicker?symbol={symbol.upper()}",{})
        return Quote(symbol.upper(),datetime.now(timezone.utc),Decimal(str(data["bidPrice"])),Decimal(str(data["askPrice"])))
