# Module 4 — Operators and Expressions

**For students (beginners)**  
**Prerequisites:** Module 1 (`print`, `input`, arithmetic), Module 2 (variables, types, casting, `bool`, `None`), Module 3 (strings, `in` for text)  
**Next:** Module 5 — Control Flow  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Explain **operator**, **operand**, and **expression**  
2. Use arithmetic operators correctly (`/`, `//`, `%`, `**`)  
3. Build **comparison** expressions that return `True` / `False`  
4. Combine conditions with **`and` / `or` / `not`**  
5. Update variables with **assignment operators** (`+=`, `*=`, …)  
6. Use **`in` / `not in`** for membership checks  
7. Explain **`is` vs `==`**, and use **`is None`** correctly  
8. Respect basic **operator precedence** (and use parentheses)  
9. Spot AI mistakes around `=` vs `==`, `/` vs `//`, and messy logic  

---

## 2. Why operators matter (AI era)

Operators are how programs **calculate** and **decide**.

| Place | Operator job |
|-------|--------------|
| FastAPI / forms | age ≥ 18? password match? |
| Billing / carts | price × qty, discounts, totals |
| Data filters | salary > 50000 and city == "Delhi" |
| AI / LLM apps | token budget, score thresholds, flag checks |
| Automation | disk > 90%? retries left > 0? |

**Golden rule:**  
If AI writes a condition for you, check **`=` vs `==`**, **`/` vs `//`**, and whether **`and` / `or`** match the real rule. Those three hide most bugs.

---

## 3. Operator, operand, expression

```python
total = 10 + 5
```

| Term | In the example |
|------|----------------|
| Operator | `+` |
| Operands | `10`, `5` |
| Expression | `10 + 5` |
| Result | `15` stored in `total` |

Think of it like a sentence:

- **Operands** = the nouns (the values)  
- **Operator** = the verb (add, compare, combine)  
- **Expression** = the full sentence that has an answer  

```python
score = 10 + 5
is_passing = score >= 15
print(is_passing)   # True
```

---

## 4. Arithmetic operators

