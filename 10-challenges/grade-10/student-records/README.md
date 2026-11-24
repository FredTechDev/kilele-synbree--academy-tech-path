# Challenge — Student Records (Grade 10)

**Level 2: Independent Practice** · Concepts: dictionaries, lists, filtering, averages

## Task

Copy `starter.py` to `solution.py`, then complete:

- `average_for(record)` — average of `record["marks"]`, rounded to 2 decimals.
- `top_student(records)` — name of the student with the highest average, or `None` if the list is empty.
- `passing_students(records, threshold)` — list of names whose average is at least `threshold`, in the same order as the records.

A record looks like this:

```python
{"name": "Amina", "marks": [78, 85, 90]}
```

## Test

```bash
bash scripts/run-challenges.sh grade-10/student-records
```

## Hints

1. Use `record["name"]` and `record["marks"]`.
2. Build a result list with `.append()` and return it.
3. Track the best average in a variable while looping.

## Level 3 — Creative extension

Add `add_student(records, name, marks)` that validates marks are between 0 and 100 before adding a record, and `report(records)` that returns a formatted table of names and averages.
