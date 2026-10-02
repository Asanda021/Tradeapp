from decimal import Decimal
from tradeapp.backtest.professional import ProfessionalBacktest,TradeRecord
from tradeapp.validation.optimization import OptimizationResult,select_robust
from tradeapp.ai.local_runtime import LocalModelRuntime
from tradeapp.paper.long_run import PaperRun,LongPaperValidator
from tradeapp.shadow.validation import ShadowValidator,ShadowObservation

def test_professional_metrics_drawdown():
    m=ProfessionalBacktest().metrics(Decimal("100"),Decimal("95"),[TradeRecord(Decimal("2"),Decimal("102")),TradeRecord(Decimal("-7"),Decimal("95"))])
    assert m.max_drawdown>0

def test_optimization_filters_oos_and_stability():
    c=[OptimizationResult("a",Decimal("9"),Decimal("1"),Decimal(".1")),OptimizationResult("b",Decimal("8"),Decimal("3"),Decimal(".8"))]
    assert select_robust(c,Decimal("2"),Decimal(".5")).name=="b"

def test_local_runtime_is_free_by_default():
    r=LocalModelRuntime().generate("test"); assert r.used_fallback

def test_paper_and_shadow():
    run=PaperRun(Decimal("100"),Decimal("100")); run.record(Decimal("2"))
    assert LongPaperValidator().validate(run)
    s=ShadowValidator(); s.record(ShadowObservation("BTCUSDT","hold",Decimal(".4"),False,"test"))
    assert s.summary()["executed"]==0
