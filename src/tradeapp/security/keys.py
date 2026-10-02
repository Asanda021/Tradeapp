from dataclasses import dataclass
from hashlib import sha256
@dataclass(frozen=True)
class ApiKeyRecord:
    provider:str
    key_fingerprint:str
    can_trade:bool=True
    can_withdraw:bool=False
class KeyPolicy:
    @staticmethod
    def fingerprint(secret:str)->str:
        if not secret: raise ValueError('secret must not be empty')
        return sha256(secret.encode()).hexdigest()
    @staticmethod
    def validate(record:ApiKeyRecord)->None:
        if record.can_withdraw: raise ValueError('withdrawal permission is prohibited')
