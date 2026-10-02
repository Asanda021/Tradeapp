from dataclasses import dataclass

@dataclass(frozen=True)
class ReleaseEvidence:
    tests_green: bool
    paper_validated: bool
    shadow_validated: bool
    security_reviewed: bool
    e2e_validated: bool
    sandbox_validated: bool
    critical_issues: int = 0
    live_enabled: bool = False

    def ready_for_controlled_rollout(self) -> bool:
        return (
            all((
                self.tests_green,
                self.paper_validated,
                self.shadow_validated,
                self.security_reviewed,
                self.e2e_validated,
                self.sandbox_validated,
            ))
            and self.critical_issues == 0
            and not self.live_enabled
        )
