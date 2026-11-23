"""Student Performance Analysis — Kilele TechPath, Pathway 2 (Data Science).

Introduces data organization, averages and basic interpretation.
Run with: python3 student-performance-analysis.py
"""

students = {
    "Amina": [78, 85, 90],
    "Brian": [65, 72, 70],
    "Cynthia": [88, 92, 95],
    "David": [55, 60, 58],
    "Eric": [70, 75, 80]
}


def analyze(records):
    print("STUDENT PERFORMANCE ANALYSIS")
    print("-----------------------------")

    class_total = 0
    student_count = len(records)

    for name, marks in records.items():
        average = sum(marks) / len(marks)
        class_total += average
        print(f"{name}: {average:.2f}")

    class_average = class_total / student_count

    print("-----------------------------")
    print(f"Class Average: {class_average:.2f}")
    return class_average


if __name__ == "__main__":
    analyze(students)
