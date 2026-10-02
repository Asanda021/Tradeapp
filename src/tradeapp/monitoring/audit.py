from dataclasses import dataclass
from datetime import datetime, timezone
@dataclass(frozen=True)
class AuditEvent:
    action: str
    detail: str
    timestamp: datetime
class AuditLog:
    def __init__(self) -> None: self.events: list[AuditEvent] = []
    def record(self, action: str, detail: str) -> AuditEvent:
        event=AuditEvent(action,detail,datetime.now(timezone.utc)); self.events.append(event); return event
