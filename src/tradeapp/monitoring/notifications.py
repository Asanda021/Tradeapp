from dataclasses import dataclass
@dataclass(frozen=True)
class Notification:
    level:str
    message:str
class NotificationCenter:
    def __init__(self): self.items:list[Notification]=[]
    def publish(self,level:str,message:str)->Notification:
        n=Notification(level,message); self.items.append(n); return n
