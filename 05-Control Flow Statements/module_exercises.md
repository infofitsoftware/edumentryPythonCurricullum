# Module 5 — Practice Exercises: Control Flow Statements

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use Modules 1–5. Prefer tracing on paper for loops.

---

## A. Decisions: if / elif / else

### A1. [E] Sign of a number
Ask for an integer. Print `Positive`, `Negative`, or `Zero`.

Example input: `-3` → `Negative`

### A2. [E] Even or odd
Ask for an integer. Print `Even` or `Odd`.

### A3. [E] Age category
Ask for age. Print:
- `Child` if age < 12  
- `Teenager` if 12 ≤ age ≤ 18  
- `Adult` if age > 18  

### A4. [M] Grade ladder
Ask for marks (0–100). Print `Excellent` (≥90), `Good` (≥75), `Average` (≥50), or `Fail`.

### A5. [M] Mini login
Ask for username and password. Correct: `admin` / `1234`.  
Print `Access granted` or `Access denied`.

### A6. [M] Nested withdrawal
```python
account_active = True
balance = 80
```
Using nested `if`, print `Withdrawal allowed`, `Insufficient balance`, or `Account inactive`  
(try changing the values).

### A7. [C] AI bug: wrong elif order
An AI wrote:
```python
marks = 82
if marks >= 50:
    print("Average")
elif marks >= 75:
    print("Good")
elif marks >= 90:
    print("Excellent")
else:
    print("Fail")
```
Predict the output. Fix the order so 82 prints `Good`.

---

## B. range and for

### B1. [E] Print 1 to 10
Using `for` and `range`, print 1 through 10, one per line.

### B2. [E] Even numbers
Print even numbers from 2 to 20 using `range` with a step.

### B3. [E] Characters
Print each character of `"Python"` on its own line.

### B4. [M] Exclusive stop
Predict, then print:

```python
print(list(range(1, 5)))
print(list(range(1, 10)))
```

Write a comment: why stop is exclusive.

### B5. [M] Multiplication table
Ask for `n`. Print the table of `n` from 1 to 10 using f-strings  
(e.g. `5 x 3 = 15`).

### B6. [M] Star triangle
Print:
```
*
**
***
****
*****
```
using a `for` loop (and string `*`).

---

## C. Accumulators and counters

### C1. [E] Sum 1 to 10
Use a loop to compute and print the sum of 1 through 10.

Expected: `55`

### C2. [E] Count evens
Count how many even numbers are in 1…10. Print the count.

Expected: `5`

### C3. [M] Even sum
Sum only the even numbers from 1 to 5. Print the total.

Expected: `6`

### C4. [M] Factorial
Compute `5!` with a loop (`1 * 2 * 3 * 4 * 5`). Print it.

Expected: `120`

### C5. [M] Vowel counter
Count vowels in `"Education"` (case-insensitive). Print the count.

### C6. [C] Factor list
Ask for a positive integer `n`. Print all factors of `n`  
(numbers from 1 to `n` that divide `n` evenly).

---

## D. while, break, continue, pass

### D1. [E] while countdown
Using `while`, print 10 down to 1.

### D2. [E] while 1 to 5
Using `while`, print 1 through 5.

### D3. [M] break practice
```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```
Predict the output. Then change it to break at 7.

### D4. [M] continue practice
Print numbers 1…10 but skip 5 using `continue`.

### D5. [M] Skip vowels
Loop over `"education"`. Skip vowels with `continue`. Print consonants only.

### D6. [M] Password attempts
```python
secret = "admin123"
attempts = ["wrong", "nope", "admin123", "later"]
```
Loop over attempts. On success print `Access granted.` and `break`.  
Otherwise print `Incorrect attempt: ...`

### D7. [C] AI bug: infinite while
An AI wrote:
```python
i = 1
while i <= 5:
    print(i)
```
Explain why this is dangerous. Fix it.

---

## E. Combine Modules 1–5 (real-world style)

### E1. [M] Clean + decide
Ask for a role string. Clean with `strip().lower()`.  
If it equals `"admin"` print `Admin panel`, else print `User panel`.

### E2. [M] Email gate
Ask for an email. After `strip().lower()`, if it contains both `@` and `.`  
print `Valid format`, else `Invalid format`.

### E3. [M] Skip empty prompts (AI era)
```python
prompts = ["  hello  ", "", "  ", "summarize"]
```
Loop, strip each item, `continue` if empty, otherwise print `Ready: ...`

### E4. [M] CPU alert
Ask for `cpu_percent` (int). If `> 90` print `Alert`, elif `>= 70` print `Warm`, else print `Normal`.

### E5. [C] Number analyzer
Ask for an integer. Print whether it is Positive/Negative/Zero, Even/Odd,  
and list its factors (if non-zero).

### E6. [C] Cart with category discount
Ask for three item prices (floats). Sum with `+=` in a loop over a small list,  
or three inputs.  
If total ≥ 200 apply 10% off (`*= 0.9`).  
Print final total with 2 decimals.

---

## F. Short written answers (as comments)

### F1. When should you use `elif` instead of separate `if`s?
Answer:

### F2. Why does `range(1, 5)` not include 5?
Answer:

### F3. What makes a `while` loop infinite?
Answer:

### F4. Difference between `break` and `continue`?
Answer:

### F5. Why initialize `total = 0` before a summing loop?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
