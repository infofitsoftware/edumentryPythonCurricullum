# Module 5 — Control Flow Statements

**For students (beginners)**  
**Prerequisites:** Module 1 (`print`, `input`), Module 2 (types, casting), Module 3 (strings), Module 4 (operators, `and`/`or`/`not`)  
**Next:** Module 6 — Collections  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Write `if`, `if-else`, and `if-elif-else` correctly  
2. Explain why **colon** and **indentation** matter  
3. Use `range(start, stop, step)` accurately (stop is exclusive)  
4. Write `for` loops over ranges, strings, and simple lists  
5. Write `while` loops with a correct update  
6. Use **counters** and **accumulators**  
7. Apply `break`, `continue`, and `pass`  
8. Trace nested decisions and simple nested loops  
9. Spot AI mistakes: missing `:`, bad indent, infinite `while`, wrong `elif` order  

---

## 2. Why control flow matters (AI era)

Until now, code ran straight down. Real programs must **decide** and **repeat**.

| Place | Control flow job |
|-------|------------------|
| FastAPI / forms | accept or reject based on rules |
| Auth | grant / deny access |
| Data pipelines | filter rows, sum values, skip bad samples |
| AI / LLM apps | retry until success; skip empty prompts |
| Automation | loop over files; alert if metric > threshold |

**Golden rule:**  
If AI writes an `if` or loop for you, check **colon + indentation**, **`=` vs `==`**, **`range` stop**, and whether a **`while` updates**. Those hide most bugs.

---

## 3. What is control flow?

**Control flow** = the order in which statements run.

Three big ideas:

1. **Sequence** — one after another (you already know)  
2. **Selection** — choose a path (`if`)  
3. **Iteration** — repeat a path (`for` / `while`)

```
Decisions  →  if / elif / else
Repetition →  for / while
Loop tools →  break / continue / pass
```

Everyday analogies:

| Real life | Control flow |
|-----------|--------------|
| Traffic signal | if / else path |
| ATM PIN check | if credentials ok |
| Exam grade bands | if-elif-else |
| Attendance roll call | for each name |
| Retry password | while not correct |
| Stop searching | break |
| Skip a holiday | continue |

---

## 4. The `if` statement

```python
if condition:
    # this block runs only when condition is True
```

```python
temperature = 36
if temperature > 30:
    print("It is hot today.")
```

**Must have:**

- a condition that is True/False (Module 4 expressions)  
- a colon `:`  
- an indented block (usually 4 spaces)

### Trace

```python
age = 20
if age >= 18:
    print("Eligible")
print("Done")
```

1. `age >= 18` → True  
2. print `Eligible`  
3. print `Done`  

If `age = 15`:

1. condition False → skip block  
2. print `Done` only  

---

## 5. `if-else`

Two doors — exactly one opens.

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

| number | `% 2 == 0` | Output |
|--------|------------|--------|
| 8 | True | Even |
| 7 | False | Odd |

---

## 6. `if-elif-else`

Use when you have **more than two** paths.

```python
score = 0
if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Zero")
```

**Rules:**

- Check conditions **top to bottom**  
- First True branch runs  
- Rest are skipped  
- `else` is optional, but useful as “everything else”

### Grade ladder (order matters!)

```python
marks = 82
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Fail")
```

Trace for 82:

- `>= 90`? False  
- `>= 75`? True → print **Good** → stop  

If you put `>= 50` before `>= 75`, a score of 82 would wrongly become Average.  
AI sometimes generates conditions in the wrong order — always check the ladder.

---

## 7. Indentation and common `if` mistakes

Python uses indentation instead of `{ }`.

```python
# Missing colon → SyntaxError
# if x > 0
#     print("yes")

# Wrong indent → IndentationError
# if x > 0:
# print("yes")

# Assignment vs comparison
# if x = 5:    # wrong
# if x == 5:   # correct
```

Multiple lines in one block must share the same indent:

```python
age = 20
if age >= 18:
    print("Eligible")
    print("You may vote")
```

---

## 8. Compound conditions and nesting

Module 4 operators power real decisions:

```python
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
```

Nested `if` (decision inside decision):

```python
if account_active:
    if balance >= 100:
        print("Withdrawal allowed")
    else:
        print("Insufficient balance")
else:
    print("Account inactive")
```

Prefer a clear compound condition when readable.  
Nest when the inner logic truly depends on the outer check.

---

## 9. Why loops?

Without loops:

```python
print(1)
print(2)
print(3)
# painful for 1000 items
```

With loops: write the rule once, repeat many times.

Use cases: process records, sum values, retry until success, scan characters in text.

---

## 10. `range()` — foundation for `for`

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

**Critical:** `stop` is **excluded** — same idea as string slices in Module 3.

