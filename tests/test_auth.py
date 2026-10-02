from tradeapp.domain.auth import AuthIdentity, AuthProvider, AuthService, AuthError

def test_verified_google_identity_is_accepted():
    identity = AuthIdentity("google-sub", "user@example.com", AuthProvider.GOOGLE, True)
    assert AuthService().accept_verified_identity(identity) == identity

def test_unverified_identity_is_rejected():
    identity = AuthIdentity("google-sub", "user@example.com", AuthProvider.GOOGLE, False)
    try:
        AuthService().accept_verified_identity(identity)
    except AuthError:
        return
    raise AssertionError("expected AuthError")
