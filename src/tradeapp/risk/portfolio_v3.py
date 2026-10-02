from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class PortfolioLimits:
    max_position:Decimal=Decimal(".10")
    max_total_exposure:Decimal=Decimal(".20")
    max_daily_loss:Decimal=Decimal(".05")
    max_trades:int=10
@dataclass(frozen=True)
class PortfolioDecision:
    allowed:bool
    quantity:Decimal
    reason:str
class PortfolioRiskEngine:
    def check(self,equity:Decimal,position:Decimal,total_exposure:Decimal,daily_loss:Decimal,trades:int,requested:Decimal,limits:PortfolioLimits=PortfolioLimits())->PortfolioDecision:
        if equity<=0:return PortfolioDecision(False,Decimal("0"),"invalid equity")
        if position+requested/equity>limits.max_position:return PortfolioDecision(False,Decimal("0"),"position limit")
        if total_exposure+requested/equity>limits.max_total_exposure:return PortfolioDecision(False,Decimal("0"),"portfolio exposure limit")
        if daily_loss>=limits.max_daily_loss:return PortfolioDecision(False,Decimal("0"),"daily loss limit")
        if trades>=limits.max_trades:return PortfolioDecision(False,Decimal("0"),"trade count limit")
        return PortfolioDecision(True,requested,"risk limits passed")