You met these in Module 1. Now learn them with precision.

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...  (float in Python 3)
print(a // b)  # 3         (floor division)
print(a % b)   # 1         (remainder)
print(2 ** 3)  # 8         (power)
```

**Must remember:**

- `/` → always a **float** in Python 3 (`10 / 2` is `5.0`)  
- `//` → whole parts only (floor division)  
- `%` → leftover after division  

### Trace: boxes and leftovers

```python
items = 17
box_size = 5
print(items // box_size)  # 3
print(items % box_size)   # 2
```

17 = 5×3 + 2  

- full boxes → `//` → **3**  
- leftover → `%` → **2**  

Even / odd check:

```python
print(14 % 2)  # 0 → even
print(15 % 2)  # 1 → odd
```

---

## 5. Operator precedence (beginner rules)

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

**Rule of thumb (high → low):**

1. `(...)` parentheses first  
2. `**`  
3. `* / // %`  
4. `+ -`  
5. comparisons (`==`, `<`, …)  
6. `not` → `and` → `or`  

**When unsure, use parentheses.**  
Clarity beats cleverness — especially when reading AI-generated code.

```python
print(2 ** 3 ** 2)    # 512  → 2 ** (3 ** 2)
print((2 ** 3) ** 2)  # 64
```

You do not need to memorize every edge case today.  
You **do** need the habit: parenthesize anything that must be obvious.

---

## 6. Comparison operators

Comparisons always return a **`bool`**: `True` or `False`.

```python
age = 20
print(age > 18)   # True
print(age == 20)  # True
print(age != 18)  # True
print(age >= 18)  # True
print(age <= 17)  # False
```

| Symbol | Meaning |
|--------|---------|
| `==` | equal to |
| `!=` | not equal |
| `>` `<` | greater / less |
| `>=` `<=` | greater/less or equal |

### The #1 beginner (and AI) trap: `=` vs `==`

```python
score = 100      # ASSIGN a value
score == 100     # COMPARE values → True
```

Analogy:

- `=` → put this label on that box  
- `==` → ask “are these the same?”  

Strings are case-sensitive (Module 3):

```python
print("admin" == "Admin")  # False
```

Trace:

| Expression | Result | Why |
|------------|--------|-----|
| `10 > 5` | True | 10 is greater |
| `5 != 5` | False | they are equal |
| `8 >= 8` | True | equal counts for `>=` |

---

## 7. Logical operators: `and`, `or`, `not`

Use these to combine True/False results.

Gate analogy:

- **`and`** → both gates must open  
- **`or`** → at least one gate opens  
- **`not`** → reverse the answer  

```python
has_ticket = True
has_id = False
print(has_ticket and has_id)  # False
print(has_ticket or has_id)   # True
print(not has_id)             # True
```

### Tiny truth table

| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

`not True` → `False`  
`not False` → `True`

### Practical patterns

Login idea (values only — `if` comes in Module 5):

```python
user_ok = (entered_user == "admin") and (entered_pass == "1234")
```

Divisible by both 3 and 5:

```python
value = 30
print((value % 3 == 0) and (value % 5 == 0))  # True
```

Trace for `value = 30`:

1. `30 % 3 == 0` → True  
2. `30 % 5 == 0` → True  
3. True and True → **True**  

For `value = 10`:

1. `10 % 3 == 0` → False  
2. `10 % 5 == 0` → True  
3. False and True → **False**  

---

## 8. Assignment operators

These update a variable using its current value.

```python
x = 5
x += 3   # x = x + 3 → 8
x *= 2   # 16
x -= 4   # 12
```

Also useful: `/=` `//=` `%=` `**=`

```python
cart = 10
cart += 5     # 15
cart *= 2     # 30
print(cart)
```

Why they exist: shorter, clearer updates for counters, totals, carts.  
Module 5 loops will use `count += 1` constantly.

Trace:

```python
x = 5
x += 3
print(x)   # 8
x *= 2
print(x)   # 16
x -= 4
print(x)   # 12
```

---

## 9. Membership: `in` / `not in`

You already used this with strings in Module 3.

```python
email = "student@example.com"
print("@" in email)         # True
print("gmail" not in email) # True
```

Same idea later for lists (Module 6 preview):

```python
roles = ["admin", "editor"]
print("editor" in roles)    # True
```

Real use: validate characters, roles, allowed extensions.

---

## 10. Identity: `is` / `is not`

**Most important beginner use:** check for `None`.

```python
result = None
print(result is None)       # True  (preferred)
print(result is not None)   # False
```

### `is` vs `==`

- `==` → same **value**?  
- `is` → same **object in memory**?  

```python
a = [1, 2, 3]
b = a            # same object
c = [1, 2, 3]    # equal values, different object

print(a is b)    # True
print(a is c)    # False
print(a == c)    # True
```

Picture:

```
a ──► [1, 2, 3] ◄── b     same box → is True, == True
c ──► [1, 2, 3]           other box → is False, == True
```

**Beginner rule:**

- Compare values with `==`  
- Check `None` with `is None`  
- Do **not** use `is` for ordinary number/string equality  

AI sometimes writes `if x is 5:` — that is a smell. Prefer `x == 5`.

---

## 11. Expressions with prior modules

The daily pattern in real programs:

```
input → cast/clean → operator expression → True/False or number
```

```python
age = int("20")
print(age >= 18)   # True

name = "  Admin ".strip().lower()
print(name == "admin")   # True
```

This is form validation in one line of thinking.  
Module 5 will wrap these expressions in `if`.

---

## 12. Real-world preview (still beginner level)

### Auth rule (expression only)

```python
entered_user = "admin"
entered_pass = "1234"
ok = (entered_user == "admin") and (entered_pass == "1234")
print(ok)   # True
```

### Cart total + discount math

```python
price = 499.5
qty = 2
subtotal = price * qty
print(subtotal)           # 999.0
print(subtotal * 0.9)     # 899.1  (10% off)
print(subtotal > 500)     # True — threshold check
```

### AI / automation style thresholds

```python
tokens_used = 1200
budget = 1000
over_budget = tokens_used > budget
print(over_budget)        # True

cpu_percent = 92
alert = cpu_percent > 90
print(alert)              # True
```

You are not building FastAPI or an LLM app today.  
You are learning the exact comparison and logic skills those systems need.

---

## 13. Common mistakes checklist

1. Using `=` when you meant `==`  
2. Confusing `/` (float) with `//` (floor)  
3. Forgetting parentheses in mixed `and` / `or` logic  
4. Using `is` instead of `==` for normal values  
5. Case-sensitive string compares (`"Admin" == "admin"` is False)  
6. Comparing numbers from `input()` without `int()` / `float()`  
7. Shipping AI conditions without checking whether **both** sides of `and` are really required  

---

## 14. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask it to explain **why**  
- Re-type the fix yourself  
- Run and verify  

---

## 15. Mini self-check (before the quiz)

Can you answer these out loud?

1. Difference between `/` and `//`?  
2. Difference between `=` and `==`?  
3. When is `and` True?  
4. Difference between `is` and `==`?  
5. Why is `"Admin" == "admin"` False?  
6. What is `17 // 5` and `17 % 5`?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 16. What “confident” means after Module 4

You can:

- trace arithmetic, comparison, and logical expressions  
- spot `=` vs `==` bugs (including in AI drafts)  
- build validation expressions with `and` / `or` / `not`  
- update running totals with `+=`  
- choose `in` vs `==` vs `is` appropriately  
- connect operators to forms, billing, filters, and AI thresholds  

Next lesson (Module 5) covers **control flow** — placing today's expressions inside `if` / loops so the program can act on decisions.
