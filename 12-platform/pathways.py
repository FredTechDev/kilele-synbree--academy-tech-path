"""Pathway metadata for the platform. Mirrors scripts/tools/pathway_explorer.py."""

PATHWAYS = [
    {
        "name": "Software Engineering",
        "activity": "Building an app that solves a school problem",
        "link": "03-specialization-pathways/software-engineering/README.md",
        "example": "09-code-examples/01-software-engineering/student-grade-calculator.py",
    },
    {
        "name": "Data Science and Analytics",
        "activity": "Finding patterns and trends in a dataset",
        "link": "03-specialization-pathways/data-science/README.md",
        "example": "09-code-examples/02-data-science/student-performance-analysis.py",
    },
    {
        "name": "Cybersecurity",
        "activity": "Finding weaknesses in a practice system and defending it",
        "link": "03-specialization-pathways/cybersecurity/README.md",
        "example": "09-code-examples/03-cybersecurity/password-strength-checker.py",
    },
    {
        "name": "Artificial Intelligence",
        "activity": "Training a model to recognize images or make predictions",
        "link": "03-specialization-pathways/artificial-intelligence/README.md",
        "example": "09-code-examples/04-artificial-intelligence/ml-classification.py",
    },
    {
        "name": "Robotics and IoT",
        "activity": "Building a sensor-based device or robot",
        "link": "03-specialization-pathways/robotics-iot/README.md",
        "example": "09-code-examples/05-robotics-iot/smart-irrigation.ino",
    },
    {
        "name": "UI/UX and Design",
        "activity": "Designing a friendly, accessible interface",
        "link": "03-specialization-pathways/ui-ux-design/README.md",
        "example": "09-code-examples/06-ui-ux-design/learning-dashboard/index.html",
    },
    {
        "name": "Networking and Cloud",
        "activity": "Setting up a network or hosting a website",
        "link": "03-specialization-pathways/networking-cloud/README.md",
        "example": "09-code-examples/07-networking-cloud/ip-address-tool.py",
    },
    {
        "name": "Multimedia and Creative Technology",
        "activity": "Creating animation, video or digital art",
        "link": "03-specialization-pathways/multimedia/README.md",
        "example": "09-code-examples/08-multimedia/interactive-art/index.html",
    },
]


def recommend(scores: dict[str, int]) -> tuple[str, str]:
    """Return the two highest-scoring pathway names."""
    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    return ranked[0][0], ranked[1][0]
