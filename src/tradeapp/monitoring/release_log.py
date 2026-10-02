from dataclasses import dataclass,field
from datetime import datetime,timezone
@dataclass
class ReleaseAuditLog:
    events:list[tuple[str,str]]=field(default_factory=list)
    def record(self,event:str,detail:str)->None:self.events.append((event,detail))
    def export(self)->tuple[tuple[str,str],...]:return tuple(self.events)
