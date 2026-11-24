# Challenge — Data Summary (Grade 11)

**Level 2: Independent Practice** · Concepts: statistics, validation, return values

## Task

Copy `starter.py` to `solution.py`, then complete:

- `summarize(values)` — return a dictionary with keys `count`, `min`, `max` and `mean` (mean rounded to 2 decimals). For an empty list, return `count: 0` and `None` for the other three values.
- `invalid_values(values)` — return a list of values that are not numbers between 0 and 100.

This challenge links the Data Science and Software Engineering pathways.

## Test

```bash
bash scripts/run-challenges.sh grade-11/data-summary
```

## Hints

1. Start with an empty result dictionary and fill each key.
2. `isinstance(value, (int, float))` checks whether a value is numeric.
3. Handle the empty-list case before calling `min()` or `max()`.

## Level 3 — Creative extension

Add `describe(values)` that returns a human-readable sentence including the count, range and average, and write a short note explaining why data validation matters before analysis.
