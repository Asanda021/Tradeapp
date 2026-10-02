from dataclasses import dataclass
@dataclass(frozen=True)
class ReleaseReport:
    version:str
    implemented_phases:tuple[int,...]
    ci_green:bool
    merged:bool
    main_verified:bool
    evidence_gaps:tuple[str,...]
    live_locked:bool=True
    def ready_for_controlled_live(self)->bool:
        return self.ci_green and self.merged and self.main_verified and not self.evidence_gaps and self.live_locked
