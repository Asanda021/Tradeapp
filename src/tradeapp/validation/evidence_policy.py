"""Evidence policy for separating CI/build evidence from real-world validation."""

from dataclasses import dataclass

REAL_WORLD_GATES = (
    "sandbox",
    "market_data",
    "paper",
    "shadow",
    "backtest",
    "walk_forward",
    "local_ai",
    "news",
    "recovery",
    "security",
    "windows",
    "android",
    "e2e",
    "release_evidence",
    "controlled_live",
)

@dataclass(frozen=True)
class EvidenceStatus:
    gate: str
    verified: bool
    source: str
    note: str

def validate_real_world_evidence(statuses: tuple[EvidenceStatus, ...]) -> tuple[str, ...]:
    by_gate = {item.gate: item for item in statuses}
    return tuple(
        gate for gate in REAL_WORLD_GATES
        if gate not in by_gate or not by_gate[gate].verified or by_gate[gate].source != "real_world"
    )
