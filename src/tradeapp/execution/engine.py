from dataclasses import dataclass
from decimal import Decimal
from tradeapp.adapters.base import TradingAdapter
from tradeapp.domain.models import OrderRequest,OrderResult
from tradeapp.execution.state import OrderState
@dataclass(frozen=True)
class ExecutionDecision:
    state:OrderState
    result:OrderResult|None
    reason:str
class ExecutionEngine:
    def __init__(self,adapter:TradingAdapter,live_enabled:bool=False): self.adapter=adapter; self.live_enabled=live_enabled
    def submit(self,request:OrderRequest)->ExecutionDecision:
        if not self.live_enabled and getattr(self.adapter,'name','')!='paper': return ExecutionDecision(OrderState.REJECTED,None,'live trading disabled')
        try:
            result=self.adapter.submit_order(request)
        except Exception as exc:
            return ExecutionDecision(OrderState.REJECTED,None,f'order rejected: {exc}')
        state=OrderState.FILLED if result.status=='filled' else OrderState.SUBMITTED
        return ExecutionDecision(state,result,'order accepted')
