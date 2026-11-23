#!/usr/bin/env bash
# Create a personal learner portfolio from the standard templates.
set -euo pipefail

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 \"Learner Name\" <grade-folder> [teacher]" >&2
    echo "Example: $0 \"Amina Otieno\" grade-8 \"Mr Kamau\"" >&2
    exit 1
fi

NAME="$1"
GRADE="$2"
TEACHER="${3:-Not assigned}"

if [[ ! "$GRADE" =~ ^grade-(6|7|8|9|10|11)$ ]]; then
    echo "Error: grade must be grade-6, grade-7, grade-8, grade-9, grade-10 or grade-11." >&2
    exit 1
fi

SLUG="$(printf '%s' "$NAME" | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+//; s/-+$//')"

if [ -z "$SLUG" ]; then
    echo "Error: learner name must contain at least one letter or number." >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PORTFOLIO="$ROOT/07-learner-portfolio"
TARGET="$PORTFOLIO/learners/$GRADE/$SLUG"

if [ -e "$TARGET" ]; then
    echo "Error: $TARGET already exists. Choose a different name or grade." >&2
    exit 1
fi

mkdir -p "$TARGET/projects"

TMP="$(mktemp)"
sed -e "s|^- \*\*Learner name:\*\*.*|- **Learner name:** $NAME|" \
    -e "s|^- \*\*Current grade:\*\*.*|- **Current grade:** $GRADE|" \
    -e "s|^- \*\*Teacher / mentor:\*\*.*|- **Teacher / mentor:** $TEACHER|" \
    "$PORTFOLIO/technology-passport.md" > "$TMP"
mv "$TMP" "$TARGET/technology-passport.md"

cp "$PORTFOLIO/reflection-template.md" "$TARGET/reflection.md"

cat > "$TARGET/README.md" <<EOF
# $NAME — Technology Passport

- **Grade:** $GRADE
- **Teacher / mentor:** $TEACHER
- **Created:** $(date -u +%Y-%m-%d)

## Files

- \`technology-passport.md\` — main progress record
- \`reflection.md\` — copy of the reflection template
- \`projects/\` — project work, one folder per project

## Templates

- [Project template](../../project-template.md)
- [Reflection template](../../reflection-template.md)

## Privacy reminder

Do not store real personal data, real passwords or identifying information in
public repositories. Use sample data and anonymized records for demonstrations.
EOF

echo "Created learner portfolio: $TARGET"
echo "Next: bash scripts/new-project.sh \"Project Title\" $GRADE $SLUG"
