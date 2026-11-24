"""Tests for the Grade 9 Grade Classifier challenge."""

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
    ("classify_average(85)", fetch("classify_average", 85), "A"),
    ("classify_average(80)", fetch("classify_average", 80), "A"),
    ("classify_average(79.99)", fetch("classify_average", 79.99), "B"),
    ("classify_average(70)", fetch("classify_average", 70), "B"),
    ("classify_average(60)", fetch("classify_average", 60), "C"),
    ("classify_average(50)", fetch("classify_average", 50), "D"),
    ("classify_average(49)", fetch("classify_average", 49), "E"),
    ("class_average([80, 90, 100])", fetch("class_average", [80, 90, 100]), 90.0),
    ("class_average([78, 85, 90])", fetch("class_average", [78, 85, 90]), 84.33),
    ("class_average([])", fetch("class_average", []), 0),
]

failures = 0
for label, actual, expected in cases:
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
    if not ok:
        failures += 1

sys.exit(1 if failures else 0)
