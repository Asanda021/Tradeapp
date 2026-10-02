from decimal import Decimal
from tradeapp.validation.e2e_runner import E2ETradeFlow
from tradeapp.monitoring.stress_v2 import StressSuite
from tradeapp.ui.app_model import AppController
from tradeapp.report.persian import PersianReport,PersianSessionReport
from tradeapp.decision.engine import Decision
from tradeapp.strategy.signals import Signal
def test_e2e_flow(): assert E2ETradeFlow().run(True,True,True,True,True).passed
def test_stress(): assert StressSuite().run([("disconnect",True),("bad_quote",True)]).passed_all
def test_ui_model():
    d=Decision(Signal.HOLD,Decimal(".4"),("داده کافی نیست",))
    assert AppController().build("connected","BTCUSDT",Decimal("100"),d).decision=="hold"
def test_persian_report():
    text=PersianReport().render(PersianSessionReport("BTCUSDT","hold",Decimal(".4"),("شرایط نامشخص",),Decimal("0")))
    assert "گزارش جلسه معامله" in text and "معاملات واقعی" in text
