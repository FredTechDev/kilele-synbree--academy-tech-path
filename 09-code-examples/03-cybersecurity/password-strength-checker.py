"""Password Strength Checker — Kilele TechPath, Pathway 3 (Cybersecurity).

An educational complexity checker. Never enter a real password into a
classroom demonstration. Run with: python3 password-strength-checker.py
"""

import string


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    if score == 5:
        result = "Meets the basic complexity checks"
    elif score >= 3:
        result = "Needs improvement"
    else:
        result = "Weak"

    return result, suggestions


def main():
    password = input("Enter a sample password to evaluate: ")
    result, suggestions = check_password(password)

    print("\nPASSWORD ASSESSMENT")
    print("-------------------")
    print("Result:", result)

    for suggestion in suggestions:
        print("-", suggestion)


if __name__ == "__main__":
    main()
