# Runnable Code Examples

*The eight demonstration projects from [PROGRAMMING-FRAMEWORK.md](../PROGRAMMING-FRAMEWORK.md), provided as real files so learners can run, modify and test them.*

The framework presents these as **introductory demonstrations, not complete production systems**. Use them as a starting point, then complete the extension project in each pathway.

## Examples

| # | Pathway | Example | File | Grades |
|---|---|---|---|---|
| 1 | Software Engineering | Student Grade Calculator | [student-grade-calculator.py](01-software-engineering/student-grade-calculator.py) | 8–11 |
| 2 | Data Science | Student Performance Analysis | [student-performance-analysis.py](02-data-science/student-performance-analysis.py) | 9–11 |
| 3 | Cybersecurity | Password Strength Checker | [password-strength-checker.py](03-cybersecurity/password-strength-checker.py) | 9–11 |
| 4 | AI / ML | Classification Demonstration | [ml-classification.py](04-artificial-intelligence/ml-classification.py) | 10–11 |
| 5 | Robotics / IoT | Smart Irrigation Controller | [smart-irrigation.ino](05-robotics-iot/smart-irrigation.ino) | 10–11 |
| 6 | UI/UX | Interactive Learning Dashboard | [index.html](06-ui-ux-design/learning-dashboard/index.html) | 9–11 |
| 7 | Networking / Cloud | IP Address Information Tool | [ip-address-tool.py](07-networking-cloud/ip-address-tool.py) | 10–11 |
| 8 | Multimedia | Interactive Animated Art | [index.html](08-multimedia/interactive-art/index.html) | 9–11 |

## How to run

### Python examples (1, 2, 3, 7)

```bash
python3 01-software-engineering/student-grade-calculator.py
python3 02-data-science/student-performance-analysis.py
python3 03-cybersecurity/password-strength-checker.py
python3 07-networking-cloud/ip-address-tool.py
```

Examples 1, 3 and 7 ask for input in the terminal — use sample data, never real personal information.

### AI example (4)

```bash
pip install -r 04-artificial-intelligence/requirements.txt
python3 04-artificial-intelligence/ml-classification.py
```

If `scikit-learn` is not installed, the script prints install instructions instead of crashing. The dataset is tiny and for learning only — it must not be used for real decisions about learners.

### Electronics example (5)

Open the `.ino` file in Arduino IDE or Tinkercad Circuits. Read [the safety notes](05-robotics-iot/README.md) first.

### Web examples (6, 8)

Open the `index.html` files in a browser. The multimedia example loads p5.js from a CDN, so it needs internet access (or a local copy of p5.js for offline use).

## Automatic self-checks

Run all examples and check their output with:

```bash
bash scripts/run-examples.sh
```

This is also used by the repository CI. See [scripts/README.md](../scripts/README.md).

## Safety and ethics

- Use **sample or anonymized data** only. Never put real learner data in public repositories.
- The password checker is a simple complexity check — never enter a real password.
- Cybersecurity practice must stay in authorized, simulated environments.
- Electronics work must use low-voltage educational equipment and supervision.
- Isolate code execution environments; do not run learner-submitted code with full system privileges.

Related: [Programming Framework](../PROGRAMMING-FRAMEWORK.md) · [Teacher Guide to Python and Shell](../06-teacher-resources/teaching-guides/python-and-shell-guide.md) · [Pathways](../03-specialization-pathways/)
