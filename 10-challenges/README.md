# Progressive Coding Challenges

*Practice with instant feedback — built from Section 8.2 of the [Programming Framework](../PROGRAMMING-FRAMEWORK.md).*

Each topic has three levels:

| Level | What you do |
|---|---|
| 1 — Guided Practice | Reproduce a working example from the [code examples](../09-code-examples/README.md) |
| 2 — Independent Practice | Complete a `starter.py` so it passes the tests |
| 3 — Creative Challenge | Extend the solution with your own idea |

## How to use a challenge

1. Read the challenge `README.md`.
2. Copy `starter.py` to `solution.py` in the same folder.
3. Edit `solution.py` — do **not** edit `tests.py`.
4. Run the tests:

```bash
bash scripts/run-challenges.sh                 # all challenges
bash scripts/run-challenges.sh grade-9         # one grade
bash scripts/run-challenges.sh grade-9/grade-classifier   # one challenge
```

Or use `make challenges`.

## Result meanings

- **PASS** — your solution works for every test case.
- **SKIP** — you have not created `solution.py` yet.
- **FAIL** — read the message; it tells you which case failed. Errors are part of learning.

## Available challenges

| Grade | Challenge | Concepts |
|---|---|---|
| 8 | [Function Calculator](grade-8/function-calculator/README.md) | functions, arithmetic, lists |
| 9 | [Grade Classifier](grade-9/grade-classifier/README.md) | conditions, boundaries, lists |
| 10 | [Student Records](grade-10/student-records/README.md) | dictionaries, filtering, averages |
| 11 | [Data Summary](grade-11/data-summary/README.md) | statistics, validation, return values |

## Teacher notes

- Learners should attempt level 2 before looking at the [reference examples](../09-code-examples/README.md).
- Ask learners to explain *why* a test failed before you help them fix it.
- Level 3 extensions are deliberately open-ended — assess them with the [project rubric](../05-assessments/rubrics/README.md).
- Challenge results are evidence for the [Technology Passport](../07-learner-portfolio/technology-passport.md).

Related: [Teacher Guide to Python and Shell](../06-teacher-resources/teaching-guides/python-and-shell-guide.md) · [Assessments](../05-assessments/)
