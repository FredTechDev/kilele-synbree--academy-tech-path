#!/usr/bin/env python3
"""Validate internal Markdown links, including heading anchors.

Used by scripts/validate-links.sh and by CI. Exits with status 1 if any
internal link points to a missing file or a heading that does not exist.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")

_anchor_cache: dict[Path, set[str]] = {}


def slugify(text: str) -> str:
    """Approximate GitHub's heading anchor generation."""
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s+", "-", text.strip())


def without_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def anchors_in(path: Path) -> set[str]:
    if path not in _anchor_cache:
        text = without_code(path.read_text(encoding="utf-8"))
        _anchor_cache[path] = {
            slugify(match.group(1)) for match in HEADING_RE.finditer(text)
        }
    return _anchor_cache[path]


def main() -> int:
    broken: list[str] = []
    checked = 0

    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS.intersection(path.parts):
            continue
        # Generated learner workspaces are personal and git-ignored; their
        # copied templates contain links relative to the template location.
        if "07-learner-portfolio" in path.parts and "learners" in path.parts:
            continue

        text = without_code(path.read_text(encoding="utf-8"))
        relative = path.relative_to(ROOT)

        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip().split(maxsplit=1)[0]
            if not raw or SCHEME_RE.match(raw):
                continue

            file_part, separator, anchor = raw.partition("#")
            checked += 1

            if file_part:
                target = (path.parent / file_part).resolve()
                if not target.exists():
                    broken.append(f"{relative}: missing file -> {raw}")
                    continue
                if separator and target.suffix.lower() == ".md":
                    if anchor not in anchors_in(target):
                        broken.append(f"{relative}: missing anchor -> {raw}")
            elif separator and anchor not in anchors_in(path):
                broken.append(f"{relative}: missing anchor -> {raw}")

    print(f"Checked {checked} internal links.")
    if broken:
        print(f"Found {len(broken)} broken link(s):")
        for item in broken:
            print(f"  - {item}")
        return 1

    print("All internal links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
