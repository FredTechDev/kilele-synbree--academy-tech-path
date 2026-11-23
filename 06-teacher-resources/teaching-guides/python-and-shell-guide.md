# Teacher Guide to Python and Shell

*Kilele TechPath — practical tooling for teachers and learners*

This guide explains where Python and the shell help in the programme, how to set up a classroom environment, and how to use the repository scripts that support teaching.

## 1. Where Python helps

Python is the main text-based programming language from Grade 8 onward.

| Grade | Classroom use of Python |
|---|---|
| 8 | First programs — `print()`, `input()`, variables, arithmetic, conditions, loops, simple calculators and quizzes |
| 9 | Lists, dictionaries, functions, error handling; grade management and data analysis |
| 10 | File handling, exceptions, OOP introduction, APIs, data analysis, AI and networking demonstrations |
| 11 | Capstones in Software Engineering, Data Science, AI, Cybersecurity and Networking |

The [runnable examples](../../09-code-examples/README.md) cover five Python demonstrations from the [Programming Framework](../../PROGRAMMING-FRAMEWORK.md):

1. Student Grade Calculator (Software Engineering)
2. Student Performance Analysis (Data Science)
3. Password Strength Checker (Cybersecurity)
4. Machine Learning Classification (AI)
5. IP Address Information Tool (Networking)

## 2. Where the shell helps

The shell (Bash on Linux/macOS, PowerShell or Git Bash on Windows) is used for:

- Running programs: `python3 script.py`
- Installing packages: `pip install -r requirements.txt`
- Moving around folders: `cd`, `ls`, `pwd`
- Version control: `git status`, `git add`, `git commit`, `git push`
- Environment setup: virtual environments, lab provisioning, deployment
- Repository maintenance: checking links, testing examples, scaffolding learner folders

Learners meet shell commands naturally around Grades 9–10 through Git and running scripts. It is a **supporting tool**, not a separate programming subject.

## 3. Setting up

### Option A — local environment

```bash
bash scripts/setup-environment.sh
```

This checks for `python3`, `git` and `bash`, then creates a `.venv` virtual environment. To also install the AI dependency:

```bash
bash scripts/setup-environment.sh --with-ai
```

### Option B — VS Code Dev Container

Open the repository in VS Code and choose **Reopen in Container**. The `.devcontainer` configuration provides Python 3.12, Node.js and useful extensions, then runs the checks automatically.

### Option C — low-resource classrooms

- Use locally installed Python (Thonny is beginner-friendly).
- Use offline editors and pre-downloaded files.
- Use unplugged algorithm activities and printed code listings.
- The AI example reports a clear install message if scikit-learn is absent — the rest of the examples still run.

## 4. Running and checking the examples

```bash
bash scripts/run-examples.sh     # run all examples with sample input
bash scripts/validate-links.sh   # check internal documentation links
bash scripts/check-all.sh        # run everything
```

Or use `make`:

```bash
make check
make examples
```

The output uses three states:

- **PASS** — the example produced the expected output.
- **SKIP** — an optional dependency is missing; install it with its `requirements.txt`.
- **FAIL** — something is wrong; read the message and investigate.

## 5. Essential commands for teachers

| Task | Command |
|---|---|
| Show current folder | `pwd` |
| List files | `ls` |
| Change folder | `cd 09-code-examples` |
| Run a Python file | `python3 01-software-engineering/student-grade-calculator.py` |
| Create a virtual environment | `python3 -m venv .venv` |
| Install a package | `python3 -m pip install scikit-learn` |
| Check Git status | `git status` |
| Save a change | `git add . && git commit -m "message"` |
| Send to GitHub | `git push` |
| Run all checks | `bash scripts/check-all.sh` |

## 6. A beginner Python refresher

```python
name = input("Enter your name: ")   # input
marks = [80, 90, 100]                # collection
average = sum(marks) / len(marks)    # calculation

if average >= 80:                    # condition
    print(name, "Grade A")
else:
    print(name, "Keep practising")

for mark in marks:                   # loop
    print(mark)
```

Connect every concept to a real problem from the learner's environment — marks, attendance, inventory, rainfall or soil moisture.

## 7. Common errors and what to say

| Error | Likely cause | Teaching response |
|---|---|---|
| `ModuleNotFoundError` | Package not installed | Read the install message; use `pip install -r requirements.txt`. |
| `SyntaxError` | Missing bracket, colon or quote | Ask the learner to read the highlighted line aloud. |
| `IndentationError` | Wrong spacing | Show that Python uses indentation to group code. |
| `command not found` | Typo or tool not installed | Check spelling and run `bash scripts/setup-environment.sh`. |
| `Permission denied` | Script not executable | Run with `bash script.sh` instead of `./script.sh`. |
| Program gives wrong answer | Logical error | Ask the learner to print intermediate values and test with known inputs. |

Errors are part of learning. Guide learners to investigate the cause rather than correcting every error for them.

## 8. Debugging routine to teach

1. Read the error message from the bottom upwards.
2. Identify the file and line number.
3. Print the values of variables near that line.
4. Test with a small, known input.
5. Change **one thing** and run again.
6. Record the fix in the project README.

## 9. Version control in the classroom

- Start with simple "save a copy" and named versions for younger learners.
- Introduce `git init`, `git add`, `git commit` in Grade 9.
- Add branches, pull requests and code review in Grades 10–11.
- Keep personal learner data out of public repositories — learner folders are ignored by Git for this reason.

## 10. Safety and ethics

- Never enter real passwords into the password checker example.
- Use synthetic or anonymized data only.
- Cybersecurity work must use authorized, isolated environments.
- Do not run learner-submitted code with full system privileges; use a sandbox or isolated environment.
- The AI demonstration uses a tiny dataset and must not inform real decisions about learners.
- Verify AI-generated code before using it and maintain academic integrity.

## 11. Assessment connection

These tools support the assessment framework in the [Programming Framework](../../PROGRAMMING-FRAMEWORK.md):

- **Guided practical exercises** — reproduce the examples.
- **Independent coding challenges** — modify one example to solve a new problem.
- **Project development** — scaffold with `new-project.sh` and document in the project README.
- **Reflection and improvement** — use the [reflection template](../../07-learner-portfolio/reflection-template.md).

Assessment should reward reasoning, testing and improvement — not just how quickly code is written.

## Related documents

- [Runnable Code Examples](../../09-code-examples/README.md)
- [Repository Scripts](../../scripts/README.md)
- [Teaching Guides](../teaching-guides/README.md)
- [Lesson Plan Template](../lesson-plans/README.md)
- [Programming Framework](../../PROGRAMMING-FRAMEWORK.md)
