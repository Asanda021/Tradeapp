from dataclasses import dataclass
@dataclass(frozen=True)
class FinalGate:
    tests_green:bool
    paper_passed:bool
    shadow_passed:bool
    security_passed:bool
    e2e_passed:bool
    critical_issues:int=0
    def ready(self)->bool:
        return all((self.tests_green,self.paper_passed,self.shadow_passed,self.security_passed,self.e2e_passed)) and self.critical_issues==0
