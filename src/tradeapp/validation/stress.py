from dataclasses import dataclass
@dataclass(frozen=True)
class StressCase:
 name:str; passed:bool
@dataclass(frozen=True)
class StressReport:
 cases:tuple[StressCase,...]
 def passed(self): return bool(self.cases) and all(c.passed for c in self.cases)
class StressRunner:
 def evaluate(self,cases:list[StressCase]): return StressReport(tuple(cases))
