from dataclasses import dataclass
@dataclass(frozen=True)
class LocalModelPolicy:
 provider:str="none"; paid_api_required:bool=False; allow_network:bool=False
 def is_free_first(self): return not self.paid_api_required
