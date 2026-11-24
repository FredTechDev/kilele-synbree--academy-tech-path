#!/usr/bin/env bash
# Install the platform's Python dependency into the local virtual environment.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ ! -x "$ROOT/.venv/bin/python" ]; then
    bash "$SCRIPT_DIR/setup-environment.sh"
fi

echo "Installing platform requirements..."
"$ROOT/.venv/bin/python" -m pip install -r "$ROOT/12-platform/requirements.txt"
echo "Platform dependencies ready."
