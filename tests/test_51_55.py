from decimal import Decimal
from tradeapp.validation.stress import StressCase,StressRunner
from tradeapp.validation.security_suite import SecurityCheck,SecuritySuite
from tradeapp.ai.model_policy import LocalModelPolicy
from tradeapp.ai.decision_explainer import DecisionExplainer
from tradeapp.strategy.lab_v2 import StrategyCandidate,StrategyLabV2
def test_validation():
 assert StressRunner().evaluate([StressCase("disconnect",True)]).passed(); assert SecuritySuite().evaluate([SecurityCheck("no_withdrawal",True)]).passed()
def test_ai_policy():
 assert LocalModelPolicy().is_free_first() and not LocalModelPolicy().allow_network; assert DecisionExplainer().explain("HOLD",.7,("low agreement",)).confidence==.7
def test_lab():
 c=(StrategyCandidate("A","trend",Decimal("1"),Decimal("2")),StrategyCandidate("B","momentum",Decimal("2"),Decimal("1"))); assert StrategyLabV2().rank(c)[0].name=="A"
