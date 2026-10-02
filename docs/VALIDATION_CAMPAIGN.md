# Tradeapp validation campaign

The campaign now contains 15 gates. Automated tests and real-world evidence are deliberately separated.

## Gates 1-10
1. Sandbox exchange connection
2. Real market-data stability
3. Long-running paper trading
4. Long-running shadow trading
5. Multi-market backtest with real data
6. Walk-forward + Monte Carlo with real data
7. Local AI benchmark
8. Multi-source news intelligence
9. Network/crash/order recovery
10. Production security audit

## Gates 11-15
11. Windows build/install/UX validation
12. Android APK/install/UX validation
13. End-to-end application flow validation
14. Release evidence completeness
15. Controlled-live preflight

A unit test does not count as real-world evidence. Gates 11-15 remain unverified until the required build, device, environment, sandbox, and operational evidence is actually collected. Live trading remains locked.
