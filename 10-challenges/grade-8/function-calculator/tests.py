"""Tests for the Grade 8 Function Calculator challenge."""

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
    except Exception as error:  # noqa: BLE001 - learner code may raise anything
        return f"ERROR in {name}: {error}"


cases = [
    ("add(2, 3)", fetch("add", 2, 3), 5),
    ("add(-4, 9)", fetch("add", -4, 9), 5),
    ("multiply(3, 4)", fetch("multiply", 3, 4), 12),
    ("multiply(0, 7)", fetch("multiply", 0, 7), 0),
    ("average([80, 90, 100])", fetch("average", [80, 90, 100]), 90),
    ("average([])", fetch("average", []), 0),
]

failures = 0
for label, actual, expected in cases:
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
    if not ok:
        failures += 1

sys.exit(1 if failures else 0)
