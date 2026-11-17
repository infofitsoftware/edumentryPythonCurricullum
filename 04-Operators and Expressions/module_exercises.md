# Module 4 — Practice Exercises: Operators and Expressions

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use only Modules 1–4. You do **not** need loops.  
If an exercise asks you to print different messages, a tiny `if` / `else` preview is OK (full control flow is Module 5). Prefer printing the `True`/`False` result when that is enough.

---

## A. Arithmetic & precedence

### A1. [E] Four calculations
Print the results of `23 + 19`, `78 - 45`, `7 * 6`, and `144 / 12` on four lines.

Expected:
```
42
33
42
12.0
```

### A2. [E] Floor, mod, power
Print `15 // 4`, `20 % 3`, and `2 ** 4` on three lines.

Expected:
```
3
2
16
```

### A3. [E] Division twins
Given `a = 12` and `b = 5`, print `a / b`, `a // b`, and `a % b` on three lines.

Expected:
```
2.4
2
2
```

### A4. [M] Boxes and leftovers
Given `items = 17` and `box_size = 5`, print full boxes and leftover.

Expected:
```
3
2
```

### A5. [M] Precedence
Predict, then print:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

Write a one-line comment: why the answers differ.

---

## B. Comparisons

### B1. [E] Six comparisons
Print:

`10 > 5`, `7 < 3`, `15 == 15`, `20 != 10`, `8 >= 8`, `9 <= 4`

Expected:
```
True
False
True
True
True
False
```

### B2. [E] Assign vs compare
```python
score = 100
print(score == 100)
```
Predict the output. Then write a comment explaining the difference between `=` and `==`.

### B3. [M] Case trap
Print `"admin" == "Admin"` and explain the result in a comment.

### B4. [M] Cast then compare
```python
age_text = "20"
```
Convert to `int` and print whether the age is `>= 18`.

### B5. [M] AI bug: comparing text as a number
```python
age_text = "9"
print(age_text > "18")
print(int(age_text) > 18)
```
Predict both lines. Write a comment: which one is the safe check for voting age?

---

## C. Logical operators

### C1. [E] Logic trio
Print:

`(10 > 5) and (8 < 12)`  
`(7 == 3) or (15 > 10)`  
`not (20 == 20)`

Expected:
```
True
True
False
```

### C2. [E] Ticket gate
```python
has_ticket = True
has_id = False
```
Print `has_ticket and has_id`, then `has_ticket or has_id`, then `not has_id`.

### C3. [M] Login expression
Given:
```python
entered_user = "admin"
entered_pass = "1234"
```
Print whether both match `"admin"` and `"1234"` using `and`.

### C4. [M] Divisible by 3 and 5
For `value = 30` and then `value = 10`, print whether each is divisible by both 3 and 5.

### C5. [C] Parentheses matter
Predict, then print:

```python
print(True or False and False)
print((True or False) and False)
```

Write a comment about operator order (`and` before `or`).

---

## D. Assignment & membership & identity

### D1. [E] Assignment chain
Start with `x = 5`. Apply `x += 3`, print `x`. Then `x *= 2`, print `x`. Then `x -= 4`, print `x`.

Expected:
```
8
16
12
```

### D2. [E] Cart updater warm-up
Start `total = 0`. Use `+=` to add `100`, then `50`, then `50`. Print `total`.

Expected: `200`

### D3. [E] Membership
For `word = "apple"`, print whether `"a"` is in `word`, and whether `"z"` is not in `word`.

### D4. [E] None identity
Set `data = None`. Print `data is None` and `data is not None`.

### D5. [M] is vs ==
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
```
Print `a is b`, `a is c`, and `a == c`. Write a comment explaining the difference.

### D6. [M] Role check
```python
roles = ["admin", "editor", "viewer"]
```
Print whether `"editor"` is in `roles` and whether `"guest"` is not in `roles`.

---

## E. Cleaning + operators (Modules 3 + 4)

### E1. [M] Normalized admin check
```python
typed = "  AdMiN  "
```
Clean with `strip().lower()` and print whether it equals `"admin"`.

### E2. [M] Email gate expression
```python
raw = "  Student@Example.COM  "
```
Clean, then print whether it contains both `"@"` and `"."`.

### E3. [M] Profile flag
```python
first = "  sara  "
role = "Admin"
```
Clean both. Print whether the cleaned first name equals `"sara"` **and** the cleaned role equals `"admin"`.

### E4. [M] Discount threshold
```python
price = 499.5
qty = 2
```
Compute `subtotal = price * qty`. Print the subtotal, the 10% off amount (`* 0.9`), and whether `subtotal > 500`.

### E5. [C] AI draft fix
An AI wrote:
```python
username = "  Admin "
print(username == "admin")
```
Show why this prints `False`, then fix it so it prints `True`.

---

## F. Real-world style (still beginner)

### F1. [M] Simple interest
Given `P = 5000`, `R = 5`, `T = 3`, compute `SI = (P * R * T) / 100` and print it.

Expected: `750.0`

### F2. [M] Token budget (AI era)
```python
tokens_used = 1200
budget = 1000
```
Print whether usage is over budget, and how many tokens over (`tokens_used - budget`).

### F3. [M] CPU alert
```python
cpu_percent = 92
```
Print `cpu_percent > 90` and `cpu_percent >= 100`.

### F4. [M] Voting eligibility (tiny if preview)
Ask for age with `input`, cast to `int`.  
If age ≥ 18 print `Eligible to vote`, else print `Not eligible`.

### F5. [M] Mini login (tiny if preview)
Ask for username and password. Correct values: `admin` / `1234`.  
Print `Access granted` or `Access denied`.

### F6. [C] Cart with discount
Start `total = 0.0`.  
Ask for three item prices (floats). Use `+=` to add each.  
Then apply 10% off with `total *= 0.9`.  
Print the final total with 2 decimal places (`:.2f`).

Example input:
```
100
50
50
```
Expected: `180.00`

### F7. [C] Access policy
Ask for `username` and `role`.  
Clean both with `strip().lower()`.  
Grant access only if username is not empty **and** role is `"admin"` or `"editor"`.  
Print `Access granted` or `Access denied`.

Example:
```
alice
Editor
```
→ `Access granted`

```

viewer
```
→ `Access denied`

---

## G. Short written answers (as comments)

### G1. Why does `/` return a float in Python 3?
Answer:

### G2. When should you use `is` instead of `==`?
Answer:

### G3. Why can AI-written conditions “look right” but fail?
Answer:

### G4. What does `17 // 5` and `17 % 5` mean in plain English?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
