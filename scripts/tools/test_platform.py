#!/usr/bin/env python3
"""Smoke tests for the platform prototype using Flask's test client."""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLATFORM = ROOT / "12-platform"


def main() -> int:
    try:
        import flask  # noqa: F401
    except ImportError:
        print("SKIP: Flask is not installed. Run: bash scripts/setup-platform.sh")
        return 0

    with tempfile.TemporaryDirectory(prefix="kilele_test_") as tmp:
        os.environ["KILELE_DB_PATH"] = str(Path(tmp) / "test.db")
        os.environ["KILELE_TEACHER_PIN"] = ""
        os.environ["KILELE_SECRET_KEY"] = "test-only"
        sys.path.insert(0, str(PLATFORM))

        import app as platform_app  # noqa: PLC0415

        client = platform_app.app.test_client()
        failures = 0

        def check(name: str, condition: bool, detail: str = "") -> None:
            nonlocal failures
            status = "PASS" if condition else "FAIL"
            print(f"[{status}] {name}" + (f": {detail}" if detail and not condition else ""))
            if not condition:
                failures += 1

        response = client.get("/")
        check("home page", response.status_code == 200 and b"Kilele TechPath" in response.data)

        response = client.get("/playground")
        check("playground page", response.status_code == 200)

        response = client.post(
            "/playground",
            data={"language": "python", "code": "print('hello kilele')"},
        )
        check("python execution", b"hello kilele" in response.data)

        response = client.post(
            "/playground",
            data={"language": "python", "code": "import os\nprint('blocked')"},
        )
        check("blocked import", b"Not permitted" in response.data)

        response = client.post(
            "/playground",
            data={"language": "html", "code": "<h1>Preview</h1>"},
        )
        check("html preview", b"sandbox" in response.data and b"Preview displayed" in response.data)

        response = client.post(
            "/submit",
            data={
                "learner": "Amina", "grade": "Grade 9", "title": "Grade Calculator",
                "description": "Calculates averages", "code": "print(1)",
                "pathway": "Software Engineering",
            },
        )
        check("project submission", response.status_code == 302)

        response = client.get("/submissions")
        check("submissions list", b"Grade Calculator" in response.data)

        response = client.post("/approve/1")
        check("approval", response.status_code == 302)
        response = client.get("/showcase")
        check("showcase", b"Grade Calculator" in response.data)

        response = client.post(
            "/passport",
            data={"learner": "Amina", "grade": "Grade 9",
                  "competency": "Programming", "level": "4"},
        )
        check("passport save", response.status_code == 302)
        response = client.get("/passport?learner=Amina")
        check("passport display", b"Programming" in response.data and b"4 / 5" in response.data)

        answers = {f"q{number}": "5" for number in range(8)}
        answers["learner"] = "Amina"
        response = client.post("/discover", data=answers)
        check("discovery", b"Suggested pathways" in response.data)

        response = client.get("/dashboard")
        check("teacher dashboard", response.status_code == 200 and b"Submissions" in response.data)

        response = client.get("/login")
        check("login page", response.status_code == 200)

        print("-------------------------------------")
        print(f"Platform checks: {12 - failures} passed, {failures} failed")
        return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
