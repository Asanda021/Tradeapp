from dataclasses import dataclass
from hashlib import sha256
@dataclass(frozen=True)
class SecurityFinding:
    check:str
    passed:bool
    detail:str
class SecurityAudit:
    def run(self,api_key:str,withdrawal:bool,live_enabled:bool)->tuple[SecurityFinding,...]:
        return (
            SecurityFinding("secret_not_empty",bool(api_key),"credential presence"),
            SecurityFinding("withdrawal_disabled",not withdrawal,"withdrawal permission must remain disabled"),
            SecurityFinding("live_gate",not live_enabled,"live trading remains gated"),
        )
