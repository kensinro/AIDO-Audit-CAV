# Reproducibility layer

This directory contains **aggregate frozen endpoint objects and governance summaries** that can be redistributed
without exposing restricted third-party evidence text or pretending that deterministic code can regenerate
the original blinded semantic adjudications.

The core package in `aido_cav/` remains the public reference/scoring implementation.

## Included

- `frozen_endpoints.json` — manuscript-authorized aggregate P1–P4 counts and claim boundaries.
- `P2_INFORMATION_BARRIERS.csv` — frozen permitted/prohibited information classes for the three ablation arms.
- `P2_HOLD_CHRONOLOGY.csv` — the two preserved contaminated Arm-C attempts, both with zero claim-level verdicts.
- `recompute_frozen_endpoints.py` — standard-library-only check that recomputes the reported P3/P4 percentages
  and enforces the non-equivalent P2 semantics.

## Important

Arm B is **not** converted into an EEA terminal-action distribution.
The two Arm-C HOLD attempts are provenance events, not packet/scientific failures.
P3 remains 11/12, not 12/12.
P4 selective agreement is 967/1020 among determinate outputs, not overall accuracy.
