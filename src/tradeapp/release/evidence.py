from dataclasses import dataclass

@dataclass(frozen=True)
class EvidenceRecord:
    key: str
    verified: bool = False
    artifact: str = ""
    note: str = ""

@dataclass(frozen=True)
class EvidenceLedger:
    records: tuple[EvidenceRecord, ...]

    def missing(self) -> tuple[str, ...]:
        return tuple(r.key for r in self.records if not r.verified)

    def complete(self) -> bool:
        return not self.missing()

    def summary(self) -> dict:
        return {
            "total": len(self.records),
            "verified": sum(r.verified for r in self.records),
            "missing": self.missing(),
            "complete": self.complete(),
        }
