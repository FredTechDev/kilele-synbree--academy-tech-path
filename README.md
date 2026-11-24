# KILELE TECHPATH

**A Complete Technology Discovery, Literacy and Specialization Curriculum — Grades 6–11**

> **Discover. Explore. Build. Specialize.**

Kilele TechPath is a progressive, practical, competency-based and project-oriented technology education pathway developed under **Kilele Archade** in association with the **Technology and Innovation Association: Synbree**.

It introduces learners to the wider technology ecosystem — not just programming — and guides them from first computer experiences in Grade 6 to a focused, documented capstone project in Grade 11.

---

## Programme at a glance

| Grade | Stage | Central theme |
|---|---|---|
| Grade 6 | Awareness | Understanding technology |
| Grade 7 | Competence | Using technology productively |
| Grade 8 | Creation | Building simple digital solutions |
| Grade 9 | Exploration | Discovering technology disciplines |
| Grade 10 | Discovery | Exploring specialization pathways |
| Grade 11 | Direction | Developing focused practical expertise |

## What learners develop

- Digital, computer and internet literacy
- Computational thinking and problem-solving
- Programming, web development and databases
- Data literacy and visualization
- Hardware, electronics, robotics and networking awareness
- Artificial intelligence literacy and cybersecurity awareness
- Digital creativity, collaboration and project development
- A personal technology portfolio and informed career awareness

---

## Repository structure

```
kilele-techpath/
├── README.md                          ← you are here
├── TECH-PATH-CURRICULUM.md            ← full curriculum document
├── PROGRAMMING-FRAMEWORK.md           ← programming & pathway development guide (v1.0)
├── CONTRIBUTING.md
├── LICENSE
├── Makefile                           ← make check / examples / learner / project
├── .gitignore
├── .github/workflows/validate.yml     ← CI: docs + example checks
├── .devcontainer/devcontainer.json    ← ready-to-code environment
│
├── 00-programme-framework/
│   ├── vision-and-mission.md
│   ├── learning-philosophy.md
│   ├── competency-framework.md
│   └── assessment-framework.md
│
├── 01-grade-curriculum/
│   ├── grade-6/   (Discover Technology)
│   ├── grade-7/   (Develop Digital Competence)
│   ├── grade-8/   (Understand and Create)
│   ├── grade-9/   (Explore the Technology Ecosystem)
│   ├── grade-10/  (Discover Technology Pathways)
│   └── grade-11/  (Build and Specialize)
│
├── 02-foundation-modules/             (11 shared modules, revisited every grade)
├── 03-specialization-pathways/        (8 Grade 11 pathways)
├── 04-projects/                       (beginner → interdisciplinary)
├── 05-assessments/                    (quizzes, practical, assignments, rubrics)
├── 06-teacher-resources/              (lesson plans, guides, activities)
├── 07-learner-portfolio/              (passport and templates)
├── 08-resources/                      (tools, glossary, references)
├── 09-code-examples/                  (8 runnable pathway demonstrations)
├── 10-challenges/                     (progressive practice with self-tests)
├── 11-printable-activities/           (unplugged and paper worksheets)
└── scripts/                           (Python + Bash helpers and checks)
```

## Quick links

**Core documents**
- [Full Curriculum](TECH-PATH-CURRICULUM.md)
- [Programming & Pathway Development Framework](PROGRAMMING-FRAMEWORK.md) — the Kilele Build Cycle, grade progression, eight pathway demonstrations with code, and implementation phases

**Framework**
- [Vision and Mission](00-programme-framework/vision-and-mission.md)
- [Learning Philosophy](00-programme-framework/learning-philosophy.md)
- [Competency Framework](00-programme-framework/competency-framework.md)
- [Assessment Framework](00-programme-framework/assessment-framework.md)

**Grade curricula**
- [Grade 6](01-grade-curriculum/grade-6/curriculum.md) · [Grade 7](01-grade-curriculum/grade-7/curriculum.md) · [Grade 8](01-grade-curriculum/grade-8/curriculum.md) · [Grade 9](01-grade-curriculum/grade-9/curriculum.md) · [Grade 10](01-grade-curriculum/grade-10/curriculum.md) · [Grade 11](01-grade-curriculum/grade-11/curriculum.md)

**Other resources**
- [Foundation modules](02-foundation-modules/)
- [Specialization pathways](03-specialization-pathways/)
- [Projects](04-projects/)
- [Assessments](05-assessments/)
- [Teacher resources](06-teacher-resources/)
- [Teacher Guide to Python and Shell](06-teacher-resources/teaching-guides/python-and-shell-guide.md)
- [Learner portfolio](07-learner-portfolio/)
- [Tools, glossary and references](08-resources/)
- [Runnable code examples](09-code-examples/README.md) — all 8 demonstrations as runnable files
- [Progressive coding challenges](10-challenges/README.md) — guided, independent and creative practice with instant feedback
- [Printable activities](11-printable-activities/README.md) — unplugged lessons for low-resource classrooms
- [Repository scripts](scripts/README.md) — validation, example tests and scaffolding helpers

## Quick checks

```bash
bash scripts/setup-environment.sh   # check tools and create .venv
bash scripts/check-all.sh            # validate links, docs, examples and challenges
make check                           # same checks through the Makefile
```

Learner-facing tools:

```bash
bash scripts/run-challenges.sh       # test your challenge solutions
bash scripts/progress.sh             # progress report from your technology passport
bash scripts/pathway-explorer.sh     # discover preferred pathways (use --demo to preview)
```

Optional: `bash scripts/setup-environment.sh --with-ai` installs scikit-learn for the AI example.

## Guiding principles

1. Learning by doing
2. Understanding before memorization
3. Problem-solving before tool dependency
4. Creativity alongside technical knowledge
5. Responsible and ethical technology use
6. Collaboration and communication
7. Progressive learning complexity
8. Practical evidence of competence
9. Equal opportunity for technology discovery
10. Continuous exploration and improvement

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). curriculum changes are versioned following the scheme in the [full curriculum](TECH-PATH-CURRICULUM.md#243-version-control).

## Licence

Released under the [MIT License](LICENSE). © Kilele Archade and Synbree.

---

*Ideas. Software. Next.*
