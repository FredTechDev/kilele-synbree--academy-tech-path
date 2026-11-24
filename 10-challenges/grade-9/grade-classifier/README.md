# Challenge — Grade Classifier (Grade 9)

**Level 2: Independent Practice** · Concepts: conditions, boundary values, lists

## Task

Copy `starter.py` to `solution.py`, then complete:

- `classify_average(average)` — return a letter grade:
  - `80` and above → `A`
  - `70` to `79.99` → `B`
  - `60` to `69.99` → `C`
  - `50` to `59.99` → `D`
  - below `50` → `E`
- `class_average(marks)` — return the average rounded to 2 decimal places. Return `0` for an empty list.

Boundary values matter — check `80`, `70`, `60` and `50` carefully.

## Test

```bash
bash scripts/run-challenges.sh grade-9/grade-classifier
```

## Hints

1. Test the highest boundary first (`>= 80`), then work downwards.
2. `round(value, 2)` rounds to two decimal places.
3. Use `elif` so only one branch runs.

## Level 3 — Creative extension

Add `report(names, marks)` that returns a list of `"Name: average (grade)"` strings, then write a short explanation of why boundary order matters.
