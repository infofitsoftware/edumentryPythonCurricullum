# Module 4 — Operators and Expressions

**Course:** Utrains Python Fundamentals  
**Audience:** Beginners  
**Prerequisites:** Module 1 (print/input/arithmetic), Module 2 (types/bool/None), Module 3 (strings, `in` for text)  
**Next:** Module 5 — Control Flow (where operators power `if` / loops)

---

# Slide 1 — Title

## Operators and Expressions

**Big idea:**  
Programs make **decisions** and **calculations** by combining values with operators.

```
values + operators  →  expression  →  result
```

**Ask the class:**  
Where have you already used operators? (`+`, `/`, `==` inside f-strings? Module 1 math?)

---

# Slide 2 — Learning Objectives

By the end of this module, students will be able to:

1. Use all **arithmetic** operators correctly (`/`, `//`, `%`, `**`)
2. Build **comparison** expressions that return `True` / `False`
3. Combine conditions with **`and` / `or` / `not`**
4. Update variables with **assignment operators** (`+=`, `*=`, …)
5. Use **`in` / `not in`** for membership checks
6. Explain **`is` vs `==`**, and use **`is None`** correctly
7. Respect basic **operator precedence** (and use parentheses)
8. Combine operators with input, casting, and strings from prior modules

---

# Slide 3 — WHY Operators Exist

### Everyday → Python

| Real life | Operator idea |
|-----------|----------------|
| Cart total = price × qty | `*` |
| “Age at least 18?” | `>=` |
| “Correct user AND password?” | `and` |
| Add 5 points to score | `+=` |
| “Is `@` in the email?” | `in` |

Without operators, programs cannot calculate or decide.

**Career links (light):**

- Backend: auth rules, validation  
- Data: filters (`salary > 50000`)  
- Automation: thresholds, retries  
- DevOps: “disk > 90%?” style checks  

---

# Slide 4 — WHAT: Operator, Operand, Expression

```python
total = 10 + 5
```

| Term | In the example |
|------|----------------|
| Operator | `+` |
| Operands | `10`, `5` |
| Expression | `10 + 5` |
| Result | `15` stored in `total` |

**Analogy:**  
Operator = verb (add, compare, combine).  
Operands = nouns.  
Expression = full sentence that has an answer.

---

# Slide 5 — Arithmetic Operators (Revisit + Deepen)

```python
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... float
print(a // b)  # 3 floor
print(a % b)   # 1 remainder
print(2 ** 3)  # 8
```

**Emphasize:**

- `/` → always float in Python 3  
- `//` → whole parts (floor division)  
- `%` → remainder (even/odd, leftovers)

---

# Slide 6 — Trace: Boxes and Leftovers

```python
items = 17
box_size = 5
print(items // box_size)  # 3
print(items % box_size)   # 2
```

**Trace:**

17 = 5×3 + 2  

- full boxes → `//` → 3  
- leftover → `%` → 2  

**Ask:** Is 14 even? How do you know with `%`?

---

# Slide 7 — Precedence (Beginner Rules)

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

**Rule of thumb:**

1. `(...)` first  
2. `**`  
3. `* / // %`  
4. `+ -`  
5. comparisons  
6. `not` → `and` → `or`

**Teaching tip:**  
When unsure, **use parentheses**. Clarity beats cleverness.

---

# Slide 8 — Comparison Operators

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

**Returns:** always a `bool`.

---

# Slide 9 — The #1 Mistake: `=` vs `==`

```python
score = 100      # ASSIGN a value
score == 100     # COMPARE values → True
```

**Analogy:**  

- `=` → put this label on that box  
- `==` → ask “are these the same?”

**Strings (Module 3):**

```python
print("admin" == "Admin")  # False — case matters
```

---

# Slide 10 — Trace Comparisons

```python
x = 10
y = 5
print(x > y)
print(y != 5)
print(8 >= 8)
```

| Expression | Result | Why |
|------------|--------|-----|
| `x > y` | True | 10 > 5 |
| `y != 5` | False | 5 is equal to 5 |
| `8 >= 8` | True | equal counts for `>=` |

**Mini challenge:** Predict `9 <= 4`.

---

# Slide 11 — Logical Operators — WHY

Traffic light / gate check analogy:

- **and** → both gates must open  
- **or** → at least one gate opens  
- **not** → reverse the answer  

```python
has_ticket = True
has_id = False
print(has_ticket and has_id)  # False
print(has_ticket or has_id)   # True
print(not has_id)             # True
```

---

# Slide 12 — Truth Tables (Keep Short)

| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

`not True` → `False`  
`not False` → `True`

**Practical login idea:**

```python
ok = (user == "admin") and (pwd == "1234")
```

---

# Slide 13 — Combined Conditions

```python
value = 30
print((value % 3 == 0) and (value % 5 == 0))  # True
```

**Trace:**

1. `30 % 3 == 0` → True  
2. `30 % 5 == 0` → True  
3. True and True → True  

