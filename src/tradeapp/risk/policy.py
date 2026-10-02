from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class RiskPolicy:
    max_trade_fraction:Decimal=Decimal('.02')
    max_daily_loss:Decimal=Decimal('.05')
    max_exposure:Decimal=Decimal('.20')
    max_consecutive_losses:int=3
@dataclass(frozen=True)
class RiskDecision:
    allowed:bool
    reason:str
    quantity:Decimal
class RiskEngine:
    def approve(self,equity:Decimal,available:Decimal,requested:Decimal,daily_loss:Decimal,exposure:Decimal,consecutive_losses:int,policy:RiskPolicy=RiskPolicy())->RiskDecision:
        if equity<=0 or available<=0:return RiskDecision(False,'invalid account state',Decimal('0'))
        if daily_loss>=policy.max_daily_loss:return RiskDecision(False,'daily loss limit reached',Decimal('0'))
        if exposure>=policy.max_exposure:return RiskDecision(False,'exposure limit reached',Decimal('0'))
        if consecutive_losses>=policy.max_consecutive_losses:return RiskDecision(False,'consecutive-loss stop reached',Decimal('0'))
        quantity=min(requested,equity*policy.max_trade_fraction)
        return RiskDecision(quantity>0,'risk limits passed' if quantity>0 else 'requested quantity is zero',quantity)
