#!/usr/bin/env bash
# Check Markdown hygiene (trailing whitespace, final newlines, empty files).
# Pass --fix to repair whitespace and newline issues automatically.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/tools/check_docs.py" "$@"
