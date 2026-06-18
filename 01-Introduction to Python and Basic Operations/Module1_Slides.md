# Module 1: Introduction to Python and Basic Operations

**Course:** edumentry Python Fundamentals  
**Duration:** ~2–3 hours (lecture + lab)  
**Prerequisites:** None — absolute beginners welcome

---

## Slide 1 — Welcome

### Introduction to Python and Basic Operations

- Your first step toward:
  - Backend & Web Development
  - Data Science & Analytics
  - Artificial Intelligence / Machine Learning
  - Automation & Scripting
  - DevOps & Infrastructure

> **Today:** What Python is, how to run it, and your first programs.

---

## Slide 2 — Learning Objectives

By the end of this module you will:

1. Explain what Python is and why companies use it
2. Install Python and verify the installation
3. Run code in the **REPL** and from a **`.py` script**
4. Use `print()` and `input()` confidently
5. Perform basic arithmetic operations
6. Write comments and read simple error messages

---

## Slide 3 — What is Python?

**Python** = high-level, **interpreted** programming language

- Created by **Guido van Rossum** (1991)
- Named after *Monty Python* (not the snake 🐍 — though the logo is a snake!)

| Characteristic | Meaning for you |
|----------------|-----------------|
| High-level | Less boilerplate, more productivity |
| Interpreted | Run code immediately — great for learning |
| Dynamically typed | No `int x = 5` — just `x = 5` |
| Cross-platform | Same code on Windows, Mac, Linux |

---

## Slide 4 — Why Python? (Industry View)

**Companies choose Python because:**

- Fast to learn → faster hiring & onboarding
- Readable code → easier maintenance
- One language, many domains → versatile teams

**Job market demand (2024–2026):**

| Role | Python Usage |
|------|----------------|
| Backend Developer | Django, Flask, FastAPI |
| Data Scientist | Pandas, NumPy, Jupyter |
| AI Engineer | PyTorch, TensorFlow, Hugging Face |
| Automation Engineer | Scripts, Selenium, APIs |
| DevOps Engineer | Ansible, pip, CI/CD pipelines |

---

## Slide 5 — Python 2 vs Python 3

⚠️ **Always use Python 3**

- Python 2 ended support in **January 2020**
- All modern jobs expect Python 3.x

**Check your version:**

```bash
python --version
# or
python3 --version
```

✅ Good: `Python 3.11.5`  
❌ Bad:  `Python 2.7.x`

---

## Slide 6 — Installing Python

