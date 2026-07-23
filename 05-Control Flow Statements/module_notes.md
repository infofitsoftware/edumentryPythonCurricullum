# Module 5 — Control Flow Statements

**Course:** Utrains Python Fundamentals  
**Audience:** Beginners  
**Prerequisites:** Modules 1–4 (I/O, types, strings, operators)  
**Next:** Module 6 — Collections (lists, tuples, dictionaries, sets)

---

# Slide 1 — Title

## Control Flow Statements

**Until now:** code ran straight down, line by line.

**Today:** programs that **decide** and **repeat**.

```
Decisions  →  if / elif / else
Repetition →  for / while
Loop tools →  break / continue / pass
```

---

# Slide 2 — Learning Objectives

Students will be able to:

1. Write `if`, `if-else`, and `if-elif-else` correctly  
2. Explain why **colon** and **indentation** matter  
3. Use `range(start, stop, step)` accurately  
4. Write `for` loops over ranges, strings, and simple lists  
5. Write `while` loops with a correct update  
6. Use **counters** and **accumulators**  
7. Apply `break`, `continue`, and `pass`  
8. Trace nested decisions and simple nested loops  
9. Combine control flow with Modules 1–4 skills  

---

# Slide 3 — WHY Control Flow?

### Analogies

| Real life | Control flow |
|-----------|----------------|
| Traffic signal | if / else path |
| ATM PIN check | if credentials ok |
| Exam grade bands | if-elif-else |
| Attendance roll call | for each name |
| Retry password | while not correct |
| Stop searching | break |
| Skip holiday | continue |

**Career links:** auth, validation, batch jobs, log scanning, data filtering, automation retries.

---

# Slide 4 — WHAT Is Control Flow?

**Control flow** = the order in which statements run.

Three big ideas:

1. **Sequence** — one after another (already know)  
2. **Selection** — choose a path (`if`)  
3. **Iteration** — repeat a path (`for` / `while`)

---

# Slide 5 — if Statement — SYNTAX

```python
if condition:
    # indented block runs only when condition is True
```

```python
temperature = 36
if temperature > 30:
    print("It is hot today.")
```

**Must have:**

- condition that is True/False (Module 4 expressions)  
- colon `:`  
- indented block (4 spaces)

---

# Slide 6 — Trace an if

```python
age = 20
if age >= 18:
    print("Eligible")
print("Done")
```

**Trace:**

1. `age >= 18` → True  
2. print Eligible  
3. print Done  

If `age = 15`:

1. condition False → skip block  
2. print Done only  

**Ask:** What prints when age is 18?

---

# Slide 7 — if-else

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Analogy:** two doors — exactly one opens.

| number | `% 2 == 0` | Output |
|--------|------------|--------|
| 8 | True | Even |
| 7 | False | Odd |

---

# Slide 8 — if-elif-else

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

- Check conditions top to bottom  
- First True branch runs  
- Rest are skipped  
- `else` is optional but useful as “everything else”

---

# Slide 9 — Grade Ladder Trace

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

**Trace for 82:**

- `>= 90`? False  
- `>= 75`? True → print **Good** → stop  

**Order matters:** if you put `>= 50` before `>= 75`, a score of 82 would wrongly become Average.

---

# Slide 10 — Indentation & Common if Mistakes

```python
# Missing colon → SyntaxError
# if x > 0
#     print("yes")

# Wrong indent → IndentationError
# if x > 0:
# print("yes")

# Assignment vs comparison
# if x = 5:   # wrong
# if x == 5:  # correct
```

**Instructor tip:** show live IndentationError once — students remember.

---

# Slide 11 — Nesting and Compound Conditions

```python
if username == "admin" and password == "1234":
    print("Access granted")
```

```python
if account_active:
    if balance >= 100:
        print("Withdrawal allowed")
```

Prefer clear compound conditions when readable; nest when inner logic is truly dependent.

---

# Slide 12 — WHY Loops?

Without loops:

```python
print(1)
print(2)
print(3)
# ... painful for 1000 items
```

With loops: write the rule once, repeat many times.

**Use cases:** process records, sum values, retry until success, scan characters in text.

---

# Slide 13 — range() Deep Dive

```python
range(5)          # 0,1,2,3,4
range(1, 6)       # 1,2,3,4,5
range(0, 10, 2)   # 0,2,4,6,8
range(5, 0, -1)   # 5,4,3,2,1
```

**Critical:** `stop` is **excluded** (like string slices).

**Mini challenge:** What numbers does `range(1, 10)` produce?

---

# Slide 14 — for with range

```python
for i in range(1, 6):
    print(i)
```

