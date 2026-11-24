# Kilele TechPath Platform Prototype

*A working local implementation of the capabilities recommended in Section 14 of the [Programming Framework](../PROGRAMMING-FRAMEWORK.md).*

## What is implemented

| Section 14 capability | Where |
|---|---|
| 14.1 Interactive Coding Playground | `/playground` — Python runner and sandboxed HTML preview |
| 14.2 Guided Coding Challenges | [10-challenges](../10-challenges/README.md) — linked from the curriculum |
| 14.3 Project Submission System | `/submit` and `/submissions` — SQLite-backed |
| 14.4 Technology Passport | `/passport` — competency levels 1–5 |
| 14.5 Teacher Dashboard | `/dashboard` — counts, recent submissions, learner averages |
| 14.6 Specialization Discovery | `/discover` — eight interest questions, two suggested pathways |
| 14.7 Project Showcase | `/showcase` — moderated, teacher-approved gallery |

## Run it locally

```bash
bash scripts/setup-platform.sh          # installs Flask into .venv
bash scripts/run-platform.sh            # starts at http://127.0.0.1:5000
```

Or manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -r 12-platform/requirements.txt
.venv/bin/python 12-platform/app.py
```

Open <http://127.0.0.1:5000>.

## Configuration

| Environment variable | Purpose | Default |
|---|---|---|
| `KILELE_DB_PATH` | SQLite database file | `12-platform/data/kilele.db` |
| `KILELE_TEACHER_PIN` | PIN for teacher pages | none (open access) |
| `KILELE_SECRET_KEY` | Flask session secret | development-only value |
| `KILELE_HOST` | Bind address | `127.0.0.1` |
| `KILELE_PORT` | Port | `5000` |

Example:

```bash
KILELE_TEACHER_PIN=changeme KILELE_SECRET_KEY="a-long-random-value" bash scripts/run-platform.sh
```

The database file is ignored by Git. Delete it to reset the prototype.

## Architecture

```
12-platform/
├── app.py            Flask routes, database helpers, teacher gate
├── runner.py         restricted Python runner (subprocess + limits)
├── pathways.py       pathway metadata and recommendation logic
├── requirements.txt  Flask dependency
├── templates/        Jinja2 pages
└── static/style.css  styling
```

Database tables: `submissions`, `competencies`, `interests`.

## Safety — read this

This is a **teaching prototype**, not a production platform.

- The Python runner blocks common dangerous modules, file access and dynamic execution, then runs code in a temporary directory with CPU, memory, file-size, file-count and time limits. A static filter is **not** a security boundary. Do not expose this to untrusted users.
- Before real deployment, run code in a container or VM with no network access, a read-only filesystem and a non-root user (or use a dedicated sandboxing service).
- HTML preview uses an iframe with `sandbox="allow-scripts"` and an opaque origin. It cannot read the parent page, but it can still make network requests.
- Use sample or anonymized data only. Never submit real learner credentials, passwords or identifying information.
- Set `KILELE_TEACHER_PIN` and `KILELE_SECRET_KEY` before allowing access from a shared network.
- Add authentication, CSRF protection, rate limiting, HTTPS, audit logs and backups before production use.

## Tests

```bash
bash scripts/test-platform.sh
```

Tests use Flask's test client with a temporary database. They cover the playground (including blocked code), submissions and approval, passport records, discovery, dashboard and showcase. If Flask is not installed the suite reports SKIP.

## Production roadmap

1. Real learner accounts and role-based access (learner, teacher, admin).
2. Containerized code execution with no network and strict resource quotas.
3. Persisted, versioned portfolio evidence and file uploads with malware scanning.
4. Teacher moderation queue with comments and rubric scoring.
5. Accessibility audit (keyboard navigation, screen readers, contrast).
6. Localization of the interface (see [13-localization](../13-localization/README.md)).
7. Backups, logging, monitoring and a documented deployment process.

Related: [Programming Framework](../PROGRAMMING-FRAMEWORK.md) · [Localization](../13-localization/README.md) · [Scripts](../scripts/README.md)
