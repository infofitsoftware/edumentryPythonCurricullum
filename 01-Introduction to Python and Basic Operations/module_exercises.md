# Module 1 — Practice Exercises (AI-Era Track)

**Mindset:** TRACE → PREDICT → RUN → VERIFY  
If you use AI for help, you must still explain every line.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — First Script

**Difficulty:** Easy  
**Concepts:** script, print  

**Problem:** Create `hello.py` that prints `Python is installed successfully!` and run it.

**Expected Output:**
```
Python is installed successfully!
```

**Hint:** `python hello.py`

---

### Exercise 2 — Log-Style Prints

**Difficulty:** Easy  
**Concepts:** print  

**Problem:** Print these three lines exactly:

```
[INFO] server starting
[INFO] routes loaded
[INFO] ready
```

**Real-world link:** FastAPI / backend startup logs.

---

### Exercise 3 — sep and end

**Difficulty:** Easy  
**Concepts:** print kwargs  

**Problem:**

1. Print `2026-11-12` using `sep="-"`  
2. Print `Loading...Done` using `end=`

---

### Exercise 4 — Arithmetic Pack

**Difficulty:** Easy  
**Concepts:** operators  

**Problem:** For `a=17`, `b=5`, print results of `+ - * / // % **` with labels.

---

### Exercise 5 — Predict Then Run

**Difficulty:** Easy  
**Concepts:** tracing  

**Problem:** Without running first, write your prediction as a comment, then run:

```python
print(15 // 4)
print(15 % 4)
print(2 ** 5)
```

---

# LEVEL 2 — APPLY

### Exercise 6 — Batching Math (AI / Jobs)

**Difficulty:** Medium  
**Concepts:** `//`, `%`  

**Problem:** You have `items = 50` and `batch_size = 16`.  
Print full batches and leftover.

**Expected Output:**
```
3
2
```

**Real-world link:** AI training batches, queue workers, file upload chunks.

---

### Exercise 7 — Token Cost Estimate

**Difficulty:** Medium  
**Concepts:** `*`  

**Problem:** `tokens = 2500`, `price_per_token = 0.000003`.  
Print estimated cost.

**Expected Output:**
```
0.0075
```

**Real-world link:** LLM API billing estimates.

---

### Exercise 8 — Pagination Offset

**Difficulty:** Medium  
**Concepts:** arithmetic  

**Problem:** `page = 4`, `page_size = 25`.  
Print offset using `(page - 1) * page_size`.

**Expected Output:**
```
75
```

**Real-world link:** FastAPI list endpoints / database LIMIT-OFFSET.

---

### Exercise 9 — Greeting Card

**Difficulty:** Easy  
**Concepts:** input, print  

**Problem:** Ask for name and city. Print:

`Welcome <name> from <city>!`

**Hint:** `input()` returns str — concatenation/commas are fine.

---

### Exercise 10 — Fix the Trap

**Difficulty:** Medium  
**Concepts:** input casting preview  

**Problem:** Ask for two numbers and print their **numeric** sum, difference, product, quotient.

**Hint:** `int(...)` (Module 2 covers casting deeply).

---

# LEVEL 3 — COMBINE + CAREER SHAPE

### Exercise 11 — Fake API Response

**Difficulty:** Medium  
**Concepts:** print formatting  

**Problem:** Ask for `username`. Print:

```
status: ok
user: <username>
message: authenticated
```

**Real-world link:** shape of a FastAPI JSON response (text form today).

---

### Exercise 12 — AI Job Status Logger

**Difficulty:** Medium  
**Concepts:** print, sep/end  

**Problem:** Print a mini pipeline log:

```
[JOB] embed:start
[JOB] embed:done
[JOB] tokens=128
```

Use variables for job name and token count.

---

### Exercise 13 — Receipt Lite

**Difficulty:** Medium  
**Concepts:** input, float/int, arithmetic  

**Problem:** Ask item price (float) and quantity (int). Print line total.

**Example Input:** `99.5` and `2` → `199.0`

---

### Exercise 14 — Debug an AI Draft

**Difficulty:** Challenging  
**Concepts:** errors, verification  

**Problem:** An AI wrote this broken code. Fix it and explain the bug in a comment:

```python
age = input("Age: ")
print("Next year you will be " + age + 1)
```

**Expected behavior:** if age is 20, print that next year is 21.

---

### Exercise 15 — Comment Quality

