from dataclasses import dataclass
from enum import Enum

class AuthProvider(str, Enum):
    PASSWORD = "password"
    GOOGLE = "google"

@dataclass(frozen=True)
class AuthIdentity:
    subject: str
    email: str
    provider: AuthProvider
    email_verified: bool

class AuthError(ValueError):
    pass

class AuthService:
    """Provider-neutral auth contract; OAuth verification stays at the edge."""
    def accept_verified_identity(self, identity: AuthIdentity) -> AuthIdentity:
        if not identity.email_verified:
            raise AuthError("A verified email is required.")
        if "@" not in identity.email:
            raise AuthError("Invalid email.")
        return identity
