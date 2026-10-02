from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

class ConnectionState(str, Enum):
    DISCONNECTED = "disconnected"
    CONNECTED = "connected"
    DEGRADED = "degraded"

@dataclass(frozen=True)
class AccountPermissions:
    trading: bool
    withdrawal: bool = False

@dataclass(frozen=True)
class AccountConnection:
    provider: str
    account_id: str
    sandbox: bool
    permissions: AccountPermissions
    state: ConnectionState = ConnectionState.DISCONNECTED

    def can_trade(self) -> bool:
        return self.permissions.trading and not self.permissions.withdrawal and self.state == ConnectionState.CONNECTED

@dataclass(frozen=True)
class Balance:
    asset: str
    free: Decimal
    locked: Decimal = Decimal("0")
