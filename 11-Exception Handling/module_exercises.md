# Module 11 — Practice Exercises: Exception Handling

**For students**

1. Read `module_notes.md`  
2. Run `module.py`  
3. Solve these short exercises  
4. Predict before you run  

**Difficulty:** [E] Easy · [M] Medium  

This is a small module — keep solutions short.

---

## A. Core try / except

### A1. [E] Catch ZeroDivisionError
Write code that tries `print(8 / 0)` and catches `ZeroDivisionError` with a clear message.

### A2. [E] Catch ValueError
Convert `"hello"` with `int(...)` inside `try` / `except ValueError`.

### A3. [E] Good path + bad path
Try `int("25")` and `int("twenty")` in two separate try blocks. Print success or error for each.

### A4. [M] Print the error object
Catch a `ValueError` using `except ValueError as e` and print `e`.

---

## B. Real situations

### B1. [E] Missing file
Try to open `"notes_missing.txt"` for reading. Catch `FileNotFoundError`.

### B2. [M] Safe age input (simulated)
```python
raw = "abc"   # pretend user typed this
```
Convert to int safely. If valid, print `Next year: <age+1>`. If invalid, print a helpful message.

### B3. [M] Safe divide function
Write `safe_divide(a, b)` that returns the result or the string `"cannot divide"`.

Test with `(9, 3)` and `(9, 0)`.

### B4. [M] Postgres connection mindset
Using these localhost values:

```text
host=localhost
port=5432
user=postgres
password=postgres
dbname=postgres
```

Write a `try` / `except` block that:

1. tries to `import psycopg2` and connect  
2. catches `ImportError` with message about installing the package  
3. catches a general `Exception` and prints that connection failed  
4. prints `"program still running"` afterward  

You do **not** need a live database for full marks — the pattern matters.

---

## C. Short written answers (as comments)

### C1. Why is exception handling important?
Answer:

### C2. Name three real places programs can fail.
Answer:

### C3. Why catch `ValueError` for `int(input(...))`?
Answer:

### C4. Why wrap a database connect call in try/except?
Answer:

---

## Done?

Rerun `module.py`, then take `module_quiz.xml`.
