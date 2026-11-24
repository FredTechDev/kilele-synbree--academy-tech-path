#!/usr/bin/env python3
"""Run coding challenge tests and report PASS / SKIP / FAIL per challenge.

SKIP means the learner has not created solution.py yet, which is expected
in a clean repository. A filter argument limits the run, e.g. "grade-9".
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHALLENGES = ROOT / "10-challenges"


def main() -> int:
    filter_text = sys.argv[1] if len(sys.argv) > 1 else ""
    tests = sorted(CHALLENGES.glob("**/tests.py"))

    if not tests:
        print("No challenges found in 10-challenges/.")
        return 1

    print("Kilele TechPath — coding challenge checks")
    print("------------------------------------------")

    passed = skipped = failed = 0

    for test in tests:
        relative = test.parent.relative_to(ROOT).as_posix()
        if filter_text and filter_text not in relative:
            continue

        result = subprocess.run(
            [sys.executable, str(test)],
            cwd=test.parent,
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = (result.stdout + result.stderr).strip()

        if "SKIP:" in output:
            status = "SKIP"
            skipped += 1
        elif result.returncode == 0:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print(f"[{status}] {relative}")
        for line in output.splitlines():
            print(f"    {line}")

    print("------------------------------------------")
    print(f"Passed: {passed} | Skipped: {skipped} | Failed: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
