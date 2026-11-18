"""Validate checklist.csv and compute the audit score.

Usage: python validate_audit.py checklist.csv
Uses only the Python standard library.
"""
import csv
import sys

EXPECTED_COLUMNS = ["id", "criterion", "stage", "score", "evidence_link"]
EXPECTED_IDS = (
    [f"D{i}" for i in range(1, 7)]
    + [f"C{i}" for i in range(1, 6)]
    + [f"R{i}" for i in range(1, 5)]
)
STAGES = {"Use", "Make", "Share"}
SCORES = {"1", "0", "N/A", ""}


def main(path):
    errors = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != EXPECTED_COLUMNS:
            sys.exit(f"Columns must be exactly: {EXPECTED_COLUMNS}")
        rows = list(reader)

    ids = [r["id"] for r in rows]
    if ids != EXPECTED_IDS:
        errors.append("Criterion ids are missing, duplicated, or out of order.")

    met = applicable = 0
    for r in rows:
        if r["stage"] not in STAGES:
            errors.append(f"{r['id']}: stage must be Use, Make, or Share.")
        if r["score"] not in SCORES:
            errors.append(f"{r['id']}: score must be 1, 0, N/A, or empty.")
        if r["score"] == "1" and not r["evidence_link"].strip():
            errors.append(f"{r['id']}: a score of 1 needs an evidence link.")
        if r["score"] in {"1", "0"}:
            applicable += 1
            met += r["score"] == "1"

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    if applicable:
        print(f"Score: {met} / {applicable} applicable criteria")
    else:
        print("No scored criteria yet.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "checklist.csv")
