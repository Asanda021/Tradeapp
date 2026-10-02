from hashlib import sha256
class SecretStore:
    def __init__(self): self._digests: dict[str,str] = {}
    def store(self, name: str, secret: str) -> None:
        if not secret: raise ValueError("secret must not be empty")
        self._digests[name] = sha256(secret.encode()).hexdigest()
    def has(self, name: str) -> bool: return name in self._digests
