from dataclasses import dataclass
@dataclass(frozen=True)
class ProductionChecklist:
    ci_green: bool
    paper_validated: bool
    shadow_validated: bool
    security_validated: bool
    risk_validated: bool
    ui_validated: bool
    documentation_ready: bool
    critical_issues: int = 0
    def ready(self) -> bool:
        return all((self.ci_green,self.paper_validated,self.shadow_validated,self.security_validated,self.risk_validated,self.ui_validated,self.documentation_ready)) and self.critical_issues == 0
