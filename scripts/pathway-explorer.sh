#!/usr/bin/env bash
# Interactive exploration of preferred technology pathways.
# Use --demo for a non-interactive sample run.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/tools/pathway_explorer.py" "$@"
