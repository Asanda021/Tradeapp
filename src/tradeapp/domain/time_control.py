from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

@dataclass(frozen=True)
class RunSchedule:
    start_at: datetime
    duration: Optional[timedelta] = None
    end_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        if self.duration is not None and self.duration.total_seconds() <= 0:
            raise ValueError("duration must be positive")
        if self.end_at is not None and self.end_at < self.start_at:
            raise ValueError("end_at cannot be before start_at")
        if self.duration is not None and self.end_at is not None and self.start_at + self.duration != self.end_at:
            raise ValueError("duration and end_at must describe the same window")

    def is_active(self, now: datetime) -> bool:
        if now < self.start_at:
            return False
        end = self.end_at or (self.start_at + self.duration if self.duration else None)
        return end is None or now <= end
