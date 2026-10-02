from dataclasses import dataclass
from decimal import Decimal
from tradeapp.adapters.contracts import (
    AccountConnection, AccountPermissions, Balance, ConnectionState,
)

@dataclass
class SandboxAccount:
    provider: str = "sandbox"
    account_id: str = "paper-account"
    cash: Decimal = Decimal("100")

    def connection(self) -> AccountConnection:
        return AccountConnection(
            self.provider,
            self.account_id,
            True,
            AccountPermissions(trading=True, withdrawal=False),
            ConnectionState.CONNECTED,
        )

    def balance(self) -> Balance:
        return Balance("USD", self.cash)

    def reserve(self, amount: Decimal) -> bool:
        if amount <= 0 or amount > self.cash:
            return False
        self.cash -= amount
        return True
