# AIDO-AUDIT-CAV — Python GitHub Version

**Version:** 1.0.0  
**Date:** 2026-08-30

Public-facing reference implementation for the Final-Locked **AIDO-AUDIT-CAV v1.0**.

## Included

- CAV structural output-contract validation
- Practical 2 summary utilities
- Practical 3 controlled-challenge scoring
- P4B-E selective-audit scoring
- SHA-256 utilities
- manuscript/cover-letter reporting linter
- synthetic examples
- unit tests

## Deliberate public boundary

This GitHub package does **not** include real third-party evidence text, row-level Gold experimental data, contaminated/invalid runs, or private replay ledgers.

The code validates and scores frozen semantic outputs. It does **not** pretend deterministic Python can regenerate the blinded semantic LLM adjudications.

## Locked selective-audit interface

```text
determinate coverage                          1020/1215 = 83.95%
selective agreement among determinate outputs 967/1020 = 94.80%
explicit abstention                            195/1215 = 16.05%
determinate disagreement                        53/1215 = 4.36%
claim-ceiling violations                         0/1215
conservative full-denominator agreement         967/1215 = 79.59%
```

**Reporting rule:** `79.59%` must not appear alone at first appearance.  
The same first appearance must also expose `16.05%` abstention and `4.36%` determinate disagreement.

## Run

```bash
python -m unittest discover -s tests -v
python -m aido_cav.cli score-p4be examples/P4BE_SYNTHETIC_EXAMPLE.csv
python -m aido_cav.cli score-p3 examples/P3_SYNTHETIC_EXAMPLE.csv
python -m aido_cav.cli public-summary
```

No third-party runtime dependency is required.
