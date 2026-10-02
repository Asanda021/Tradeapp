from dataclasses import dataclass

@dataclass(frozen=True)
class CredentialPolicy:
    allow_trading: bool = True
    allow_withdrawal: bool = False

    def validate(self) -> None:
        if self.allow_withdrawal:
            raise ValueError("Tradeapp must never require withdrawal permission")

@dataclass(frozen=True)
class CredentialReference:
    provider: str
    key_id: str
    fingerprint: str
    policy: CredentialPolicy

    def safe_for_trading(self) -> bool:
        self.policy.validate()
        return self.policy.allow_trading and not self.policy.allow_withdrawal
