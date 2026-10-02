from decimal import Decimal

from tradeapp.adapters.contracts import AccountPermissions, ConnectionState, AccountConnection
from tradeapp.adapters.sandbox import SandboxAccount
from tradeapp.execution.resilience import ExecutionGuard, RetryPolicy
from tradeapp.release.readiness import ReleaseEvidence
from tradeapp.release.rollout import RolloutPolicy, authorize_rollout
from tradeapp.security.credentials import CredentialPolicy, CredentialReference
from tradeapp.ui.control_model import build_session_view

def test_release_evidence_keeps_live_locked():
    evidence = ReleaseEvidence(True, True, True, True, True, True)
    assert evidence.ready_for_controlled_rollout()
    assert evidence.live_enabled is False

def test_sandbox_account_has_no_withdrawal_permission():
    account = SandboxAccount()
    assert account.connection().can_trade()
    assert account.connection().permissions.withdrawal is False
    assert account.reserve(Decimal("10")) is True
    assert account.balance().free == Decimal("90")

def test_credential_policy_rejects_withdrawal():
    try:
        CredentialPolicy(allow_withdrawal=True).validate()
        assert False
    except ValueError:
        pass
    ref = CredentialReference("demo", "key-1", "fp", CredentialPolicy())
    assert ref.safe_for_trading()

def test_disconnect_requires_reconciliation():
    guard = ExecutionGuard().after_disconnect()
    assert guard.permits_new_order() is False
    assert guard.reconciliation_required is True

def test_retry_policy_is_bounded():
    assert RetryPolicy(2).max_attempts == 2

def test_ui_only_starts_sandbox():
    assert build_session_view(True, True, False).can_start
    assert not build_session_view(True, False, False).can_start

def test_rollout_requires_evidence():
    policy = RolloutPolicy()
    assert authorize_rollout(policy, False, False).allowed is False
    assert authorize_rollout(policy, True, False).allowed is True
