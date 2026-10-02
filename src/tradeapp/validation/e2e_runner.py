from dataclasses import dataclass
@dataclass(frozen=True)
class E2EStep:
    name:str
    passed:bool
    detail:str=""
@dataclass(frozen=True)
class E2EResult:
    steps:tuple[E2EStep,...]
    @property
    def passed(self)->bool: return all(x.passed for x in self.steps)
class E2ETradeFlow:
    def run(self,connected:bool,market_data:bool,decision:bool,paper_execution:bool,report:bool)->E2EResult:
        return E2EResult((E2EStep("account_connection",connected),E2EStep("market_data",market_data),E2EStep("decision",decision),E2EStep("paper_execution",paper_execution),E2EStep("persian_report",report)))
