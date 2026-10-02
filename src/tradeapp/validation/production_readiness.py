from dataclasses import dataclass
@dataclass(frozen=True)
class ProductionReadiness:
    adapter_tested:bool; paper_tested:bool; shadow_tested:bool; recovery_tested:bool; security_tested:bool; critical_issues:int=0
    def passed(self): return all((self.adapter_tested,self.paper_tested,self.shadow_tested,self.recovery_tested,self.security_tested)) and self.critical_issues==0
