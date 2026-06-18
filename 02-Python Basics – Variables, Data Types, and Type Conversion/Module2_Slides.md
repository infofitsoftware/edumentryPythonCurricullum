# Module 2: Variables, Data Types, and Type Conversion

**Course:** edumentry Python Fundamentals  
**Duration:** ~2–3 hours (lecture + lab)  
**Prerequisites:** Module 1 — print(), input(), basic arithmetic

---

## Slide 1 — Welcome

### Python Basics: Variables, Data Types & Type Conversion

**Module 1 recap:** You ran Python, used `print()` and `input()`.

**Today:** Store data in variables, understand types, and convert between them.

> Every backend API, ML pipeline, and automation script builds on this module.

---

## Slide 2 — Learning Objectives

By the end of this module you will:

1. Create variables and follow **PEP 8** naming (`snake_case`)
2. Use **int, float, str, bool, None**
3. Check types with `type()` and `isinstance()`
4. Cast with `int()`, `float()`, `str()`, `bool()`
5. Fix the **`input()` + math** bug permanently
6. Use **f-strings** to display formatted output

---

## Slide 3 — What is a Variable?

A **variable** = a name that refers to a value in memory.

```python
name = "Alice"
age = 25
```

| Concept | Meaning |
|---------|---------|
| `name` | Variable (label) |
| `"Alice"` | Value (data) |
| `=` | Assignment operator |

You do **not** write `str name` in Python — the type is inferred.

---

## Slide 4 — Dynamic Typing

Python is **dynamically typed**:

```python
x = 10        # x is int
x = "hello"   # x is now str — allowed!
```

| Python | Java / C++ |
|--------|------------|
| Type follows value | Type declared once |
| Flexible | Strict |

**Career link:** JSON from APIs arrives as strings — you cast before math.

---

## Slide 5 — Variable Naming Rules

| Rule | Example |
|------|---------|
| Start with letter or `_` | `_count`, `total` |
| Then letters, digits, `_` | `user_id_2` |
| Case-sensitive | `Age` ≠ `age` |
| No keywords | `if`, `class`, `import` |

**PEP 8 style:** `snake_case` for variables

```python
user_name = "Sara"      # ✅
userName = "Sara"       # works, but not Pythonic
```

---

## Slide 6 — Invalid Names (Don't Do This)

```python
# 2name = "x"       # ❌ starts with digit
# my-var = 5        # ❌ hyphen = minus
# if = 10           # ❌ reserved keyword
```

These cause **`SyntaxError`** before your program even runs.

---

## Slide 7 — Constants (By Convention)

Python has no `const` keyword. Use **ALL_CAPS**:

```python
PI = 3.14159
MAX_USERS = 100
DEFAULT_PORT = 8000
```

Signals to teammates: **don't reassign this**.

Used in DevOps configs, API limits, and ML hyperparameters.

---

## Slide 8 — Assignment Tricks

**Multiple assignment:**
```python
x, y, z = 1, 2, 3
```

**Swap without temp variable:**
```python
a, b = 10, 20
a, b = b, a    # a=20, b=10
```

**Reassignment:**
```python
score = 90
score = 95.5   # type can change too
```

---

## Slide 9 — The Five Core Types

| Type | Example | Use case |
|------|---------|----------|
| `int` | `42`, `-7` | Counts, IDs, ages |
| `float` | `3.14`, `2.0` | Prices, metrics, ML features |
| `str` | `"Hello"` | Names, messages, JSON text |
| `bool` | `True`, `False` | Flags, conditions |
| `NoneType` | `None` | Missing / optional values |

```python
print(type(42))       # <class 'int'>
print(type("hello"))  # <class 'str'>
```

---

## Slide 10 — int and float

```python
age = 25              # int
price = 19.99         # float
temperature = 37.0    # float (has decimal point)
```

**Watch out:**
```python
print(0.1 + 0.2)   # 0.30000000000000004
```

Important in **finance** and **data science** — use `round()` or `decimal` later.

**Division reminder (Module 1):**
```python
10 / 4    # 2.5  (float)
10 // 4   # 2    (int floor)
```

---

## Slide 11 — str (Strings)

Text in single or double quotes:

```python
name = "Alice"
city = 'Mumbai'
```

