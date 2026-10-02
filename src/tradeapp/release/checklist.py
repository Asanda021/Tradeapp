from dataclasses import dataclass
@dataclass(frozen=True)
class ReleaseEvidence:
    sandbox:bool=False
    paper:bool=False
    shadow:bool=False
    android:bool=False
    windows:bool=False
    security:bool=False
    def count(self)->int:return sum(vars(self).values())
    def summary(self)->dict:return vars(self).copy()
@dataclass(frozen=True)
class ReleaseChecklist:
    code_implemented:bool
    ci_green:bool
    merged:bool
    main_ci_green:bool
    evidence:ReleaseEvidence
    def status(self)->str:
        if not (self.code_implemented and self.ci_green and self.merged and self.main_ci_green): return "NOT_RELEASE_CANDIDATE"
        return "RC_WITH_EVIDENCE_GAPS" if self.evidence.count()<6 else "RC_EVIDENCE_COMPLETE"
