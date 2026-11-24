#!/usr/bin/env python3
"""Validate the localization termbase and translated locale summaries."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "13-localization"
TERMBASE = BASE / "termbase.csv"
LOCALES = {"sw": "Kiswahili", "fr": "Français"}
MIN_TERMS = 35
MIN_TRANSLATED_TERMS = 5


def main() -> int:
    issues: list[str] = []

    if not TERMBASE.exists():
        print(f"Missing termbase: {TERMBASE}")
        return 1

    with TERMBASE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    columns = set(rows[0].keys()) if rows else set()
    for column in ["en", "sw", "fr"]:
        if column not in columns:
            issues.append(f"termbase is missing the '{column}' column")

    seen: set[str] = set()
    for number, row in enumerate(rows, 2):
        term = row.get("en", "").strip()
        if not term:
            issues.append(f"termbase line {number}: empty English term")
            continue
        if term in seen:
            issues.append(f"termbase line {number}: duplicate term '{term}'")
        seen.add(term)
        for column in ["sw", "fr"]:
            if not row.get(column, "").strip():
                issues.append(f"termbase line {number}: missing {column} translation for '{term}'")

    if len(rows) < MIN_TERMS:
        issues.append(f"termbase has {len(rows)} terms; expected at least {MIN_TERMS}")

    for code, label in LOCALES.items():
        path = BASE / "locales" / code / "README.md"
        if not path.exists():
            issues.append(f"{label}: missing {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        if len(text) < 500:
            issues.append(f"{label}: translation is very short ({len(text)} characters)")
        if "TODO" in text:
            issues.append(f"{label}: untranslated TODO marker found")
        if "TECH-PATH-CURRICULUM.md" not in text:
            issues.append(f"{label}: no link to the full curriculum")

        translations = [row.get(code, "").strip().lower() for row in rows]
        used = sum(1 for term in translations if term and term in text.lower())
        if used < MIN_TRANSLATED_TERMS:
            issues.append(
                f"{label}: only {used} approved terms used; expected at least {MIN_TRANSLATED_TERMS}"
            )

    print(f"Checked termbase ({len(rows)} terms) and {len(LOCALES)} locales.")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    print("Localization resources are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
