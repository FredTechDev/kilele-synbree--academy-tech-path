#!/usr/bin/env bash
# Prepare a local environment for the code examples and repository checks.
# Use --with-ai to also install the AI example dependency (scikit-learn).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Checking required tools..."

for tool in python3 git bash; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  [OK] $tool"
    else
        echo "  [MISSING] $tool — please install it before continuing." >&2
        exit 1
    fi
done

VENV="$ROOT/.venv"
if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment at $VENV ..."
    python3 -m venv "$VENV"
else
    echo "Virtual environment already exists."
fi

PYTHON="$VENV/bin/python"
"$PYTHON" -m pip --version >/dev/null

if [ "${1:-}" = "--with-ai" ]; then
    echo "Installing AI example dependencies..."
    "$PYTHON" -m pip install -r "$ROOT/09-code-examples/04-artificial-intelligence/requirements.txt"
fi

echo
echo "Environment ready."
echo "  Run checks:       bash scripts/check-all.sh"
echo "  Run examples:     bash scripts/run-examples.sh"
echo "  Optional AI demo: bash scripts/setup-environment.sh --with-ai"
