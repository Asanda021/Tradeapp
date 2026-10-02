from dataclasses import dataclass
from datetime import datetime,timedelta
from tradeapp.domain.time_control import RunSchedule
from tradeapp.application.runtime import RuntimeController
@dataclass(frozen=True)
class SessionConfig:
    start_at:datetime
    duration_seconds:int|None=None
class SessionService:
    def controller(self,config:SessionConfig)->RuntimeController:
        duration=timedelta(seconds=config.duration_seconds) if config.duration_seconds else None
        return RuntimeController(RunSchedule(config.start_at,duration=duration))
