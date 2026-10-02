from dataclasses import dataclass
@dataclass(frozen=True)
class ReleaseCandidateGate:
    tests_green:bool
    main_verified:bool
    security_audit_passed:bool
    live_locked:bool
    required_evidence:int=0
    def passed(self)->bool:
        return self.tests_green and self.main_verified and self.security_audit_passed and self.live_locked and self.required_evidence>=1
