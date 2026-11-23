"""Machine Learning Classification — Kilele TechPath, Pathway 4 (AI/ML).

Educational demonstration only. The small dataset is not suitable for real
educational decisions. Install the dependency with:
    pip install -r requirements.txt
Then run with: python3 ml-classification.py
"""

# Training information:
# [Study hours, Attendance percentage]

features = [
    [1, 50],
    [2, 60],
    [3, 65],
    [4, 75],
    [5, 85],
    [6, 90],
    [7, 95]
]

# 0 = Needs support
# 1 = Demonstrating progress

labels = [
    0, 0, 0, 1, 1, 1, 1
]


def build_and_predict(study_hours, attendance):
    from sklearn.tree import DecisionTreeClassifier

    model = DecisionTreeClassifier(random_state=42)
    model.fit(features, labels)
    return model.predict([[study_hours, attendance]])[0]


def main():
    study_hours = 4
    attendance = 80

    try:
        prediction = build_and_predict(study_hours, attendance)
    except ImportError:
        print("scikit-learn is not installed in this environment.")
        print("Install it with: pip install -r requirements.txt")
        return

    print("LEARNING PROGRESS DEMONSTRATION")
    print("--------------------------------")

    if prediction == 1:
        print("The model predicts: Demonstrating progress")
    else:
        print("The model predicts: May need additional support")


if __name__ == "__main__":
    main()
