from decimal import Decimal
from tradeapp.validation.data_quality import DataQuality
from tradeapp.validation.walk_forward_v2 import build_windows,WalkForwardReport
from tradeapp.validation.monte_carlo_v2 import simulate
from tradeapp.strategy.robust_lab import RobustStrategyLab,CandidateEvidence
from tradeapp.news.intelligence import NewsIntelligence,NewsSignal
from tradeapp.risk.portfolio_v3 import PortfolioRiskEngine
from tradeapp.execution.retry import RetryGuard
from tradeapp.ai.benchmark import LocalAIBenchmark
from tradeapp.ai.local_runtime import LocalModelRuntime
from tradeapp.security.audit import SecurityAudit
from tradeapp.ui.session_model import SessionController,SessionState,SessionAction

def test_data_walkforward_montecarlo():
    assert DataQuality(1000,1,1,1).acceptable()
    assert len(build_windows(100,50,10,10))==5
    assert WalkForwardReport(10,7,(Decimal("1"),)).passed()
    assert simulate([Decimal("1"),Decimal("-1")],10)["iterations"]==10
def test_strategy_news_risk():
    c=[CandidateEvidence("x",Decimal(".1"),Decimal(".8"),Decimal(".1"),40)]
    assert RobustStrategyLab().filter(c)
    assert NewsIntelligence().assess([NewsSignal("BTC",1,.9,.9,1,1,"test")],"BTC")>.8
    assert PortfolioRiskEngine().check(Decimal("100"),Decimal("0"),Decimal("0"),Decimal("0"),0,Decimal("5")).allowed
def test_retry_ai_security_ui():
    n=[0]
    def op():
        n[0]+=1
        if n[0]<2: raise ConnectionError()
        return "ok"
    assert RetryGuard().run(op)=="ok"
    assert LocalAIBenchmark().run(LocalModelRuntime(),["x"]).passed==1
    assert all(x.passed for x in SecurityAudit().run("k",False,False))
    state=SessionController().transition(SessionState(),SessionAction.START)
    assert state.status=="در حال اجرا"
