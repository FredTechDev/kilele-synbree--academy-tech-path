#!/usr/bin/env bash
# Validate all internal Markdown links and heading anchors.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/tools/validate_links.py" "$@"
