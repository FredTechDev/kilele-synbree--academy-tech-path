#!/usr/bin/env bash
# Run platform smoke tests. Skips cleanly if Flask is not installed.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PYTHON="python3"
if [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
fi

exec "$PYTHON" "$SCRIPT_DIR/tools/test_platform.py" "$@"