**Trace:**

| Iteration | i | prints |
|-----------|---|--------|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |

Then stop (`i` would be 6 but 6 not in range).

---

# Slide 15 — for over Strings and Collections

```python
for char in "Python":
    print(char)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

**Connection:** Module 3 strings are sequences → loopable.  
Lists/tuples preview Module 6.

---

# Slide 16 — Accumulators (ESSENTIAL PATTERN)

```python
total = 0
for number in range(1, 4):
    total = total + number
print(total)  # 6
```

**Trace:**

| Iteration | number | total |
|-----------|--------|-------|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

**Pattern:** initialize → update in loop → use after loop.  
Used for sums, counts, products, building results.

---

# Slide 17 — while Loops

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Parts:**

1. Initialize (`i = 1`)  
2. Condition (`i <= 5`)  
3. Body  
4. Update (`i += 1`) ← forgetting this → **infinite loop**

**Analogy:** keep refilling a bottle while it is not full; remember to pour each time.

---

# Slide 18 — for vs while

| Prefer `for` when | Prefer `while` when |
|-------------------|---------------------|
| You know how many times / you have a sequence | You repeat until a condition becomes false |
| `range`, string, list | retries, “until user quits”, reading until sentinel |

Both can often solve the same problem; choose the clearer one.

---

# Slide 19 — break

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output: `1 2 3 4`  
Loop **ends completely** at 5.

**Real use:** stop when password is correct; stop search when item found.

---

# Slide 20 — continue

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

**Ask:** Difference between break and continue in one sentence?

---

# Slide 21 — pass

```python
for i in range(5):
    pass  # placeholder
```

**Why:** Python requires a block after `:` — `pass` is an intentional no-op while designing.

---

# Slide 22 — Nested Loops (Intro)

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

# Slide 23 — Full Trace: Sum + Filter

```python
total = 0
for n in range(1, 6):
    if n % 2 == 0:
        total += n
print(total)
```

**Trace:**

- n=1 odd → skip  
- n=2 → total=2  
- n=3 skip  
- n=4 → total=6  
- n=5 skip  
Output: **6**

---

# Slide 24 — Common Beginner Mistakes

1. Missing `:` after `if` / `for` / `while`  
2. Bad indentation  
3. `=` instead of `==`  
4. `range(1, 10)` expecting 10 included  
5. Infinite `while` (no update)  
6. Confusing `break` and `continue`  
7. Accumulator not initialized before loop  
8. Using `if` chain where `elif` order is wrong  

---

# Slide 25 — Professional Connection

| Domain | Control flow |
|--------|----------------|
| Backend | auth branches, validation |
| Data | filter rows, aggregate sums |
| Automation | retry while failing; break on success |
| DevOps | alert if metric > threshold |
| AI pipelines | skip bad samples (`continue`) |

---

# Slide 26 — Concept Recap

- `if` / `elif` / `else` choose paths  
- `for` iterates sequences / ranges  
- `while` repeats on condition  
- Accumulators build results  
- `break` exits; `continue` skips; `pass` placeholders  

---

# Slide 27 — Syntax Cheat Sheet

```python
if cond:
    ...
elif cond2:
    ...
else:
    ...

for i in range(1, n + 1):
    ...

while cond:
    ...
    # update

if x == stop:
    break
if skip:
    continue
pass
```

---

# Slide 28 — Mistakes Checklist

- [ ] Colon present?  
- [ ] Indentation consistent?  
- [ ] Comparison uses `==`?  
- [ ] `range` stop exclusive?  
- [ ] `while` variable updated?  
- [ ] Accumulator initialized?  

---

# Slide 29 — “Can You Explain This?”

1. When do you use `elif` instead of many separate `if`s?  
2. Why does `range(1, 5)` not include 5?  
3. What makes a `while` loop infinite?  
4. `break` vs `continue`?  
5. Why initialize `total = 0` before summing?  

---

# Slide 30 — Mini Live Challenges

1. Trace output of break-at-5 loop  
2. Sum even numbers from 1 to 10  
3. Countdown 10 → 1 with `while`  
4. Count vowels in `"Education"`  

---

# Slide 31 — What You Should Now Be Able To Do

- Trace branching and looping code  
- Write decision programs (grades, login, sign checks)  
- Write loops for sums, counts, tables, text scans  
- Debug infinite loops and off-by-one range errors  

---

# Slide 32 — Next Module

**Module 6 — Collections**

You will store many values in lists/dicts and loop over them heavily using today's `for` skills.

---

# Slide 33 — Lab Directions

1. Study `module.py`  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 5 teaching slides*
