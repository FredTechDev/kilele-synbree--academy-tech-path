# Learner Portfolio Folders

This folder holds **generated learner workspaces**. Do not create these by hand — use the scripts:

```bash
bash scripts/new-learner.sh "Amina Otieno" grade-8 "Mr Kamau"
bash scripts/new-project.sh "Grade Calculator" grade-8 amina-otieno
```

Each learner folder contains:

- `technology-passport.md` — the learner's progress record
- `reflection.md` — reflection template
- `projects/<project-name>/README.md` — project documentation
- `projects/<project-name>/src/` — source files

## Privacy

Learner folders are ignored by Git by default (see `.gitignore`) because they may contain personal information. Only commit **anonymized sample learners** for demonstration purposes, and only with permission.

- Use fictional names for shared examples.
- Never store real passwords, account credentials or sensitive learner data.
- Verify outputs before publishing screenshots or demonstration videos.

Related: [Scripts](../../scripts/README.md) · [Technology Passport](../technology-passport.md)
