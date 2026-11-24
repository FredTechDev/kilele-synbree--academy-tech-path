#!/usr/bin/env bash
# Validate localization termbase and translated locale summaries.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/tools/check_localization.py" "$@"
