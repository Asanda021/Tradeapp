from dataclasses import dataclass
from hashlib import sha256
import hmac
import time
from typing import Protocol
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

@dataclass(frozen=True)
class ExchangeCredentials:
    api_key: str
    api_secret: str

class HttpTransport(Protocol):
    def request(self, method: str, url: str, headers: dict[str,str], body: bytes|None = None) -> dict: ...

class UrllibTransport:
    def request(self, method: str, url: str, headers: dict[str,str], body: bytes|None = None) -> dict:
        req=Request(url,data=body,headers=headers,method=method)
        with urlopen(req,timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))

class BinanceSpotClient:
    """Network-capable REST client; live trading stays locked unless explicitly gated."""
    def __init__(self, credentials: ExchangeCredentials, base_url: str="https://api.binance.com",
                 transport: HttpTransport|None=None, allow_live: bool=False):
        if not credentials.api_key or not credentials.api_secret:
            raise ValueError("credentials are required")
        self.credentials=credentials
        self.base_url=base_url.rstrip("/")
        self.transport=transport or UrllibTransport()
        self.allow_live=allow_live

    def _signed(self, method: str, path: str, params: dict) -> dict:
        params={k:v for k,v in params.items() if v is not None}
        params.setdefault("timestamp",int(time.time()*1000))
        query=urlencode(params)
        signature=hmac.new(self.credentials.api_secret.encode(),query.encode(),sha256).hexdigest()
        headers={"X-MBX-APIKEY":self.credentials.api_key}
        return self.transport.request(method,f"{self.base_url}{path}?{query}&signature={signature}",headers)

    def account(self) -> dict:
        return self._signed("GET","/api/v3/account",{})

    def klines(self,symbol: str,interval: str="1m",limit: int=200) -> list:
        if not symbol: raise ValueError("symbol is required")
        if not 1 <= limit <= 1000: raise ValueError("limit must be 1..1000")
        url=f"{self.base_url}/api/v3/klines?{urlencode({'symbol':symbol.upper(),'interval':interval,'limit':limit})}"
        return self.transport.request("GET",url,{})

    def place_order(self,params: dict) -> dict:
        if not self.allow_live:
            raise RuntimeError("live order placement is locked")
        if not params.get("symbol") or not params.get("side") or not params.get("type"):
            raise ValueError("symbol, side and type are required")
        return self._signed("POST","/api/v3/order",params)
