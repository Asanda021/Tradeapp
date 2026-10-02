from dataclasses import dataclass

@dataclass(frozen=True)
class RolloutPolicy:
    sandbox_only: bool = True
    max_notional: float = 0.0
    manual_approval: bool = True
    emergency_stop_required: bool = True

    def validate(self) -> None:
        if self.max_notional < 0:
            raise ValueError("max_notional must not be negative")
        if not self.sandbox_only and self.max_notional == 0:
            raise ValueError("non-sandbox rollout needs an explicit cap")

@dataclass(frozen=True)
class RolloutDecision:
    allowed: bool
    reason: str

def authorize_rollout(policy: RolloutPolicy, evidence_ready: bool, approved: bool) -> RolloutDecision:
    policy.validate()
    if not evidence_ready:
        return RolloutDecision(False, "release evidence is incomplete")
    if policy.sandbox_only:
        return RolloutDecision(True, "sandbox rollout permitted")
    if not approved:
        return RolloutDecision(False, "manual approval required")
    if not policy.emergency_stop_required:
        return RolloutDecision(False, "emergency stop is mandatory")
    return RolloutDecision(True, "controlled rollout permitted")
