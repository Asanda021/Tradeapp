from dataclasses import dataclass
from decimal import Decimal
@dataclass(frozen=True)
class PersianSessionReport:
    symbol:str
    decision:str
    confidence:Decimal
    reasons:tuple[str,...]
    pnl:Decimal
class PersianReport:
    def render(self,report:PersianSessionReport)->str:
        lines=["گزارش جلسه معامله","================","نماد: "+report.symbol,"تصمیم: "+report.decision,"میزان اطمینان: "+f"{report.confidence:.2%}","سود/زیان: "+str(report.pnl),"دلایل:"]
        lines.extend("• "+r for r in report.reasons)
        lines.append("معاملات واقعی: فعلاً غیرفعال")
        return "\n".join(lines)
