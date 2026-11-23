#!/usr/bin/env python3
"""Run every code example and check that it behaves as documented.

This gives learners a one-command confidence check and is used by CI.
Examples needing optional dependencies are skipped with a clear message.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "09-code-examples"

PYTHON_CASES = [
    {
        "name": "Student Grade Calculator",
        "path": "01-software-engineering/student-grade-calculator.py",
        "stdin": "Amina\n80\n90\n100\n",
        "expect": ["STUDENT REPORT", "Student: Amina", "Average: 90.0", "Grade: A"],
    },
    {
        "name": "Student Performance Analysis",
        "path": "02-data-science/student-performance-analysis.py",
        "stdin": "",
        "expect": ["STUDENT PERFORMANCE ANALYSIS", "Class Average: 75.53"],
    },
    {
        "name": "Password Strength Checker (weak)",
        "path": "03-cybersecurity/password-strength-checker.py",
        "stdin": "abc\n",
        "expect": ["PASSWORD ASSESSMENT", "Result: Weak"],
    },
    {
        "name": "Password Strength Checker (strong)",
        "path": "03-cybersecurity/password-strength-checker.py",
        "stdin": "Str0ng!Password\n",
        "expect": ["Result: Meets the basic complexity checks"],
    },
    {
        "name": "ML Classification",
        "path": "04-artificial-intelligence/ml-classification.py",
        "stdin": "",
        "expect": ["The model predicts:"],
        "skip_marker": "scikit-learn is not installed",
    },
    {
        "name": "IP Address Tool (valid)",
        "path": "07-networking-cloud/ip-address-tool.py",
        "stdin": "192.168.1.0/24\n",
        "expect": [
            "Network Address: 192.168.1.0",
            "Subnet Mask: 255.255.255.0",
            "Number of Addresses: 256",
            "IP Version: IPv4",
        ],
    },
    {
        "name": "IP Address Tool (invalid)",
        "path": "07-networking-cloud/ip-address-tool.py",
        "stdin": "not-an-ip\n",
        "expect": ["Invalid IP address or network range."],
    },
]

STATIC_CASES = [
    {
        "name": "Smart Irrigation Controller",
        "path": "05-robotics-iot/smart-irrigation.ino",
        "expect": ["void setup()", "void loop()", "analogRead(soilSensor)"],
    },
    {
        "name": "Learning Dashboard",
        "path": "06-ui-ux-design/learning-dashboard/index.html",
        "expect": ["<!DOCTYPE html>", "My Learning Dashboard", "showMessage()"],
    },
    {
        "name": "Interactive Animated Art (page)",
        "path": "08-multimedia/interactive-art/index.html",
        "expect": ["<!DOCTYPE html>", "p5.min.js", "sketch.js"],
    },
    {
        "name": "Interactive Animated Art (sketch)",
        "path": "08-multimedia/interactive-art/sketch.js",
        "expect": ["function setup()", "function draw()", "circle(x, y, 60)"],
    },
]


def run_python_case(case: dict) -> tuple[str, str]:
    result = subprocess.run(
        [sys.executable, str(EXAMPLES / case["path"])],
        input=case["stdin"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=30,
    )
    output = result.stdout + result.stderr

    if result.returncode != 0:
        return "FAIL", f"exited with {result.returncode}: {output.strip()[:300]}"

    if case.get("skip_marker") and case["skip_marker"] in output:
        return "SKIP", "optional dependency missing; install with its requirements.txt"

    missing = [item for item in case["expect"] if item not in output]
    if missing:
        return "FAIL", f"missing output: {missing}; got: {output.strip()[:300]}"

    return "PASS", "output matches"


def run_static_case(case: dict) -> tuple[str, str]:
    path = EXAMPLES / case["path"]
    if not path.exists():
        return "FAIL", "file is missing"
    text = path.read_text(encoding="utf-8")
    missing = [item for item in case["expect"] if item not in text]
    if missing:
        return "FAIL", f"missing content: {missing}"
    return "PASS", "file present with expected content"


def main() -> int:
    print("Kilele TechPath — code example checks")
    print("-------------------------------------")

    failures = 0
    passes = 0
    skips = 0

    for case in PYTHON_CASES + STATIC_CASES:
        if "stdin" in case:
            status, detail = run_python_case(case)
        else:
            status, detail = run_static_case(case)

        print(f"[{status}] {case['name']}: {detail}")
        if status == "FAIL":
            failures += 1
        elif status == "SKIP":
            skips += 1
        else:
            passes += 1

    print("-------------------------------------")
    print(f"Passed: {passes} | Skipped: {skips} | Failed: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
