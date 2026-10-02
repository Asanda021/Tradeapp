from dataclasses import dataclass
@dataclass(frozen=True)
class Alert:
    level: str
    message: str
class AlertManager:
    def risk(self,message:str)->Alert: return Alert("risk",message)
    def error(self,message:str)->Alert: return Alert("error",message)
    def info(self,message:str)->Alert: return Alert("info",message)
