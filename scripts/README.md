# Repository Scripts

*Small Python and shell tools that make the curriculum easier to use, check and extend.*

All scripts are run from the repository root. They are safe to run repeatedly.

## Quick start

```bash
bash scripts/setup-environment.sh    # check tools and create .venv
bash scripts/check-all.sh             # links + docs + example tests
```

## Available scripts

| Script | Purpose |
|---|---|
| `setup-environment.sh` | Check required tools, create a Python virtual environment. Add `--with-ai` to install scikit-learn. |
| `validate-links.sh` | Check internal Markdown links and heading anchors. |
| `check-docs.sh` | Check Markdown hygiene. Add `--fix` to repair whitespace and final newlines. |
| `run-examples.sh` | Run and verify every example in `09-code-examples/`. Uses `.venv` if present. |
| `check-all.sh` | Run all checks — also used by CI and `make check`. |
| `run-challenges.sh` | Run coding challenge tests. Pass a filter such as `grade-9`. |
| `progress.sh` | Print a progress report from a Technology Passport. |
| `pathway-explorer.sh` | Interactive pathway discovery. Use `--demo` for a sample run. |
| `setup-platform.sh` | Install Flask into `.venv` for the platform prototype. |
| `run-platform.sh` | Start the platform at `http://127.0.0.1:5000`. |
| `test-platform.sh` | Smoke-test the platform with Flask's test client. |
| `localization.sh` | Validate termbase and translated locale summaries. |
| `new-learner.sh` | Create a learner portfolio from the standard templates. |
| `new-project.sh` | Scaffold a project folder from the project template. |

## Examples

```bash
# Create a learner portfolio
bash scripts/new-learner.sh "Amina Otieno" grade-8 "Mr Kamau"

# Create a project for that learner
bash scripts/new-project.sh "Grade Calculator" grade-8 amina-otieno

# Repair documentation whitespace
bash scripts/check-docs.sh --fix

# Test your challenge solutions
bash scripts/run-challenges.sh grade-9

# See a progress report and explore pathways
bash scripts/progress.sh
bash scripts/pathway-explorer.sh --demo

# Run everything
bash scripts/check-all.sh
```

## Makefile shortcuts

From the repository root:

```bash
make check
make links
make examples
make challenges
make progress
make explore
make localization
make platform-test
make setup
make platform
make learner NAME="Amina Otieno" GRADE=grade-8
make project TITLE="Grade Calculator" GRADE=grade-8 LEARNER=amina-otieno
```

## Under the hood

The shell scripts are thin wrappers around Python tools in `scripts/tools/`:

- `validate_links.py` — parses Markdown links and heading anchors.
- `check_docs.py` — documentation hygiene checks, with `--fix`.
- `test_examples.py` — runs each example with sample input and checks its output.
- `check_challenges.py` — runs challenge tests; unattempted challenges are reported as SKIP.
- `progress_report.py` — reads a passport and suggests competencies to practise next.
- `pathway_explorer.py` — scores eight interest questions and suggests pathways to explore.
- `test_platform.py` — exercises the Flask prototype with a temporary database.
- `check_localization.py` — validates termbase consistency and locale files.

Optional dependencies are reported as `SKIP`, not failure, so the checks work on machines without scikit-learn.

## Privacy and safety

- Learner folders are for local use. Do not commit real personal data or identifying information to a public repository.
- Never enter real passwords into the password checker example.
- Do not run learner-submitted code with elevated privileges.

Related: [Code Examples](../09-code-examples/README.md) · [Teacher Guide to Python and Shell](../06-teacher-resources/teaching-guides/python-and-shell-guide.md)
