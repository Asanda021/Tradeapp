"""Optional encrypted-at-rest secret storage using cryptography when installed."""
from dataclasses import dataclass
import hashlib,os
@dataclass(frozen=True)
class EncryptedSecret:
    nonce:bytes
    ciphertext:bytes
class EncryptedSecretStore:
    def __init__(self,master_key:bytes):
        if len(master_key)<32: raise ValueError("master key must be at least 32 bytes")
        self._key=hashlib.sha256(master_key).digest(); self._data={}
    def put(self,name:str,secret:str)->None:
        if not name or not secret: raise ValueError("name and secret are required")
        try:
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        except ImportError as exc: raise RuntimeError("cryptography package is required") from exc
        nonce=os.urandom(12); cipher=AESGCM(self._key).encrypt(nonce,secret.encode(),name.encode())
        self._data[name]=EncryptedSecret(nonce,cipher)
    def get(self,name:str)->str:
        try:
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        except ImportError as exc: raise RuntimeError("cryptography package is required") from exc
        item=self._data[name]
        return AESGCM(self._key).decrypt(item.nonce,item.ciphertext,name.encode()).decode()