| Call | Numbers |
|------|---------|
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(1, 10)` | 1 … 9 (not 10) |

---

## 11. `for` loops

### With `range`

```python
for i in range(1, 6):
    print(i)
```

| Iteration | i | prints |
|-----------|---|--------|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |

### Over a string (Module 3)

```python
for char in "Python":
    print(char)
```

### Over a simple list (preview of Module 6)

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

---

## 12. Accumulators and counters (essential pattern)

```python
total = 0
for number in range(1, 4):
    total = total + number
print(total)  # 6
```

| Iteration | number | total |
|-----------|--------|-------|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

**Pattern:** initialize → update in loop → use after loop.

Used for sums, counts, products, building results.

```python
even_count = 0
for n in range(1, 11):
    if n % 2 == 0:
        even_count += 1
print(even_count)  # 5
```

Forgetting `total = 0` before the loop is a classic bug (AI does this too).

---

## 13. `while` loops

Repeats **while** the condition is True.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Four parts:**

1. Initialize (`i = 1`)  
2. Condition (`i <= 5`)  
3. Body  
4. Update (`i += 1`) ← forgetting this → **infinite loop**

Analogy: keep filling a bottle while it is not full — remember to pour each time.

Countdown:

```python
i = 5
while i >= 1:
    print(i)
    i -= 1
```

---

## 14. `for` vs `while`

| Prefer `for` when | Prefer `while` when |
|-------------------|---------------------|
| You know how many times / you have a sequence | You repeat until a condition becomes false |
| `range`, string, list | retries, “until user quits”, reading until stop |

Both can often solve the same problem. Choose the clearer one.

---

## 15. `break` — exit the loop now

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output: `1 2 3 4`  
The loop **ends completely** when `i == 5`.

Real use: stop when password is correct; stop search when item found.

---

## 16. `continue` — skip this iteration

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

Skips printing 5, continues with 6…10.

```python
for char in "education":
    if char in "aeiou":
        continue
    print(char)
```

**One sentence difference:**

- `break` → leave the loop entirely  
- `continue` → skip the rest of this round, keep looping  

---

## 17. `pass` — intentional do-nothing

```python
for i in range(5):
    pass  # placeholder
```

Python requires a block after `:`.  
`pass` keeps the syntax valid while you design later logic.

---

## 18. Nested loops (intro)

```python
for i in range(1, 4):
    print("*" * i)
```

```
*
**
***
```

```python
for row in range(1, 3):
    for col in range(1, 3):
        print(row, col)
```

Inner loop finishes fully for each outer iteration.

---

## 19. Full trace: sum + filter

```python
total = 0
for n in range(1, 6):
    if n % 2 == 0:
        total += n
print(total)
```

- n=1 odd → skip  
- n=2 → total=2  
- n=3 skip  
- n=4 → total=6  
- n=5 skip  

Output: **6**

Vowel counter (string + loop + if):

```python
text = "Education"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print(vowel_count)
```

---

## 20. Real-world preview (still beginner level)

### Auth branch

```python
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
```

### Skip bad AI prompts

```python
prompts = ["  summarize this  ", "", "  ", "write a title"]
for raw in prompts:
    clean = raw.strip()
    if clean == "":
        continue
    print(f"Ready prompt: {clean}")
```

### Retry until success (while + break)

```python
attempts = ["wrong", "nope", "admin123"]
secret = "admin123"
for attempt in attempts:
    if attempt == secret:
        print("Access granted.")
        break
    print("Incorrect:", attempt)
```

You are not building FastAPI today.  
You are learning the decision and loop skills those systems need.

---

## 21. Common mistakes checklist

1. Missing `:` after `if` / `for` / `while`  
2. Bad indentation  
3. `=` instead of `==`  
4. `range(1, 10)` expecting 10 included  
5. Infinite `while` (forgot update)  
6. Confusing `break` and `continue`  
7. Accumulator not initialized before the loop  
8. Wrong `elif` order in grade ladders  
9. Shipping AI loop code without tracing one full pass  

---

## 22. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask it to explain **why**  
- Trace one iteration yourself  
- Run and verify  

---

## 23. Mini self-check (before the quiz)

Can you answer these out loud?

1. When do you use `elif` instead of many separate `if`s?  
2. Why does `range(1, 5)` not include 5?  
3. What makes a `while` loop infinite?  
4. `break` vs `continue`?  
5. Why initialize `total = 0` before summing?  
6. What prints for marks `82` in the grade ladder?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 24. What “confident” means after Module 5

You can:

- trace branching and looping code  
- write decision programs (grades, login, sign checks)  
- write loops for sums, counts, tables, text scans  
- debug infinite loops and off-by-one `range` errors  
- spot AI mistakes around indent, `elif` order, and `while` updates  

Next lesson (Module 6) covers **collections** — lists, tuples, dictionaries, sets — which you will loop over heavily using today's `for` skills.
