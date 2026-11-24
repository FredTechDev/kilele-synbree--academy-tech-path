"""Restricted educational code runner for the playground.

This is a teaching prototype, not a production sandbox. It combines a small
static policy with an isolated subprocess, time and resource limits, and a
temporary working directory. Do not expose it to untrusted users without a
real container or VM sandbox (see README.md).
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import resource  # Unix only
except ImportError:  # pragma: no cover - non-Unix fallback
    resource = None  # type: ignore[assignment]

MAX_CODE_CHARS = 20_000
MAX_OUTPUT_CHARS = 12_000
TIMEOUT_SECONDS = 4

DANGEROUS_MODULES = {
    "os", "subprocess", "socket", "shutil", "ctypes", "multiprocessing",
    "pty", "importlib", "webbrowser", "signal", "tempfile", "sys",
}

IMPORT_RE = re.compile(r"^\s*(?:import|from)\s+([A-Za-z_][\w.]*)")
DYNAMIC_RE = re.compile(r"\b(__import__|eval|exec)\s*\(")
FILE_RE = re.compile(r"\bopen\s*\(")


def inspect_code(code: str) -> str | None:
    """Return a reason to reject the code, or None if it is allowed."""
    for line in code.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        match = IMPORT_RE.match(stripped)
        if match:
            root = match.group(1).split(".")[0]
            if root in DANGEROUS_MODULES:
                return f"module '{root}' is not available in the playground"

        if DYNAMIC_RE.search(stripped):
            return "dynamic execution is not allowed"
        if FILE_RE.search(stripped):
            return "file access is not allowed here (use a local editor instead)"
    return None


def _limits() -> None:
    if resource is None:
        return
    resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (32, 32))


def run_python(code: str) -> str:
    """Execute learner Python code and return its combined output."""
    if not code.strip():
        return "No code supplied. Write a program and run it again."
    if len(code) > MAX_CODE_CHARS:
        return "Code is too long for the playground. Shorten it and try again."

    rejected = inspect_code(code)
    if rejected:
        return f"Not permitted: {rejected}. Run this program in a local editor."

    with tempfile.TemporaryDirectory(prefix="kilele_") as workdir:
        script = Path(workdir) / "main.py"
        script.write_text(code, encoding="utf-8")

        env = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "HOME": workdir,
            "PYTHONIOENCODING": "utf-8",
            "PYTHONDONTWRITEBYTECODE": "1",
        }

        try:
            result = subprocess.run(
                [sys.executable, "-I", str(script)],
                cwd=workdir,
                env=env,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                preexec_fn=_limits if resource is not None else None,
            )
        except subprocess.TimeoutExpired:
            return f"Execution timed out after {TIMEOUT_SECONDS} seconds. Check your loops."
        except Exception as error:  # noqa: BLE001
            return f"Could not run the program: {error}"

    output = result.stdout + result.stderr
    if len(output) > MAX_OUTPUT_CHARS:
        output = output[:MAX_OUTPUT_CHARS] + "\n... output truncated."
    return output if output.strip() else "(Program finished with no output.)"
