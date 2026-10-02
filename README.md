# Tradeapp

Free-first autonomous trading platform core for Windows and Android.

Current status:
- Phases 1-40: foundation implemented and CI-verified.
- Phases 40-45: controlled-readiness hardening.
- Real-money trading remains disabled by design.
- Sandbox/paper validation is supported; production trading requires separate real-world validation.

Safety principles:
- No withdrawal permission.
- Kill switch and manual stop.
- Reconciliation after connectivity failures.
- Bounded retry behavior.
- Release evidence before any controlled rollout.
