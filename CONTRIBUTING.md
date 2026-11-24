# Contributing to Kilele TechPath

Thank you for helping improve the Kilele TechPath curriculum. This document explains how to propose changes and keep the repository consistent.

## Who can contribute

Teachers, mentors, curriculum designers, learners, parents and technology professionals are welcome to contribute. Contributions are reviewed by the Kilele Archade / Synbree curriculum team.

## Ways to contribute

- Fix errors, typos and unclear wording.
- Add or improve practical activities and projects.
- Suggest age-appropriate tools and resources.
- Improve assessment rubrics and competency descriptors.
- Translate or adapt materials for local contexts.
- Report accessibility or inclusion gaps.
- Add lesson plans and teaching guides.

## Ground rules

1. **Learner safety first.** Every activity must be age-appropriate and safe. Cybersecurity work must only use approved, simulated or explicitly authorized environments — never real systems without permission.
2. **Practical and evidence-based.** Major topics should include a hands-on activity and observable evidence of learning.
3. **Stay aligned with the progression.** New content should fit the grade stage (Awareness → Competence → Creation → Exploration → Discovery → Direction).
4. **Respect attribution.** Cite sources for external material and respect copyright and licensing.
5. **Use inclusive language.** Materials should accommodate different abilities, devices and connectivity levels.
6. **Keep it accessible.** Prefer free/open, affordable and offline-capable tools where possible.

## How to propose a change

1. Open an issue describing the proposed change and the reasoning behind it.
2. Fork the repository and create a focused branch, e.g. `grade-8-python-activity`.
3. Make your change in the appropriate file:
   - Full curriculum changes → `TECH-PATH-CURRICULUM.md`
   - Grade detail → `01-grade-curriculum/grade-*/curriculum.md`
   - Shared modules → `02-foundation-modules/*/README.md`
   - Pathways → `03-specialization-pathways/*/README.md`
   - Projects → `04-projects/*/README.md`
   - Assessments → `05-assessments/*/README.md`
   - Teacher resources → `06-teacher-resources/*/README.md`
4. Keep Markdown formatting, headings and tables consistent with the existing files.
5. Run the local checks before opening a pull request (see "Local checks" below).
6. Open a pull request explaining the change, the grade level affected and any resources required.

## Curriculum versioning

Use semantic-style version numbers as described in the curriculum:

- **Major** (`v2.0.0`) — significant curriculum restructuring.
- **Minor** (`v1.1.0`) — new modules or substantial improvements.
- **Patch** (`v1.1.1`) — corrections and small updates.

Document every released change in the repository release notes.

## Local checks

The repository includes Python and shell helpers that check documentation and run every code example:

```bash
bash scripts/setup-environment.sh   # check tools and create .venv
bash scripts/check-all.sh            # links + docs hygiene + example tests
```

Useful individual commands:

- `bash scripts/validate-links.sh` — internal links and heading anchors
- `bash scripts/check-docs.sh --fix` — repair trailing whitespace and final newlines
- `bash scripts/run-examples.sh` — run all examples with sample input
- `bash scripts/run-challenges.sh` — check challenge solutions (SKIP is expected when none are attempted)
- `make check` — same as `check-all.sh` through the Makefile

See [scripts/README.md](scripts/README.md) for the full list, including learner and project scaffolding.

## Review checklist

- [ ] Content is accurate and age-appropriate.
- [ ] At least one practical activity is included where relevant.
- [ ] Safety, privacy and ethics are addressed where relevant.
- [ ] Links and tool references are valid and licensing is acceptable.
- [ ] Markdown renders correctly.
- [ ] Related files (curriculum, grade, assessment, resource lists) are updated consistently.
- [ ] `bash scripts/check-all.sh` passes (or any failure is explained in the PR).

By contributing, you agree that your work is licensed under the [MIT License](LICENSE).

---

*Ideas. Software. Next.*