Strings are **immutable** (can't change in place) — Module 3 goes deeper.

**Concatenation:**
```python
"Hello" + " " + "World"   # "Hello World"
"5" + "3"                 # "53"  ← not 8!
```

---

## Slide 12 — bool (Booleans)

Only two values: `True` and `False` (capital T and F!)

```python
is_active = True
has_error = False
```

**Truthy / Falsy** (used in `if` statements — Module 5):

| Falsy | Truthy |
|-------|--------|
| `0`, `0.0` | Any non-zero number |
| `""` | Non-empty strings |
| `None` | Most other values |
| `False` | `True` |

```python
bool(0)       # False
bool("hi")    # True
```

---

## Slide 13 — None — "No Value"

```python
middle_name = None
email = None
```

Means: **not set**, **optional**, **missing data**.

| Domain | Example |
|--------|---------|
| Backend | Optional profile field |
| Database | NULL → `None` in Python |
| Data Science | Missing sensor reading |

**Check with:** `if value is None:` (preferred style)

---

## Slide 14 — type() vs isinstance()

```python
x = 42
type(x)              # <class 'int'>  — for debugging
isinstance(x, int)   # True           — preferred in production
```

**isinstance with multiple types:**
```python
isinstance(3.14, (int, float))   # True
```

Backend validation pattern:
```python
if isinstance(user_id, str) and user_id.isdigit():
    user_id = int(user_id)
```

---

## Slide 15 — Type Casting Overview

| Function | Converts to | Example |
|----------|-------------|---------|
| `int(x)` | Integer | `int(3.9)` → `3` |
| `float(x)` | Float | `float("10")` → `10.0` |
| `str(x)` | String | `str(123)` → `"123"` |
| `bool(x)` | Boolean | `bool(0)` → `False` |

Casting = **explicit conversion** when you need a different type.

---

## Slide 16 — Casting Examples

```python
str(100)        # "100"
int("42")       # 42
float("3.14")   # 3.14
int(7.8)        # 7  (truncates, does NOT round)
bool("")        # False
bool("text")    # True
```

**Danger:**
```python
int("hello")    # ValueError!
int("10.5")     # ValueError!  use float() first
```

Always **validate** user input in real apps.

---

## Slide 17 — The input() Trap (Again)

```python
a = input("First: ")   # user types 5  →  a = "5"
b = input("Second: ")  # user types 3  →  b = "3"
print(a + b)           # "53"  ❌
```

**Fix:**
```python
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)           # 8  ✅
```

For decimals: `float(input(...))`

---

## Slide 18 — Real Calculator Pattern

```python
price = float(input("Price: "))
qty = int(input("Quantity: "))
total = price * qty
print("Total:", total)
```

Same pattern everywhere:

```
input (str) → cast → compute → output
```

Automation scripts, billing systems, ML data loaders.

---

## Slide 19 — f-strings (Formatted Output)

Embed variables directly in text:

```python
name = "Ravi"
score = 87.5
print(f"{name} scored {score}%")
```

**Formatting numbers:**
```python
pi = 3.14159
print(f"Pi: {pi:.2f}")      # Pi: 3.14
emp_id = 42
print(f"EMP-{emp_id:05d}")  # EMP-00042
```

Used in logging, reports, API responses.

---

## Slide 20 — Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError` | Variable not defined | Assign first |
| `TypeError` | `int` + `str` | Cast types |
| `ValueError` | `int("abc")` | Validate input |
| `SyntaxError` | Bad variable name | Follow rules |

**Debug tip:** `print(type(variable))` is your friend.

---

## Slide 21 — Career Spotlight

```
  User input / API / File
           │
           ▼ (all strings first)
      TYPE CASTING  ← Module 2
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
  Backend Data   AI/ML
  models  clean  features
```

Master types here → fewer bugs in every future module.

---

## Slide 22 — Lab Time

Open **`exercise.py`**:

| Section | Topic |
|---------|-------|
| A | Variables & naming |
| B | Types & `type()` |
| C | Casting & truthy/falsy |
| D | `input()` + conversion |
| E | f-strings |
| F | `None` |
| G | Career mini-projects |

---

## Slide 23 — Module 2 Summary

✅ Variables store values; `snake_case` naming  
✅ Five types: `int`, `float`, `str`, `bool`, `None`  
✅ Dynamic typing — type follows the value  
✅ `type()` and `isinstance()` check types  
✅ Cast with `int()`, `float()`, `str()`, `bool()`  
✅ `input()` returns `str` — always cast for math  
✅ f-strings for clean formatted output  

---

## Slide 24 — What's Next?

**Module 3:** Strings in Python

- Indexing & slicing
- String methods
- Formatting deep dive

**Before next class:**
- Complete exercise.py Sections A–D (minimum)
- Take **Module 2 Quiz** on Moodle

---

## Slide 25 — Quick Reference

```python
name = "Sara"              # assign
type(name)                 # <class 'str'>
isinstance(name, str)      # True

age = int("25")            # cast
price = float(input())     # cast input

print(f"Age: {age}")       # f-string

if value is None:          # check None
    ...
```

---

*End of Module 2 Slides*
