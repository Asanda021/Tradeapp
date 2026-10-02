from dataclasses import dataclass, field

@dataclass(frozen=True)
class AcceptanceItem:
    key: str
    title: str
    automated: bool
    real_world_required: bool
    verified: bool = False
    evidence: str = ""

@dataclass
class AcceptanceCampaign:
    items: list[AcceptanceItem] = field(default_factory=list)

    def add(self, item: AcceptanceItem) -> None:
        self.items.append(item)

    @property
    def automated_passed(self) -> bool:
        return all((not i.automated) or i.verified for i in self.items)

    @property
    def real_world_complete(self) -> bool:
        return all((not i.real_world_required) or i.verified for i in self.items)

    def status(self) -> str:
        if self.real_world_complete:
            return "REAL_WORLD_VALIDATED"
        if self.automated_passed:
            return "AUTOMATED_VALIDATION_COMPLETE_REAL_EVIDENCE_MISSING"
        return "VALIDATION_INCOMPLETE"

    def report(self) -> dict:
        return {"status": self.status(), "items": [
            {"key": i.key, "title": i.title, "verified": i.verified,
             "automated": i.automated, "real_world_required": i.real_world_required,
             "evidence": i.evidence} for i in self.items]}

def default_campaign() -> AcceptanceCampaign:
    titles = (
        ("01_sandbox_connection", "Sandbox exchange connection"),
        ("02_market_data", "Real market data stability"),
        ("03_paper", "Long-running paper trading"),
        ("04_shadow", "Long-running shadow trading"),
        ("05_backtest", "Real multi-market backtest"),
        ("06_walk_forward", "Real walk-forward and Monte Carlo"),
        ("07_local_ai", "Real local AI benchmark"),
        ("08_news", "Real multi-source news intelligence"),
        ("09_recovery", "Network/crash/order recovery"),
        ("10_security", "Production security audit"),
        ("11_windows", "Windows build, install and UX validation"),
        ("12_android", "Android APK, install and UX validation"),
        ("13_e2e", "End-to-end application flow validation"),
        ("14_release_evidence", "Release evidence completeness"),
        ("15_controlled_live", "Controlled-live preflight gate"),
    )
    c = AcceptanceCampaign()
    for key, title in titles:
        c.add(AcceptanceItem(key, title, True, True))
    return c
