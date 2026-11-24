#!/usr/bin/env bash
# Start the Kilele TechPath platform prototype on localhost.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ ! -x "$ROOT/.venv/bin/python" ]; then
    echo "Virtual environment missing. Run: bash scripts/setup-platform.sh" >&2
    exit 1
fi

if ! "$ROOT/.venv/bin/python" -c "import flask" >/dev/null 2>&1; then
    echo "Flask missing. Run: bash scripts/setup-platform.sh" >&2
    exit 1
fi

cd "$ROOT"
exec "$ROOT/.venv/bin/python" 12-platform/app.py "$@"
