from dataclasses import dataclass
from enum import Enum

class SessionAction(str, Enum):
    START = "start"
    PAUSE = "pause"
    RESUME = "resume"
    STOP = "stop"
    EMERGENCY_STOP = "emergency_stop"

@dataclass(frozen=True)
class SessionView:
    connected: bool
    sandbox: bool
    running: bool
    can_start: bool
    status_fa: str

def build_session_view(connected: bool, sandbox: bool, running: bool) -> SessionView:
    can_start = connected and sandbox and not running
    if not connected:
        status = "حساب متصل نیست"
    elif not sandbox:
        status = "حالت واقعی قفل است"
    elif running:
        status = "جلسه در حال اجراست"
    else:
        status = "آماده اجرای آزمایشی"
    return SessionView(connected, sandbox, running, can_start, status)
