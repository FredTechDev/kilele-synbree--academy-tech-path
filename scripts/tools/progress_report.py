#!/usr/bin/env python3
"""Summarize a learner's Technology Passport and suggest next steps.

Usage:
    python3 scripts/tools/progress_report.py [path/to/technology-passport.md]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT = ROOT / "07-learner-portfolio/technology-passport.md"

COMPETENCIES = [
    "Computer literacy", "Digital productivity", "Internet literacy",
    "Digital citizenship", "Computational thinking", "Programming",
    "Data literacy", "Hardware / electronics", "Networking",
    "AI awareness", "Creative technology", "Collaboration",
    "Project development",
]

MODULES = {
    "Computer literacy": "02-foundation-modules/computer-literacy/README.md",
    "Digital productivity": "02-foundation-modules/digital-productivity/README.md",
    "Internet literacy": "02-foundation-modules/internet-literacy/README.md",
    "Digital citizenship": "02-foundation-modules/digital-citizenship/README.md",
    "Computational thinking": "02-foundation-modules/computational-thinking/README.md",
    "Programming": "02-foundation-modules/programming/README.md",
    "Data literacy": "02-foundation-modules/data-literacy/README.md",
    "Hardware / electronics": "02-foundation-modules/hardware-electronics/README.md",
    "Networking": "02-foundation-modules/networking/README.md",
    "AI awareness": "02-foundation-modules/artificial-intelligence/README.md",
    "Creative technology": "02-foundation-modules/creative-technology/README.md",
    "Collaboration": "06-teacher-resources/classroom-activities/README.md",
    "Project development": "04-projects/README.md",
}


def field(text: str, name: str) -> str:
    match = re.search(rf"\*\*{re.escape(name)}:\*\*[ \t]*(.+)", text)
    return match.group(1).strip() if match else "not recorded"


def levels_in(text: str) -> dict[str, int]:
    levels: dict[str, int] = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] in COMPETENCIES:
            value = cells[1]
            if value.isdigit() and 1 <= int(value) <= 5:
                levels[cells[0]] = int(value)
    return levels


def projects_in(text: str) -> list[str]:
    found = re.findall(r"\*\*Project title:\*\*[ \t]*(.+)", text)
    return [item.strip() for item in found if item.strip()]


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    if not target.exists():
        print(f"File not found: {target}")
        return 1

    text = target.read_text(encoding="utf-8")
    levels = levels_in(text)
    projects = projects_in(text)

    print("Kilele TechPath — Progress Report")
    print("---------------------------------")
    print("Learner:", field(text, "Learner name"))
    print("Grade:", field(text, "Current grade"))
    print("Teacher / mentor:", field(text, "Teacher / mentor"))
    print("Competencies recorded:", f"{len(levels)}/{len(COMPETENCIES)}")
    if levels:
        average = sum(levels.values()) / len(levels)
        print("Average competency level:", f"{average:.2f} / 5")
    else:
        print("Average competency level: not yet recorded")
    print("Projects recorded:", len(projects))
    for project in projects:
        print("  -", project)

    print()
    print("Next steps")
    print("----------")
    if not levels:
        print("- Fill in the competency table in your technology passport.")
        print("- Use the developmental scale: 1 Emerging to 5 Advanced.")

    priorities = [
        name for name in COMPETENCIES
        if name not in levels or levels[name] <= 2
    ]
    if priorities:
        for name in priorities[:6]:
            print(f"- Practise {name}: {MODULES[name]}")
    else:
        print("- No priority gaps. Try an independent coding challenge in 10-challenges/.")

    print("- Attempt a challenge: 10-challenges/README.md")
    print("- Record evidence: 07-learner-portfolio/technology-passport.md")

    pathway = field(text, "Primary pathway")
    if pathway != "not recorded":
        print(f"- Your chosen pathway ({pathway}): explore 09-code-examples/README.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
