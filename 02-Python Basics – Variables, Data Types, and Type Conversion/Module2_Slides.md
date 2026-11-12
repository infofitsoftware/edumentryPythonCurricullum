# Module 2 — Variables, Data Types, and Type Conversion

**For students (beginners)**  
**Prerequisites:** Module 1 — `print()`, `input()`, arithmetic  
**Next:** Module 3 — Strings  

Read this slowly. Run the examples in `module2.py`. Then do `exercise.py`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Create variables with clear names  
2. Recognize `int`, `float`, `str`, `bool`, and `None`  
3. Check a type with `type()` / `isinstance()`  
4. Convert types with `int()`, `float()`, `str()`, `bool()`  
5. Fix the famous `input()` math bug  
6. Print values cleanly with f-strings  
7. Understand why types matter in APIs, JSON, and AI code  

---

## 2. Why this module matters (AI era)

In Module 1 you printed and calculated.  
Today you learn **what kind of data** you are holding.

That sounds small. It is not.

| Place | Why types matter |
|-------|------------------|
| FastAPI request | `"age": "25"` (text) is different from `25` (number) |
| JSON from an AI/API | Almost everything arrives as text first |
| Data cleaning | `"90"` cannot be averaged until converted |
| AI-generated code | Casting bugs are very common |

**Golden rule:**  
If AI writes code for you, check the **types**. Many bugs hide there.

---

## 3. What is a variable?

A **variable** is a name that points to a value in memory.

Think of it like a labeled box:

```python
name = "Alice"
age = 25
```

- `name` is the label  
- `"Alice"` is what is inside the box  
- `=` means “put this value into that name”

You do **not** write the type first (unlike Java/C++).  
Python looks at the value and decides the type.

---

## 4. Dynamic typing (simple meaning)

Python lets the same name hold different types later:

```python
x = 10        # now x is an int
x = "hello"   # now x is a str
```

This is flexible. It is also dangerous if you forget what type is inside.

**Beginner habit:**  
After important assignments, print `type(x)` while learning.

---

## 5. Naming rules (so your code looks professional)

### Must follow

- Start with a letter or `_`  
- Then letters, digits, `_`  
- Case matters: `Age` and `age` are different  
- Cannot use keywords like `if`, `for`, `class`

### Good style (snake_case)

```python
user_name = "Sara"
total_price = 499.5
is_active = True
```

### Bad / invalid

```python
# 2name = "x"      # starts with digit
# my-name = "x"    # hyphen not allowed
# if = 10          # keyword
```

### Constants (by convention)

Python has no true constant lock. We write ALL_CAPS to mean “please don’t change”:

```python
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_PORT = 8000
```

---

## 6. The five types you must know now

| Type | Example | Everyday meaning |
|------|---------|------------------|
| `int` | `25`, `0`, `-3` | whole numbers |
| `float` | `19.99`, `3.0` | decimals |
| `str` | `"hello"`, `'hi'` | text |
| `bool` | `True`, `False` | yes/no flags |
| `None` | `None` | “no value yet” |

```python
age = 25
price = 19.99
message = "Hello"
is_ready = True
email = None
```

### Tiny gotchas

- `3.0` is a **float**, not int  
- `True` / `False` must be capitalized  
- `None` is not `0`, not `""`, not `False` — it means missing  

### Float surprise

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

Computers store decimals in a special way. For money later, we round carefully.

---

## 7. Checking types

```python
print(type(42))                 # <class 'int'>
print(isinstance(42, int))      # True
print(isinstance(3.14, (int, float)))  # True
```

- `type()` → good while learning  
- `isinstance()` → good for checks in real programs  

---

## 8. Type conversion (casting)

Casting = changing one type into another **on purpose**.

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False
bool("hi")      # True
```

### Important details

```python
int(3.9)     # 3   (cuts decimal, does NOT round)
int("10.5")  # ERROR — use float("10.5") first
bool("")     # False (empty text)
bool("false")# True  (!!) because the string is not empty
```

That last one surprises everyone.  
`bool("false")` is `True` because any non-empty string is treated as “truthy”.

For real flags from text/config:

```python
flag_text = "true"
is_debug = flag_text.lower() == "true"
```

---

## 9. The `input()` trap (must master)

`input()` always gives a **string**.

```python
a = input("First: ")   # user types 5 → a is "5"
b = input("Second: ")  # user types 3 → b is "3"
print(a + b)           # "53"  wrong for math
```

Correct:

```python
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)           # 8
```

For money/decimals:

```python
price = float(input("Price: "))
```

**Interview classic.** Also a top AI-generated bug.

---

## 10. Where this appears in real apps (preview)

### FastAPI / backend mental model

A request body may look like JSON:

```json
{"name": "Ada", "age": "25", "active": "true"}
```

Notice: values often arrive as **text**.  
Before saving to a database you convert:

```python
age = int("25")
active = "true".lower() == "true"
```

You are not writing FastAPI today.  
You are learning the exact skill FastAPI needs.

### AI / LLM apps

Prompts, token counts, temperatures, and flags must have correct types:

```python
temperature = float("0.7")   # model setting
max_tokens = int("256")
```

If these stay as strings, math and APIs break.

---

## 11. f-strings (clean printing)

```python
name = "Ravi"
score = 87.5
print(f"{name} scored {score}%")
```

Useful patterns:

```python
print(f"Total: {19.99 * 2:.2f}")
print(f"ID: {42:05d}")   # 00042
```

---

## 12. `None` means “missing”

```python
email = None
if email is None:
    print("Email not provided")
```

Use `is None` (not `== None`).

You will see this in:

- optional API fields  
- missing data in CSV/JSON  
- “no result yet” from a function  

---

## 13. Common mistakes checklist

1. Forgetting `input()` returns `str`  
2. Doing `"10" + "5"` and expecting `15`  
3. Using `bool("false")` as a real False flag  
4. Calling `int("10.5")` instead of `float`  
5. Shipping AI code without checking `type(...)`  
6. Bad variable names (`a1`, `x`, `data2`) when a clear name exists  

---

## 14. How to study this lesson

1. Read one section  
2. Run the matching part in `module2.py`  
3. Predict output before looking  
4. Do `exercise.py` in order  
5. Take `Module2_Quiz.xml`  

If you use AI for help:

- Ask it to explain **why**  
- Re-type the fix yourself  
- Run and verify  

---

## 15. Mini self-check (before the quiz)

Can you answer these out loud?

1. What is dynamic typing?  
2. Difference between `int` and `float`?  
3. Why is `"5" + "3"` equal to `"53"`?  
4. Why is `bool("false")` True?  
5. When do you use `None`?  

If any answer is unclear, re-read that section and rerun `module2.py`.

---

## 16. What “confident” means after Module 2

You can:

- store values in well-named variables  
- identify types quickly  
- convert types safely  
- fix casting bugs in your code and in AI drafts  
- connect types to JSON/API/AI settings  

Next lesson (Module 3) goes deep into **strings** — the type you will use constantly for prompts, paths, and messages.
