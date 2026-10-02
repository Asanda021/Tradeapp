from dataclasses import dataclass
from decimal import Decimal
from uuid import uuid4
from tradeapp.domain.models import OrderRequest, OrderResult
@dataclass
class SandboxExecutionAdapter:
    fill_price: Decimal = Decimal("100")
    def submit_order(self, request: OrderRequest) -> OrderResult:
        if request.quantity <= 0: raise ValueError("quantity must be positive")
        return OrderResult(f"sandbox-{uuid4().hex[:12]}",request.symbol,request.side,request.quantity,"filled",self.fill_price)
