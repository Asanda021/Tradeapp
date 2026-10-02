from dataclasses import dataclass
@dataclass(frozen=True)
class PaperRun:
    sessions:int
    trades:int
    pnl:float
    completed:bool
class LongPaperValidator:
    def validate(self,sessions:int,trades:int,pnl:float)->PaperRun:
        if sessions<1: raise ValueError("sessions must be positive")
        return PaperRun(sessions,trades,pnl,True)
