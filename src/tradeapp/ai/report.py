from dataclasses import dataclass
@dataclass(frozen=True)
class SessionReport:
    decision: str
    confidence: float
    reasons: tuple[str, ...]
class LocalReportAI:
    def explain(self, decision: str, confidence: float, reasons: list[str]) -> SessionReport:
        return SessionReport(decision, confidence, tuple(reasons))
