#!/usr/bin/env python3
"""Help a learner discover preferred technology pathways.

Asks eight short interest questions and suggests two pathways to explore.
This guides exploration — it does not assign a learner to a career.
Use --demo to run with sample answers without interaction.
"""

from __future__ import annotations

import sys

PATHWAYS = [
    ("Software Engineering", "Building an app that solves a school problem",
     "03-specialization-pathways/software-engineering/README.md",
     "09-code-examples/01-software-engineering/student-grade-calculator.py"),
    ("Data Science and Analytics", "Finding patterns and trends in a dataset",
     "03-specialization-pathways/data-science/README.md",
     "09-code-examples/02-data-science/student-performance-analysis.py"),
    ("Cybersecurity", "Finding weaknesses in a practice system and defending it",
     "03-specialization-pathways/cybersecurity/README.md",
     "09-code-examples/03-cybersecurity/password-strength-checker.py"),
    ("Artificial Intelligence", "Training a model to recognize images or make predictions",
     "03-specialization-pathways/artificial-intelligence/README.md",
     "09-code-examples/04-artificial-intelligence/ml-classification.py"),
    ("Robotics and IoT", "Building a sensor-based device or robot",
     "03-specialization-pathways/robotics-iot/README.md",
     "09-code-examples/05-robotics-iot/smart-irrigation.ino"),
    ("UI/UX and Design", "Designing a friendly, accessible interface",
     "03-specialization-pathways/ui-ux-design/README.md",
     "09-code-examples/06-ui-ux-design/learning-dashboard/index.html"),
    ("Networking and Cloud", "Setting up a network or hosting a website",
     "03-specialization-pathways/networking-cloud/README.md",
     "09-code-examples/07-networking-cloud/ip-address-tool.py"),
    ("Multimedia and Creative Technology", "Creating animation, video or digital art",
     "03-specialization-pathways/multimedia/README.md",
     "09-code-examples/08-multimedia/interactive-art/index.html"),
]


def ask() -> dict[str, int]:
    scores: dict[str, int] = {}
    print("Rate each activity from 1 (not for me) to 5 (very interesting).")
    print()
    for number, (name, activity, _, _) in enumerate(PATHWAYS, 1):
        while True:
            answer = input(f"{number}. {activity}: ").strip()
            if answer.isdigit() and 1 <= int(answer) <= 5:
                scores[name] = int(answer)
                break
            print("   Please enter a number from 1 to 5.")
        print()
    return scores


def demo_scores() -> dict[str, int]:
    sample = [5, 4, 2, 3, 4, 5, 3, 5]
    return {entry[0]: score for entry, score in zip(PATHWAYS, sample)}


def main() -> int:
    print("Kilele TechPath — Pathway Explorer")
    print("==================================")
    print("These results guide exploration. They do not assign you to a career.")
    print("You can change your preferred pathway at any time.")
    print()

    scores = demo_scores() if "--demo" in sys.argv else ask()
    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    details = {name: (activity, link, example) for name, activity, link, example in PATHWAYS}

    print("Your strongest interests")
    print("-----------------------")
    for rank, (name, score) in enumerate(ranked[:3], 1):
        activity, link, _ = details[name]
        print(f"{rank}. {name} ({score}/5) — {activity}")
        print(f"   Explore: {link}")

    first, second = ranked[0][0], ranked[1][0]
    print()
    print("Suggested combination")
    print("---------------------")
    print(f"Primary pathway: {first}")
    print(f"Complementary pathway: {second}")
    print("Combinations stay flexible — try both before deciding.")
    print()
    print("Start with an example:", details[first][2])
    print("Reflect afterwards: 07-learner-portfolio/reflection-template.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
