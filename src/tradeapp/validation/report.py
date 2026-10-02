"""Deterministic validation report without inventing real-world evidence."""

from dataclasses import dataclass

from tradeapp.validation.acceptance import AcceptanceCampaign, default_campaign

@dataclass(frozen=True)
class ValidationReport:
    status: str
    automated_missing: tuple[str, ...]
    real_world_missing: tuple[str, ...]
    live_locked: bool = True

def build_report(campaign: AcceptanceCampaign | None = None) -> ValidationReport:
    campaign = campaign or default_campaign()
    automated_missing = tuple(
        item.key for item in campaign.items if item.automated and not item.verified
    )
    real_world_missing = tuple(
        item.key for item in campaign.items if item.real_world_required and not item.verified
    )
    return ValidationReport(
        status=campaign.status(),
        automated_missing=automated_missing,
        real_world_missing=real_world_missing,
        live_locked=True,
    )
