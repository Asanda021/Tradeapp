from dataclasses import dataclass
from time import monotonic
from tradeapp.ai.local_runtime import LocalModelRuntime
@dataclass(frozen=True)
class ModelBenchmark:
    model:str
    cases:int
    passed:int
    seconds:float
    @property
    def pass_rate(self)->float:return self.passed/self.cases if self.cases else 0.0
class LocalAIBenchmark:
    def run(self,runtime:LocalModelRuntime,cases:list[str])->ModelBenchmark:
        start=monotonic(); passed=0
        for prompt in cases:
            result=runtime.generate(prompt)
            if result.text: passed+=1
        return ModelBenchmark(runtime.command or "deterministic",len(cases),passed,monotonic()-start)
