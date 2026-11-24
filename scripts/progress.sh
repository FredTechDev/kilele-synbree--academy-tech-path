#!/usr/bin/env bash
# Print a progress report from a learner's Technology Passport.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "$SCRIPT_DIR/tools/progress_report.py" "$@"
