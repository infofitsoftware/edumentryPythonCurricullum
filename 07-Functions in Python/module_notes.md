# Module 7 — Functions in Python

**Course:** Utrains Python Fundamentals  
**Prerequisites:** Modules 1–6  
**Next:** Module 8 — File Handling

---

# Slide 1 — Title

## Functions in Python

**Big idea:** Give a name to a block of logic and reuse it.

```
define once  →  call many times
```

---

# Slide 2 — Learning Objectives

1. Define and call functions with `def`  
2. Distinguish **parameters** vs **arguments**  
3. Use `return` correctly (vs `print`)  
4. Use positional, default, and keyword arguments  
5. Use `*args` and `**kwargs`  
6. Understand basic **local vs global** scope  
7. Write small lambdas appropriately  
8. Combine functions with collections and control flow  

---

# Slide 3 — WHY Functions Exist

Without functions:

```python
# copy-paste the same 10 lines everywhere 😱
```

With functions:

- Reuse logic  
- Easier to read (`calculate_total()`)  
- Easier to fix bugs in one place  
- Matches how real software is built  

**Career:** every backend endpoint handler, data transform, and test helper is a function.

---

# Slide 4 — WHAT Is a Function?

A **function** is a named, reusable block of code.

**Analogy:** a kitchen appliance — “blender” — you press it with ingredients (arguments) and get a result (return).

---

# Slide 5 — SYNTAX: Define and Call

```python
def greet():
    print("Hello! Welcome to Python.")

greet()  # call
```

Rules:

- `def` keyword  
- name (`snake_case`)  
- parentheses `()`  
- colon `:`  
- indented body  

**Ask:** What happens if you write `greet` without `()`?

---

# Slide 6 — Parameters vs Arguments

```python
def greet_person(name):   # parameter
    print(f"Hello, {name}!")

greet_person("Alice")     # argument
```

| Term | Meaning |
|------|---------|
| Parameter | Variable in the definition |
| Argument | Actual value passed in |

---

# Slide 7 — return vs print

```python
def square(n):
    return n * n

result = square(4)
print(result)
```

| `print` | `return` |
|---------|----------|
| Shows text to screen | Sends value back to caller |
| For humans | For further computation |

**Common mistake:** using only `print` inside a function, then wondering why `x = f()` is `None`.

---

# Slide 8 — Trace a Return

```python
def add(a, b):
    return a + b

value = add(3, 5)
print(value)
```

**Trace:**

1. Call `add(3, 5)`  
2. `a=3`, `b=5`  
3. `return 8`  
4. `value` becomes 8  
5. print 8  

---

# Slide 9 — Multiple Return Values

```python
def min_max(values):
    return min(values), max(values)

lo, hi = min_max([3, 9, 1])
```

Returns a **tuple** (Module 6 unpacking).

---

# Slide 10 — Positional Arguments

```python
def describe(animal, name):
    print(f"{name} is a {animal}.")

describe("dog", "Buddy")  # order matters
```

Wrong order → wrong meaning.

Missing required argument → `TypeError`.

---

# Slide 11 — Default Arguments

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ada")
```

**Rule:** parameters with defaults come **after** those without.

```python
def power(base, exponent=2):
    return base ** exponent
```

---

# Slide 12 — Keyword Arguments

```python
describe(animal="cat", name="Kitty")
describe(name="Kitty", animal="cat")  # same
```

Clarity + flexible order.

Can mix: positional first, then keywords.

---

# Slide 13 — *args

```python
def add_numbers(*args):
    return sum(args)

add_numbers(1, 2, 3, 4)  # args → (1, 2, 3, 4)
```

Use when the number of inputs varies.

---

# Slide 14 — **kwargs

```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25)
```

`kwargs` is a **dictionary**.

---

# Slide 15 — Scope: Local vs Global (Brief)

```python
counter = 0

def increment_local():
    counter = 10  # local variable
```

Changing a name inside a function usually creates a **local** variable.

**Best practice:** pass data in as arguments; return results out. Avoid relying on globals.

---

# Slide 16 — Functions + Prior Modules

```python
def even_only(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
```

Functions become powerful when they wrap loops, conditions, and collections.

---

# Slide 17 — Docstrings

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32
```

Docstrings document **what** the function does for future you / teammates.

---

# Slide 18 — Lambda Functions

```python
cube = lambda x: x ** 3
print(cube(3))  # 27
```

- One expression  
- Anonymous / short-lived  
- Prefer `def` for real logic  

Useful later with `sorted(..., key=lambda ...)`.

---

# Slide 19 — Recursion Preview

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Needs a **base case**. Cool for learning; loops often clearer for beginners.

---

# Slide 20 — Mutable Default Trap (Important Warning)

```python
# BAD
def add_item(item, bag=[]):
    bag.append(item)
    return bag
```

Default list is created **once** and shared across calls.

```python
# GOOD
def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag
```

---

# Slide 21 — Common Beginner Mistakes

1. Forgetting `()` when calling  
2. `print` instead of `return`  
3. Wrong argument order  
4. Default before non-default params  
5. Calling a name before it is defined in a script  
6. Mutable default arguments  
7. Expecting code after `return` to run  

---

# Slide 22 — Professional Connection

| Role | Function examples |
|------|-------------------|
| Backend | `authenticate_user()`, `create_order()` |
| Data | `clean_column()`, `compute_mean()` |
| Automation | `send_report()`, `retry_task()` |
| AI | `preprocess()`, `predict()` |

---

# Slide 23 — Concept Recap

- `def` / call / parameters / arguments  
- `return` sends values back  
- positional / default / keyword / `*args` / `**kwargs`  
- scope basics  
- lambda for tiny expressions  

---

# Slide 24 — Syntax Cheat Sheet

```python
def f(a, b=0, *args, **kwargs):
    """Docstring."""
    return a + b

f(1)
f(1, 2)
f(a=1, b=2)
lambda x: x * 2
```

---

# Slide 25 — Mistakes Checklist

- [ ] Did I `return` when I need a value?  
- [ ] Did I call with `()`?  
- [ ] Defaults at the end?  
- [ ] Avoided mutable defaults?  
- [ ] Clear function name?  

---

# Slide 26 — “Can You Explain This?”

1. Parameter vs argument?  
2. `print` vs `return`?  
3. Why default args must be last?  
4. What is `*args`?  
5. Why is `bag=[]` as a default dangerous?  

---

# Slide 27 — Mini Challenges

1. Write `is_even(n)` returning bool  
2. Write `average(numbers)`  
3. Write `word_count(sentence)`  
4. Convert a Celsius function to also support keyword `celsius=`  

---

# Slide 28 — What You Can Do Now

- Break programs into named pieces  
- Pass and return data cleanly  
- Reuse logic across exercises and projects  
- Read other people’s functions more confidently  

---

# Slide 29 — Next Module

**Module 8 — File Handling**  
You will wrap file read/write logic in functions like `load_lines(path)` and `save_report(path, text)`.

---

# Slide 30 — Lab Directions

1. Study `module.py`  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 7 teaching slides*
