#!/usr/bin/env bash
# Scaffold a new project folder from the standard project template.
set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 \"Project Title\" [grade] [learner-slug]" >&2
    echo "Example: $0 \"Grade Calculator\" grade-8 amina-otieno" >&2
    exit 1
fi

TITLE="$1"
GRADE="${2:-grade-11}"
LEARNER="${3:-class}"

if [[ ! "$GRADE" =~ ^grade-(6|7|8|9|10|11)$ ]]; then
    echo "Error: invalid grade folder." >&2
    exit 1
fi

SLUG="$(printf '%s' "$TITLE" | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+//; s/-+$//')"

if [ -z "$SLUG" ]; then
    echo "Error: project title must contain at least one letter or number." >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PORTFOLIO="$ROOT/07-learner-portfolio"
TARGET="$PORTFOLIO/learners/$GRADE/$LEARNER/projects/$SLUG"

if [ -e "$TARGET" ]; then
    echo "Error: $TARGET already exists." >&2
    exit 1
fi

mkdir -p "$TARGET/src"

TMP="$(mktemp)"
sed -e "1s|^# Project Template|# $TITLE|" \
    -e "s|^# \[Project title\]|# $TITLE|" \
    "$PORTFOLIO/project-template.md" > "$TMP"
mv "$TMP" "$TARGET/README.md"

touch "$TARGET/src/.gitkeep"

cat > "$TARGET/src/README.md" <<EOF
# Source files for: $TITLE

Put your source code here. Keep a short README at the project root explaining
how to run the project, and record evidence in your technology passport.
EOF

echo "Created project: $TARGET"
