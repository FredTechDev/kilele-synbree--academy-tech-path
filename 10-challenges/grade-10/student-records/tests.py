"""Tests for the Grade 10 Student Records challenge."""

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

sample = [
    {"name": "Amina", "marks": [78, 85, 90]},
    {"name": "Brian", "marks": [65, 72, 70]},
    {"name": "Cynthia", "marks": [88, 92, 95]},
]


def fetch(name, *args):
    try:
        return getattr(solution, name)(*args)
    except AttributeError:
        return f"MISSING FUNCTION: {name}"
    except Exception as error:  # noqa: BLE001
        return f"ERROR in {name}: {error}"


cases = [
    ("average_for(Amina)", fetch("average_for", sample[0]), 84.33),
    ("average_for(Brian)", fetch("average_for", sample[1]), 69.0),
    ("top_student(records)", fetch("top_student", sample), "Cynthia"),
    ("top_student([])", fetch("top_student", []), None),
    ("passing_students(records, 60)", fetch("passing_students", sample, 60),
     ["Amina", "Brian", "Cynthia"]),
    ("passing_students(records, 80)", fetch("passing_students", sample, 80),
     ["Amina", "Cynthia"]),
    ("passing_students([], 50)", fetch("passing_students", [], 50), []),
]

failures = 0
for label, actual, expected in cases:
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
    if not ok:
        failures += 1

sys.exit(1 if failures else 0)
