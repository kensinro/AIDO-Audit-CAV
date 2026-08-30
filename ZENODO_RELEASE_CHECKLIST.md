# Zenodo release checklist — AIDO-AUDIT-CAV v1.0.0

This repository has completed the GitHub → Zenodo software archive workflow.

## Release status

1. Software license: **PASS — Apache-2.0**
2. `main` tests/reproducibility checks: **PASS before release**
3. `PACKAGE_MANIFEST_SHA256.csv`: synchronized to the release tree
4. Zenodo GitHub integration: **Enabled**
5. GitHub release/tag: **Published — `v1.0.0`**
6. Zenodo software record: **Published**
7. Zenodo software DOI: **10.5281/zenodo.22179598**

## Archive separation

- GitHub / Zenodo: executable source, tests, frozen aggregate endpoint inputs, release metadata.
- Dryad: manuscript-linked data/audit artifacts and reproducibility objects where appropriate.
- Restricted third-party article content is not redistributed unless the original license permits it.
- The Zenodo software DOI is not the Dryad data DOI and must not be substituted for it in the manuscript Data Availability statement.

## Claim boundary

This software validates and scores governed output contracts. It does not establish scientific truth,
universal accuracy, clinical validity, autonomous evidence retrieval, or language-model vendor invariance.
