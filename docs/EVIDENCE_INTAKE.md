# Real-world evidence intake

A gate is considered verified only when its evidence record has:
1. the exact campaign gate key;
2. source = `real_world`;
3. a non-empty artifact/reference;
4. verified = true.

CI, unit tests, build artifacts, screenshots generated only by CI, or simulated
exchange responses cannot be promoted to real-world evidence.

This registry is deliberately conservative so the live gate cannot be opened
by accidentally relabelling automated evidence.