**Ask:** For `value = 10`, what happens?

---

# Slide 14 — Assignment Operators

```python
x = 5
x += 3   # x = x + 3 → 8
x *= 2   # 16
x -= 4   # 12
```

Also: `/=` `//=` `%=` `**=`

**Why they exist:**  
Shorter, clearer updates — counters, totals, carts.

**Connection:** Module 5 loops will use `count += 1` constantly.

---

# Slide 15 — Trace Assignment Chain

```python
x = 5
x += 3
print(x)   # 8
x *= 2
print(x)   # 16
x -= 4
print(x)   # 12
```

**Student activity:**  
Start `x = 10`, apply `x //= 3`, then `x %= 2`. Final `x`?

---

# Slide 16 — Membership: `in` / `not in`

```python
email = "a@b.com"
print("@" in email)
print("x" not in email)
```

Works with strings now; same idea later for lists (Module 6).

```python
roles = ["admin", "editor"]
print("editor" in roles)
```

**Real use:** validate characters, roles, allowed file extensions (with Module 3 methods).

---

# Slide 17 — Identity: `is` / `is not`

```python
result = None
print(result is None)      # preferred check
print(result is not None)
```

**`is` vs `==`:**

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True  — same object
print(a is c)   # False — different objects
print(a == c)   # True  — same values
```

**Rule for beginners:**  

- Compare values with `==`  
- Check `None` with `is None`  
- Do not use `is` for ordinary number/string equality

---

# Slide 18 — Diagram: is vs ==

```
list_a ──► [1, 2, 3] ◄── list_b     (same box)  → is True, == True

list_c ──► [1, 2, 3]                 (other box) → is False, == True
```

**Instructor talking point:**  
Equal twins (`==`) vs the exact same person (`is`).

---

# Slide 19 — Expressions with Prior Modules

```python
age = int("20")
print(age >= 18)

name = "  Admin ".strip().lower()
print(name == "admin")
```

**Pattern:**

```
input → cast/clean → operator expression → True/False or number
```

This pattern powers almost every form validation.

---

# Slide 20 — Common Beginner Mistakes

1. `=` instead of `==`  
2. Confusing `/` and `//`  
3. Forgetting parentheses in mixed logic  
4. Using `is` instead of `==` for values  
5. Case-sensitive string comparisons (`"Admin" == "admin"`)  
6. Expecting `and` / `or` to work like English “and/or” without bools  

---

# Slide 21 — Professional Connection

| Domain | Operator use |
|--------|----------------|
| Auth | `user == ... and password == ...` |
| Billing | `+=`, `*`, discounts |
| Data filters | `age >= 18 and city == "Delhi"` |
| Monitoring | `cpu_percent > 90` |
| Text cleaning | `"@" in email` |

Module 5 will wrap these expressions in `if` / loops.

---

# Slide 22 — Concept Recap

- Arithmetic: `+ - * / // % **`  
- Comparison → `bool`  
- Logical: `and or not`  
- Assignment updates: `+=` …  
- Membership: `in`  
- Identity: `is` (especially `None`)  
- Precedence + parentheses  

---

# Slide 23 — Syntax Cheat Sheet

```python
a + b, a - b, a * b, a / b, a // b, a % b, a ** b
a == b, a != b, a > b, a < b, a >= b, a <= b
cond1 and cond2
cond1 or cond2
not cond
x += 1
"@" in email
value is None
```

---

# Slide 24 — Mistakes Checklist

- [ ] Did I use `==` for comparison?  
- [ ] Did I cast `input()` before comparing numbers?  
- [ ] Did I normalize strings before `==`?  
- [ ] Did I use parentheses for clear logic?  
- [ ] Did I use `is None` rather than `== None`?  

---

# Slide 25 — “Can You Explain This?”

1. Difference between `/` and `//`?  
2. Difference between `=` and `==`?  
3. When is `and` True?  
4. Difference between `is` and `==`?  
5. Why is `"Admin" == "admin"` False?  

---

# Slide 26 — Mini Live Challenges

1. Predict: `(7 == 3) or (15 > 10)`  
2. Predict final `x`: `x=5; x+=3; x*=2; x-=4`  
3. Write expression: number divisible by 3 **and** 5  
4. Clean `"  ADMIN "` and check equality to `"admin"`  

---

# Slide 27 — What You Should Now Be Able To Do

- Trace arithmetic / comparison / logical expressions  
- Spot `=` vs `==` bugs  
- Build validation expressions  
- Update running totals with `+=`  
- Choose `in` vs `==` vs `is` appropriately  

---

# Slide 28 — Next Module

**Module 5 — Control Flow**

You will place today's expressions inside:

```python
if age >= 18:
    ...
```

Operators decide; control flow acts.

---

# Slide 29 — Lab Directions

1. Run and study `module.py`  
2. Complete `module_exercises.md` Levels 1–4  
3. Take quiz from `module_quiz.json`  

---

*End of Module 4 teaching slides*
