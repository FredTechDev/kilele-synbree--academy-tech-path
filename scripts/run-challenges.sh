#!/usr/bin/env bash
# Run coding challenge tests. Pass an optional filter, e.g. grade-9.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PYTHON="python3"
if [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
fi

exec "$PYTHON" "$SCRIPT_DIR/tools/check_challenges.py" "$@"
