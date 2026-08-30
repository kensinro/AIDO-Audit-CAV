# AIDO-AUDIT-CAV — Python GitHub Version

**Version:** 1.0.0  
**Date:** 2026-08-30

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22179598.svg)](https://doi.org/10.5281/zenodo.22179598)

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

## Frozen reproducibility layer

Redistributable aggregate endpoint objects and governance summaries are provided in `reproducibility/`.
They preserve the P2 information-ablation semantics, the two contaminated Arm-C HOLD events, the P3 11/12 raw miss,
and the P4 denominator accounting without redistributing restricted third-party evidence text.

Run:

```bash
python reproducibility/recompute_frozen_endpoints.py
```

## Citation and software archive

- Software DOI: `10.5281/zenodo.22179598`
- Zenodo archive: https://doi.org/10.5281/zenodo.22179598
- `CITATION.cff` describes the software citation.
- `.zenodo.json` supplies Zenodo software metadata for GitHub-triggered archiving.
- `ZENODO_RELEASE_CHECKLIST.md` records the GitHub → Zenodo release gate.

The Zenodo DOI identifies the **software release**. It is distinct from the manuscript-linked Dryad data/audit-artifact archive and any future Dryad DOI.

## License

The source code and redistributable software/reproducibility utilities in this repository are released under the
**Apache License 2.0**. See `LICENSE`.

The license does not expand the redistribution rights of third-party source material. Restricted third-party evidence
text remains outside this repository unless its original license independently permits redistribution.
