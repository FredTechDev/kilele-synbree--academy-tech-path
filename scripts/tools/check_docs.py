#!/usr/bin/env python3
"""Check basic Markdown hygiene across the repository.

Reports trailing whitespace, missing final newlines and empty Markdown files.
Pass --fix to repair whitespace and newline issues automatically.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def markdown_files() -> list[Path]:
    return [
        path
        for path in sorted(ROOT.rglob("*.md"))
        if not SKIP_DIRS.intersection(path.parts)
        and not ("07-learner-portfolio" in path.parts and "learners" in path.parts)
    ]


def trailing_space_count(line: str) -> int:
    return len(line) - len(line.rstrip())


def has_hard_break(line: str) -> bool:
    """Two trailing spaces are a valid Markdown hard line break."""
    count = trailing_space_count(line)
    return count == 2 and line.endswith("  ")


def clean_line(line: str) -> str:
    return line + "  " if has_hard_break(line) else line.rstrip()


def main() -> int:
    fix = "--fix" in sys.argv[1:]
    issues: list[str] = []

    for path in markdown_files():
        relative = path.relative_to(ROOT)
        original = path.read_text(encoding="utf-8")

        if not original.strip():
            issues.append(f"{relative}: empty file")
            continue

        lines = original.splitlines()
        trailing = [
            number
            for number, line in enumerate(lines, 1)
            if trailing_space_count(line) and not has_hard_break(line)
        ]
        bad_newline = not original.endswith("\n")

        if trailing:
            issues.append(f"{relative}: trailing whitespace on line(s) {trailing[:8]}")
        if bad_newline:
            issues.append(f"{relative}: missing final newline")

        if fix and (trailing or bad_newline):
            cleaned = "\n".join(clean_line(line) for line in lines) + "\n"
            path.write_text(cleaned, encoding="utf-8")

    print(f"Checked {len(markdown_files())} Markdown files.")
    if not issues:
        print("No documentation hygiene issues found.")
        return 0

    if fix:
        print(f"Fixed {len(issues)} issue(s).")
        return 0

    print(f"Found {len(issues)} issue(s) (run check_docs.py --fix to repair):")
    for issue in issues:
        print(f"  - {issue}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
