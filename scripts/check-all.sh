#!/usr/bin/env bash
# Run every repository check. Used by CI and by `make check`.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "$SCRIPT_DIR/validate-links.sh"
bash "$SCRIPT_DIR/check-docs.sh"
bash "$SCRIPT_DIR/run-examples.sh"
bash "$SCRIPT_DIR/run-challenges.sh"

echo "All checks completed successfully."
