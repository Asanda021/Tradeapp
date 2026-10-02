from dataclasses import dataclass
@dataclass(frozen=True)
class FailureCase:
    name:str
    passed:bool
@dataclass(frozen=True)
class E2EReport:
    cases:tuple[FailureCase,...]
    def passed(self)->bool: return bool(self.cases) and all(c.passed for c in self.cases)
class E2ERunner:
    def evaluate(self,cases:list[FailureCase])->E2EReport: return E2EReport(tuple(cases))
