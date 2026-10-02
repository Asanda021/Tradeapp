from dataclasses import dataclass
@dataclass(frozen=True)
class SecurityCheck:
 name:str; passed:bool
@dataclass(frozen=True)
class SecurityReport:
 checks:tuple[SecurityCheck,...]
 def passed(self): return bool(self.checks) and all(c.passed for c in self.checks)
class SecuritySuite:
 def evaluate(self,checks:list[SecurityCheck]): return SecurityReport(tuple(checks))
