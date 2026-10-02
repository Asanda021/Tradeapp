"""Evidence intake and verification rules.

The registry intentionally refuses to promote CI/build evidence to real-world
evidence. A real-world record must identify its gate, source, artifact and
verification state.
"""

from dataclasses import dataclass

from tradeapp.validation.evidence_policy import REAL_WORLD_GATES


@dataclass(frozen=True)
class EvidenceRecord:
    gate: str
    source: str
    artifact: str
    verified: bool = False

    @property
    def real_world(self) -> bool:
        return self.source == "real_world" and bool(self.artifact) and self.verified


def validate_record(record: EvidenceRecord) -> bool:
    return record.gate in REAL_WORLD_GATES and record.real_world


def missing_gates(records: list[EvidenceRecord]) -> tuple[str, ...]:
    valid = {r.gate for r in records if validate_record(r)}
    return tuple(gate for gate in REAL_WORLD_GATES if gate not in valid)
