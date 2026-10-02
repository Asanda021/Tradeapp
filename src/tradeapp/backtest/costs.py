from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class ExecutionCostModel:
    fee_rate: Decimal = Decimal('0.001')
    slippage_rate: Decimal = Decimal('0.0005')
    def buy_price(self, price: Decimal) -> Decimal: return price*(Decimal('1')+self.slippage_rate)
    def sell_price(self, price: Decimal) -> Decimal: return price*(Decimal('1')-self.slippage_rate)
    def fee(self, notional: Decimal) -> Decimal: return abs(notional)*self.fee_rate
