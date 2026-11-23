#!/usr/bin/env bash
# Run and verify every code example in 09-code-examples/.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PYTHON="python3"
if [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
fi

exec "$PYTHON" "$SCRIPT_DIR/tools/test_examples.py" "$@"
