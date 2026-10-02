from dataclasses import dataclass
from datetime import datetime
from tradeapp.domain.time_control import RunSchedule

@dataclass
class RuntimeState:
    running: bool = False
    stopped_by_user: bool = False

class RuntimeController:
    def __init__(self, schedule: RunSchedule) -> None:
        self.schedule = schedule
        self.state = RuntimeState()
    def start(self, now: datetime) -> None:
        if not self.schedule.is_active(now):
            raise ValueError("scheduled start time has not been reached")
        self.state.running = True
        self.state.stopped_by_user = False
    def stop(self) -> None:
        self.state.running = False
        self.state.stopped_by_user = True
    def should_run(self, now: datetime) -> bool:
        return self.state.running and not self.state.stopped_by_user and self.schedule.is_active(now)
