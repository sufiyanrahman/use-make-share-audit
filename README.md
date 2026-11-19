# Use–Make–Share Self-Audit

A 15-question checklist for checking whether a research project applies open science practices (data, code, results). It is derived from the public module descriptions of NASA's Open Science 101 (TOPS) curriculum.

> Independent work. Not affiliated with, endorsed by, or produced for NASA. The accompanying paper is a preprint and has not been peer reviewed.

## What is in this repo
- `checklist.csv` – the 15 criteria (id, criterion, stage, score, evidence_link).
- `data_dictionary.md` – explains each column and its allowed values.
- `validate_audit.py` – checks the checklist file and computes the score.
- `requirements.txt` – lists dependencies (none).
- `LICENSE` – MIT.
- Paper: https://doi.org/10.5281/zenodo.24364509

## How to use the checklist
1. Copy `checklist.csv`.
2. Score each criterion: 1 only if a public link proves it, 0 if it applies but is not met, N/A if it does not apply.
3. Paste the proof link in `evidence_link`.
4. Run the validation script (see Reproduction).

## Data management plan
- **Data:** one file, `checklist.csv`, containing the 15 audit criteria. It holds no personal or sensitive data.
- **Format:** plain CSV (RFC 4180), documented in `data_dictionary.md`.
- **Storage and versioning:** public GitHub repository with commit history.
- **Preservation:** tagged releases are archived on Zenodo, which issues a DOI.
- **License:** the checklist data and documentation are CC BY 4.0. Code is MIT.
- **Responsibility:** the author maintains the repository.

## Reproduction
Requires Python 3.8 or newer. No packages to install.
1. Download or clone this repository.
2. Open a terminal in the repository folder.
3. Run: `python validate_audit.py checklist.csv`
4. The script reports any errors, or prints the score out of the applicable criteria.

## Limitations
The checklist is unvalidated beyond the author's own use, uses 1 / 0 / N/A scoring, and covers only criteria that can be verified from public materials.

## Author
Sufiyan Shafeeq Ur Rahman · Independent researcher · ORCID 0009-0007-0719-6404
