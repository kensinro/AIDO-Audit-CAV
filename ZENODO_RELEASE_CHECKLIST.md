# Zenodo release checklist — AIDO-AUDIT-CAV v1.0.0

This repository is prepared for a GitHub → Zenodo software archive.

## Before creating the GitHub release

1. **License gate: PASS — Apache-2.0.** Confirm `LICENSE`, `CITATION.cff`, `.zenodo.json`, and `pyproject.toml` remain synchronized.
2. Confirm `main` tests pass:
   ```bash
   python -m unittest discover -s tests -v
   python reproducibility/recompute_frozen_endpoints.py
   ```
3. Confirm `PACKAGE_MANIFEST_SHA256.csv` matches the release tree.
4. Enable this repository in the Zenodo GitHub integration.
5. Create the GitHub release/tag exactly as `v1.0.0`.
6. Confirm the resulting Zenodo software record describes **software**, not a data archive.
7. Record the Zenodo DOI in the CAV controlled metadata patch only after the DOI actually exists.

## Archive separation

- GitHub / Zenodo: executable source, tests, frozen aggregate endpoint inputs, release metadata.
- Dryad: manuscript-linked data/audit artifacts and reproducibility objects where appropriate.
- Restricted third-party article content is not redistributed unless the original license permits it.

## Claim boundary

This software validates and scores governed output contracts. It does not establish scientific truth,
universal accuracy, clinical validity, autonomous evidence retrieval, or language-model vendor invariance.