**Difficulty:** Easy  
**Concepts:** comments  

**Problem:** Write 5–8 lines that compute leftover items after boxing.  
Include at least two useful WHY comments (not "add numbers").

---

# LEVEL 4 — PROBLEM SOLVING / INTERVIEW

### Exercise 16 — Even Batch Check

**Difficulty:** Medium  
**Concepts:** `%`  

**Problem:** Ask for an integer `n`. Print `Even leftover` if `n % 4 == 0` else `Odd pattern`  
(Use a simple `if` preview if needed.)

---

### Exercise 17 — Mini Dashboard

**Difficulty:** Challenging  
**Concepts:** print, arithmetic, variables  

**Problem:** Hard-code:

- `requests = 1200`  
- `errors = 36`  

Print:

```
requests=1200
errors=36
error_rate_percent=<errors/requests*100>
```

Round not required; printing the float is fine.

**Real-world link:** API monitoring dashboards.

---

### Exercise 18 — Verify AI Output Challenge

**Difficulty:** Challenging  
**Concepts:** tracing  

**Problem:** Ask any AI:

> "Write a Python snippet that prints numbers of full teams of 7 from 52 people and remainder."

Then:

1. Paste the AI code into a file  
2. Trace expected output yourself  
3. Run and confirm  
4. Write 3 lines: what was correct / wrong / what you changed  

---

### Exercise 19 — Personal Intro CLI

**Difficulty:** Medium  
**Concepts:** input, print  

**Problem:** Ask name, goal role (`AI Engineer` / `Backend` / etc.), and years of study.  
Print a 4-line profile card.

---

### Exercise 20 — Confidence Checklist Script

**Difficulty:** Easy  
**Concepts:** print  

**Problem:** Print a checklist of 5 Module 1 skills you can now do, each prefixed with `[ ]` or `[x]`.

---

# Instructor Solution Guide

```python
# Exercise 1
print("Python is installed successfully!")

# Exercise 2
print("[INFO] server starting")
print("[INFO] routes loaded")
print("[INFO] ready")

# Exercise 3
print("2026", "11", "12", sep="-")
print("Loading", end="...")
print("Done")

# Exercise 4
a, b = 17, 5
print("add", a + b)
print("sub", a - b)
print("mul", a * b)
print("div", a / b)
print("floor", a // b)
print("mod", a % b)
print("pow", a ** b)

# Exercise 5
print(15 // 4)  # 3
print(15 % 4)   # 3
print(2 ** 5)   # 32

# Exercise 6
items, batch_size = 50, 16
print(items // batch_size)
print(items % batch_size)

# Exercise 7
tokens = 2500
price_per_token = 0.000003
print(tokens * price_per_token)

# Exercise 8
page, page_size = 4, 25
print((page - 1) * page_size)

# Exercise 9
name = input("Name: ")
city = input("City: ")
print("Welcome", name, "from", city + "!")

# Exercise 10
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Exercise 11
username = input("Username: ")
print("status: ok")
print("user:", username)
print("message: authenticated")

# Exercise 12
job = "embed"
tokens = 128
print(f"[JOB] {job}:start")
print(f"[JOB] {job}:done")
print(f"[JOB] tokens={tokens}")

# Exercise 13
price = float(input("Price: "))
qty = int(input("Qty: "))
print(price * qty)

# Exercise 14
age = int(input("Age: "))
print("Next year you will be", age + 1)
# Bug was: string + int without casting / wrong concatenation

# Exercise 15
total = 23
size = 4
# WHY: // gives complete boxes only
print(total // size)
# WHY: % tells how many items remain unpacked
print(total % size)

# Exercise 16
n = int(input("n: "))
if n % 4 == 0:
    print("Even leftover")
else:
    print("Odd pattern")

# Exercise 17
requests = 1200
errors = 36
print("requests=", requests, sep="")
print("errors=", errors, sep="")
print("error_rate_percent=", errors / requests * 100, sep="")

# Exercise 18 — student reflection (no single code solution)

# Exercise 19
name = input("Name: ")
role = input("Goal role: ")
years = input("Years studying: ")
print("-----")
print("Name:", name)
print("Goal:", role)
print("Years:", years)
print("-----")

# Exercise 20
print("[x] Run Python scripts")
print("[x] Use print for debugging")
print("[x] Use arithmetic for metrics")
print("[x] Know input returns str")
print("[x] Read basic errors")
```
