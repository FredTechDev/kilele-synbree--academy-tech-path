# Worksheet — Algorithm Debug Hunt (Grades 8–11)

**Name:** ______________________ **Date:** ______________

## Goal

Find logical errors by tracing an algorithm with test data.

## Part A — Trace the algorithm

An algorithm is meant to classify a mark:

```
1. READ mark
2. IF mark >= 50 THEN
3.     PRINT "Pass"
4. ELSE
5.     PRINT "Fail"
6. PRINT "Grade A"
```

Complete the table by tracing each input.

| Input mark | What the algorithm prints | Correct? |
|---|---|---|
| 80 | ______________________ | Yes / No |
| 50 | ______________________ | Yes / No |
| 49 | ______________________ | Yes / No |

## Part B — Find the bug

What is wrong with the algorithm?

__________________________________________________________________

Rewrite the algorithm correctly:

```
1. ______________________________________________________________
2. ______________________________________________________________
3. ______________________________________________________________
4. ______________________________________________________________
```

## Part C — Test your fix

Give two test inputs you would use and the expected output.

| Test input | Expected output |
|---|---|
| __________ | ______________________ |
| __________ | ______________________ |

## Reflection

Why is testing with boundary values important?

__________________________________________________________________

## Teacher notes

- The bug is that line 6 always prints "Grade A" regardless of the mark.
- Reward learners who choose boundary tests (49, 50, 80) rather than only typical values.
- Connect to "Encourage Debugging" in the [Programming Framework](../PROGRAMMING-FRAMEWORK.md).
- Follow up with the [coding challenges](../10-challenges/README.md).
