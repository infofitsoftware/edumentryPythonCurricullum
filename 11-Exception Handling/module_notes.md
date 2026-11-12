# Module 11 — Exception Handling

**For students (beginners)**  
**Prerequisites:** Modules 1–3 (basics, types, strings). Helpful if you have seen files or functions.  
**Size:** Small module — learn the idea, not every advanced pattern.

Read this slowly. Run `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

1. What an **exception** is  
2. Why exception handling matters in real programs  
3. How to use `try` / `except`  
4. How to catch common errors (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`)  
5. What `finally` is for (cleanup)  
6. Where this shows up: forms, files, APIs, and **database connections**

---

## 2. Why this module matters

Programs fail. Users type bad input. Files go missing. Databases are offline.

Without exception handling, one error can **crash the whole program**.

With exception handling, you can:

- show a clear message  
- ask the user to try again  
- log the problem  
- keep the rest of the app running  

| Real situation | What can go wrong |
|----------------|-------------------|
| Login form age field | User types `"twenty"` instead of `20` |
| Opening a file | File was deleted or wrong path |
| Division / calculator | Divide by zero |
| Calling an API | Network timeout / server down |
| Connecting to Postgres | Wrong password, DB not running |

**Golden rule:**  
If something **might** fail, wrap it in `try` / `except` and plan what to do next.

---

## 3. What is an exception?

An **exception** is an error that happens **while the program is running**.

Example:

```python
print(10 / 0)
```

Python stops and shows something like:

```text
ZeroDivisionError: division by zero
```

That message is useful for you (the developer).  
For users, a crash is usually not acceptable — so we **handle** the exception.

---

## 4. The basic pattern: `try` / `except`

```python
try:
    # risky code
    number = int("abc")
except ValueError:
    # what to do if that error happens
    print("Please enter a valid number.")
```

How to read it:

1. Python tries the code under `try`  
2. If that code raises a matching error, it jumps to `except`  
3. The program continues after the block instead of crashing  

---

## 5. Catch specific errors (best beginner habit)

Prefer catching the **exact** error you expect:

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Age must be a whole number.")
```

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

```python
try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found.")
```

Why specific is better:

- You understand **what** failed  
- You don’t accidentally hide unrelated bugs  

Beginner tip: if you are unsure of the name, run the code once and read the error type Python prints.

---

## 6. Show the error message (optional but useful)

```python
try:
    x = int("hello")
except ValueError as e:
    print("Something went wrong:", e)
```

`as e` lets you print the details. Helpful while learning and debugging.

---

## 7. `else` and `finally` (keep it simple)

```python
try:
    value = int("42")
except ValueError:
    print("Not a number")
else:
    print("Success:", value)   # runs only if try worked
finally:
    print("Done")              # runs always
```

| Block | When it runs |
|-------|----------------|
| `try` | Attempt the risky work |
| `except` | If a matching error happens |
| `else` | If **no** error happened |
| `finally` | Always — good for cleanup messages / closing resources |

You do **not** need all four every time.  
Most beginner code only needs `try` + `except`.

---

## 8. Real example 1 — safe number input

```python
raw = "twenty"   # imagine this came from input()
try:
    age = int(raw)
    print("Age is", age)
except ValueError:
    print("Invalid age. Please type digits only.")
```

This is the Module 2 casting bug — now handled safely.

---

## 9. Real example 2 — file missing

```python
try:
    with open("report.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("report.txt was not found. Check the filename.")
```

Very common in automation and data scripts.

---

## 10. Real example 3 — database connection (Postgres localhost)

In real apps, connecting to a database can fail for many reasons:

- PostgreSQL is not running  
- wrong password  
- wrong host/port  
- database name does not exist  

Example pattern using common **localhost learning credentials**:

```text
host: localhost
port: 5432
user: postgres
password: postgres
database: postgres
```

```python
try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="postgres",
        dbname="postgres",
    )
    print("Connected to Postgres")
    conn.close()
except ImportError:
    print("psycopg2 is not installed.")
except Exception as e:
    print("Could not connect to database:", e)
```

What to notice:

- The **idea** is more important than memorizing Postgres details  
- Connection code is “risky,” so it lives inside `try`  
- Failure should become a clear message, not a silent crash  

You do not need a live database to understand this module.  
`module.py` shows the same pattern safely.

---

## 11. Other places exception handling becomes important

| Area | Example failure |
|------|-----------------|
| Web / FastAPI | Bad request body, missing field |
| AI / LLM calls | API key missing, timeout, rate limit |
| File uploads | Wrong file type / file not found |
| Math / finance | Division by zero, bad conversions |
| Config loading | Missing `.env` or config key |
| Network requests | Server unreachable |

Same beginner skill every time: **try → catch → message / recovery**.

---

## 12. Common mistakes checklist

1. Catching everything and ignoring it (`except:` with `pass`) — hides bugs  
2. Using exceptions for normal logic when a simple `if` is enough  
3. Forgetting that `input()` returns text (casting can raise `ValueError`)  
4. Assuming files and databases always exist  
5. Copying AI code that crashes on the first bad input  

---

## 13. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict what happens before looking  
4. Do `module_exercises.md`  
5. Take `module_quiz.xml`  

If AI writes a `try` / `except` for you:

- Check which error it catches  
- Check the message is clear  
- Run a failing case on purpose  

---

## 14. Mini self-check

1. What is an exception?  
2. What do `try` and `except` do?  
3. Name three real places programs fail.  
4. Why wrap a Postgres connection in `try` / `except`?  

---

## 15. What “confident” means after Module 11

You can:

- explain why exception handling exists  
- write a basic `try` / `except`  
- handle common beginner errors safely  
- recognize database / file / input failures as exception cases  

Keep it simple. Master the basic pattern first. Advanced exception design comes later.
