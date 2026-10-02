from dataclasses import dataclass
@dataclass(frozen=True)
class LocalAIReport:
    summary:str
    reasons:tuple[str,...]
    confidence:float
class LocalAI:
    def explain(self, decision:str, reasons:tuple[str,...], confidence:float)->LocalAIReport:
        return LocalAIReport(decision,reasons,max(0.0,min(1.0,confidence)))
