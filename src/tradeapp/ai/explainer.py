from dataclasses import dataclass
from tradeapp.strategy.council import CouncilDecision
from tradeapp.strategy.signals import Signal

@dataclass(frozen=True)
class Explanation:
    title: str
    text: str

class LocalExplainer:
    """Rule-based, zero-API-cost explanation layer. No paid AI service required."""
    def explain(self,decision:CouncilDecision)->Explanation:
        if decision.signal is Signal.BUY:
            title="سیگنال خرید"
            text=f"چند شاخص هم‌جهت شده‌اند؛ میزان توافق {decision.agreement:.0%} است."
        elif decision.signal is Signal.SELL:
            title="سیگنال فروش"
            text=f"سیگنال‌های نزولی غالب‌اند؛ میزان توافق {decision.agreement:.0%} است."
        else:
            title="عدم معامله"
            text="سیگنال‌ها برای ورود کافی و هم‌جهت نیستند؛ فعلاً صبر."
        return Explanation(title,text)
