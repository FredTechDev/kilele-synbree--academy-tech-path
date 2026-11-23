"""Student Grade Calculator — Kilele TechPath, Pathway 1 (Software Engineering).

Introduces variables, user input, arithmetic, conditions and functions.
Run with: python3 student-grade-calculator.py
"""


def calculate_average(marks):
    return sum(marks) / len(marks)


def determine_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


def main():
    student_name = input("Enter student name: ")

    marks = []

    for subject in range(1, 4):
        mark = float(input(f"Enter mark for subject {subject}: "))

        if mark < 0 or mark > 100:
            print("Invalid mark. Enter a value between 0 and 100.")
            break

        marks.append(mark)

    if len(marks) == 3:
        average = calculate_average(marks)
        grade = determine_grade(average)

        print("\nSTUDENT REPORT")
        print("--------------------")
        print("Student:", student_name)
        print("Average:", round(average, 2))
        print("Grade:", grade)


if __name__ == "__main__":
    main()