### Windows
1. Download from [python.org](https://www.python.org/downloads/)
2. ✅ Check **"Add Python to PATH"**
3. Verify: `python --version`

### macOS
```bash
python3 --version
brew install python   # if needed
```

### Linux (Ubuntu)
```bash
sudo apt install python3 python3-pip python3-venv
```

---

## Slide 7 — Your Toolkit

| Tool | Purpose |
|------|---------|
| **Terminal / CMD** | Run Python commands |
| **VS Code / PyCharm** | Write & edit code |
| **pip** | Install libraries (`pip install django`) |
| **venv** | Isolate project dependencies |

> Professionals **always** use virtual environments — you'll master this soon.

---

## Slide 8 — Two Ways to Run Python

### A) REPL (Interactive Mode)
```bash
python
>>> print("Hi")
Hi
>>> exit()
```

### B) Script Mode (Real Projects)
```python
# hello.py
print("Hello, World!")
```
```bash
python hello.py
```

| REPL | Script |
|------|--------|
| Quick experiments | Full programs |
| Line by line | Entire file runs |

---

## Slide 9 — Hello, World!

Your first program:

```python
print("Hello, World!")
```

**Steps:**
1. Create file `hello.py`
2. Save
3. Run: `python hello.py`
4. Output: `Hello, World!`

🎉 Every programmer starts here — including AI researchers and DevOps engineers.

---

## Slide 10 — Comments

Code tells the computer **what** to do.  
Comments tell humans **why**.

```python
# Single-line comment — ignored by Python

"""
Multi-line docstring —
used for documentation.
"""

price = 99  # price in rupees
```

**Rule:** Comment complex logic, not obvious code.

---

## Slide 11 — Arithmetic Operators

```python
a, b = 10, 5

a + b    # 15  Addition
a - b    # 5   Subtraction
a * b    # 50  Multiplication
a / b    # 2.0 Division (float!)
a // b   # 2   Floor division
a % b    # 0   Modulus (remainder)
a ** b   # 100000 Exponent
```

**Career link:** `%` checks even/odd; `//` used in pagination (backend APIs).

---

## Slide 12 — print() — Showing Output

```python
print("Welcome to Python!")
print("Score:", 95, "Grade:", "A")
```

**Special parameters:**

```python
print("2024", "06", "18", sep="-")     # 2024-06-18
print("Loading", end="...")
print(" Done!")                         # Loading... Done!
```

- `sep` → separator between values
- `end` → what to print at the end (default: newline)

---

## Slide 13 — input() — Getting User Input

```python
name = input("Enter your name: ")
print("Hello,", name)
```

⚠️ **Critical rule:** `input()` **always returns a string**

```python
age = input("Age: ")   # User types 25
type(age)              # <class 'str'>  NOT int!
```

→ Type conversion (`int()`, `float()`) covered in **Module 2**.

---

## Slide 14 — Common input() Mistake

```python
num1 = input("First: ")   # "5"
num2 = input("Second: ")  # "3"
print(num1 + num2)        # "53" ❌ string concat!
```

**Fix:**

```python
num1 = int(input("First: "))
num2 = int(input("Second: "))
print(num1 + num2)        # 8 ✅
```

---

## Slide 15 — Mini Example: Calculator

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
```

Same pattern as APIs: **receive input → process → return output**

---

## Slide 16 — Indentation Matters

Python uses **indentation** (spaces), not `{}`

```python
if True:
    print("Inside if")    # 4 spaces
print("Outside if")       # no indent
```

❌ Wrong indent → `IndentationError`

**Standard:** 4 spaces per level (PEP 8 style guide)

---

## Slide 17 — Reading Error Messages

Don't panic! Errors are teachers.

| Error | Meaning |
|-------|---------|
| `SyntaxError` | Typo, missing `:` or `)` |
| `NameError` | Variable doesn't exist |
| `TypeError` | Wrong types (e.g. `int` + `str`) |
| `IndentationError` | Wrong spacing |

**Tip:** Read the **last line** of the traceback first.

---

## Slide 18 — Career Spotlight

### Same fundamentals, different paths

```
         ┌─────────────┐
         │  Module 1   │
         │ print/input │
         └──────┬──────┘
    ┌──────────┼──────────┐
    ▼          ▼          ▼
 Backend    Data Sci    AI/ML
 Flask API  Pandas      Model training
 logs       reports     inference scripts
```

Everything builds on today's basics.

---

## Slide 19 — Lab Time

Open **`exercise.py`** and complete:

| Section | Topic |
|---------|-------|
| A | Setup verification |
| B | `print()` practice |
| C | Arithmetic |
| D | `input()` programs |
| E | Comments & fixes |
| F | Mini projects |

Run: `python exercise.py`

---

## Slide 20 — Module 1 Summary

✅ Python is versatile & industry-standard  
✅ Use Python 3, verify with `--version`  
✅ REPL for experiments, `.py` files for projects  
✅ `print()` outputs, `input()` reads (always `str`)  
✅ Seven arithmetic operators: `+ - * / // % **`  
✅ Comments document your code  
✅ Read error messages — don't fear them  

---

## Slide 21 — What's Next?

**Module 2:** Variables, Data Types & Type Conversion

- Why `"5" + "3"` ≠ `8`
- `int()`, `float()`, `str()`, `bool()`
- Variables naming rules

**Before next class:**
- Finish `exercise.py` Sections A–D (minimum)
- Take **Module 1 Quiz** on Moodle

---

## Slide 22 — Quick Reference Card

```python
# Run script
# python myfile.py

print("text", variable)           # output
name = input("Prompt: ")          # input (str!)
x = int("42")                     # string → int

# Math: + - * / // % **
# Comment: # line   """ block """
```

**Resources:** [docs.python.org](https://docs.python.org/3/) | [python.org](https://www.python.org/)

---

*End of Module 1 Slides*
