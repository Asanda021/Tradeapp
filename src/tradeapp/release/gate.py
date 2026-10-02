from dataclasses import dataclass
@dataclass(frozen=True)
class ReleaseGate:
    tests_green: bool
    paper_validated: bool
    security_reviewed: bool
    live_enabled: bool=False
    def can_enable_live(self)->bool: return self.tests_green and self.paper_validated and self.security_reviewed and self.live_enabled
