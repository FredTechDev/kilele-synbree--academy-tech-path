"""Tests for the Grade 11 Data Summary challenge."""

import importlib.util
import sys
from pathlib import Path

solution_path = Path(__file__).with_name("solution.py")

if not solution_path.exists():
    print("SKIP: solution.py not found. Copy starter.py to solution.py.")
    sys.exit(0)

spec = importlib.util.spec_from_file_location("solution", solution_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def fetch(name, *args):
    try:
        return getattr(solution, name)(*args)
    except AttributeError:
        return f"MISSING FUNCTION: {name}"
    except Exception as error:  # noqa: BLE001
        return f"ERROR in {name}: {error}"


cases = [
    ("summarize([4, 8, 10])", fetch("summarize", [4, 8, 10]),
     {"count": 3, "min": 4, "max": 10, "mean": 7.33}),
    ("summarize([100])", fetch("summarize", [100]),
     {"count": 1, "min": 100, "max": 100, "mean": 100.0}),
    ("summarize([])", fetch("summarize", []),
     {"count": 0, "min": None, "max": None, "mean": None}),
    ("invalid_values([50, 120, -3, 80])", fetch("invalid_values", [50, 120, -3, 80]),
     [120, -3]),
    ("invalid_values([0, 100, 75])", fetch("invalid_values", [0, 100, 75]), []),
]

failures = 0
for label, actual, expected in cases:
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
    if not ok:
        failures += 1

sys.exit(1 if failures else 0)
