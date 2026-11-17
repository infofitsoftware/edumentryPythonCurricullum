# Module 7 — Functions in Python

**For students (beginners)**  
**Prerequisites:** Modules 1–6 (I/O, types, strings, operators, control flow, collections)  
**Next:** Module 8 — File Handling  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Define and call functions with `def`  
2. Distinguish **parameters** vs **arguments**  
3. Use `return` correctly (and know how it differs from `print`)  
4. Use positional, default, and keyword arguments  
5. Use `*args` and `**kwargs` at a beginner level  
6. Understand basic **local vs global** scope  
7. Write a small **lambda** when it is appropriate  
8. Spot AI mistakes: `print` instead of `return`, missing `()`, mutable defaults  

---

## 2. Why functions matter (AI era)

Without functions you copy-paste the same logic everywhere.  
With functions you **define once** and **call many times**.

| Place | Function job |
|-------|--------------|
| FastAPI / backend | `authenticate_user()`, `create_order()` |
| Data cleaning | `clean_email()`, `normalize_name()` |
| Automation | `send_report()`, `retry_task()` |
| AI / LLM apps | `build_prompt()`, `count_tokens()`, `score_reply()` |

**Golden rule:**  
If AI writes a function for you, check **`return` vs `print`**, **argument order**, and whether the name clearly says what it does.

---

## 3. What is a function?

A **function** is a named, reusable block of code.

Analogy: a kitchen appliance.  
You press “blender” with ingredients (**arguments**) and get a result (**return**).

```
define once  →  call many times
```

---

## 4. Define and call

```python
def greet():
    print("Hello! Welcome to Python.")

greet()  # call
greet()  # call again
```

**Rules:**

- `def` keyword  
- name in `snake_case`  
- parentheses `()`  
- colon `:`  
- indented body  

Writing `greet` without `()` does **not** call the function — it only refers to the function object.

---

## 5. Parameters vs arguments

```python
def greet_person(name):   # parameter
    print(f"Hello, {name}!")

greet_person("Alice")     # argument
```

| Term | Meaning |
|------|---------|
| Parameter | Variable name in the definition |
| Argument | Actual value passed when calling |

---

## 6. `return` vs `print`

```python
def square(n):
    return n * n

result = square(4)
print(result)          # 16
print(square(5) * 2)   # 50
```

| `print` | `return` |
|---------|----------|
| Shows text on screen | Sends a value back to the caller |
| For humans | For further computation |

**Common AI/beginner bug:**

```python
def square(n):
    print(n * n)

value = square(4)
print(value)   # None
```

If you need the value later, **`return` it**.

Code after `return` in the same function does not run:

```python
def demo():
    return "first"
    print("never runs")
```

A function with no `return` returns `None`.

---

## 7. Trace a return

```python
def add(a, b):
    return a + b

value = add(3, 5)
print(value)
```

1. Call `add(3, 5)`  
2. `a=3`, `b=5`  
3. `return 8`  
4. `value` becomes `8`  
5. print `8`  

---

## 8. Multiple return values

```python
def min_max(values):
    return min(values), max(values)

lo, hi = min_max([3, 9, 1])
print(lo, hi)   # 1 9
```

Python returns a **tuple**. You unpack it (Module 6).

---

## 9. Positional arguments

```python
def describe(animal, name):
    print(f"{name} is a {animal}.")

describe("dog", "Buddy")  # order matters
```

Wrong order → wrong meaning.  
Missing a required argument → `TypeError`.

---

## 10. Default arguments

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ada")
```

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25
print(power(5, 3))   # 125
```

**Rule:** parameters with defaults come **after** parameters without defaults.

```python
# def bad(a=1, b):  # SyntaxError
```

---

## 11. Keyword arguments

```python
describe(animal="cat", name="Kitty")
describe(name="Kitty", animal="cat")  # same meaning
```

Keywords make calls clearer and allow flexible order.  
You can mix styles: **positional first**, then keywords.

```python
describe("fish", name="Nemo")
```

---

## 12. `*args` — variable positional

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # args is (1, 2, 3, 4)
```

Use when the number of inputs can vary.  
Inside the function, `args` is a **tuple**.

---

## 13. `**kwargs` — variable keyword

```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25)
```

Inside the function, `kwargs` is a **dictionary**.

Beginner-friendly combined pattern:

```python
def make_profile(name, age, *hobbies, city="Unknown", **extra):
    profile = {
        "name": name,
        "age": age,
        "hobbies": list(hobbies),
        "city": city,
    }
    profile.update(extra)
    return profile
```

---

## 14. Scope: local vs global (brief)

```python
counter = 0

def increment_local():
    counter = 10  # local — does not change the global
    print(counter)

increment_local()
print(counter)    # still 0
```

**Best practice:** pass data in as arguments; return results out.  
Avoid depending on global variables.

---

## 15. Functions + prior modules

Functions become powerful when they wrap loops, conditions, and collections.

```python
def even_only(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
```

```python
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq
```

---

## 16. Docstrings

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32
```

A docstring documents **what** the function does for future you, teammates, and AI tools reading your code.

---

## 17. Lambda functions (intro)

```python
cube = lambda x: x ** 3
print(cube(3))  # 27
```

- One expression only  
- Useful for tiny helpers  
- Prefer `def` for real logic  

Common later use:

```python
pairs = [("Ada", 90), ("Bob", 75)]
print(sorted(pairs, key=lambda item: item[1]))
```

---

## 18. Recursion preview (optional)

A function can call itself. It needs a **base case**.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Cool for learning. For many beginner tasks, a normal loop is clearer.

---

## 19. Mutable default trap (important)

```python
# BAD — default list is created once and shared
def add_item(item, bag=[]):
    bag.append(item)
    return bag
```

```python
# GOOD
def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag
```

AI tools still generate the bad version sometimes. Check for it.

---

## 20. Real-world preview (still beginner level)

### Clean an email

```python
def clean_email(raw):
    return raw.strip().lower()
```

### Build a simple AI prompt

```python
def build_prompt(task, text):
    clean = text.strip()
    return f"Task: {task}\nText: {clean}"
```

### Validate a role

```python
def is_admin(role):
    return role.strip().lower() == "admin"
```

You are not building FastAPI today.  
You are learning how real systems package logic into named functions.

---

## 21. Common mistakes checklist

1. Forgetting `()` when calling  
2. Using `print` when you needed `return`  
3. Wrong argument order  
4. Default parameter before a required parameter  
5. Calling a function before it is defined in a simple top-to-bottom script  
6. Mutable default arguments (`bag=[]`)  
7. Expecting code after `return` to run  
8. Shipping AI functions without testing the returned value  

---

## 22. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask why `return` is needed  
- Re-type the function yourself  
- Call it with 2–3 different inputs and verify  

---

## 23. Mini self-check (before the quiz)

Can you answer these out loud?

1. Parameter vs argument?  
2. `print` vs `return`?  
3. Why must default args come last?  
4. What is `*args`?  
5. Why is `bag=[]` as a default dangerous?  
6. What does a function return if it has no `return`?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 24. What “confident” means after Module 7

You can:

- break programs into named pieces  
- pass and return data cleanly  
- reuse logic across exercises and projects  
- combine functions with lists, dicts, and conditions  
- spot AI mistakes around `return`, defaults, and calling syntax  

Next lesson (Module 8) covers **file handling** — wrapping read/write logic in functions like `load_lines(path)` and `save_report(path, text)`.
