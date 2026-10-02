from dataclasses import dataclass
@dataclass(frozen=True)
class StressResult:
    cases:int
    passed:int
    failures:tuple[str,...]
    @property
    def passed_all(self)->bool: return self.cases==self.passed and not self.failures
class StressSuite:
    def run(self,cases:list[tuple[str,bool]])->StressResult:
        failures=tuple(name for name,ok in cases if not ok)
        return StressResult(len(cases),len(cases)-len(failures),failures)
