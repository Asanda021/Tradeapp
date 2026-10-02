from dataclasses import dataclass
from enum import Enum
class SessionAction(str,Enum):START="start";PAUSE="pause";RESUME="resume";STOP="stop";EMERGENCY_STOP="emergency_stop"
@dataclass(frozen=True)
class SessionState:
    status:str="آماده"
    action:SessionAction|None=None
    live:bool=False
class SessionController:
    def transition(self,state:SessionState,action:SessionAction)->SessionState:
        if action==SessionAction.START and state.live:return state
        if action==SessionAction.EMERGENCY_STOP:return SessionState("توقف اضطراری",action,False)
        labels={SessionAction.START:"در حال اجرا",SessionAction.PAUSE:"مکث",SessionAction.RESUME:"در حال اجرا",SessionAction.STOP:"متوقف"}
        return SessionState(labels[action],action,state.live)
