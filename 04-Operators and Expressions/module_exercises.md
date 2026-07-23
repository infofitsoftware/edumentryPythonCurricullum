# Module 4 — Practice Exercises: Operators and Expressions

**Instructions**

- Attempt each exercise before opening the Instructor Solution Guide.
- Use Modules 1–4 concepts. Minimal `if` / `else` is allowed where a decision must be shown (preview of Module 5).
- Test your code by running it.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Basic Arithmetic Printout

**Difficulty:** Easy  
**Concepts:** arithmetic operators  

**Problem:**  
Print results of: `23 + 19`, `78 - 45`, `7 * 6`, and `144 / 12` (four lines, numbers only or clearly labeled).

**Example Input:** (none)

**Expected Output:**
```
42
33
42
12.0
```

**Hint:** Use `/` for the last one — Python 3 returns a float.

---

### Exercise 2 — Floor, Modulus, Power

**Difficulty:** Easy  
**Concepts:** `//`, `%`, `**`  

**Problem:**  
Print the results of `15 // 4`, `20 % 3`, and `2 ** 4` on three lines.

**Example Input:** (none)

**Expected Output:**
```
3
2
16
```

**Hint:** `//` drops the fraction; `%` is remainder.

---

### Exercise 3 — Compare Six Ways

**Difficulty:** Easy  
**Concepts:** comparison operators  

**Problem:**  
Print the boolean results of:

`10 > 5`, `7 < 3`, `15 == 15`, `20 != 10`, `8 >= 8`, `9 <= 4`

**Example Input:** (none)

**Expected Output:**
```
True
False
True
True
True
False
```

**Hint:** Each expression prints `True` or `False`.

---

### Exercise 4 — Logic Trio

**Difficulty:** Easy  
**Concepts:** `and`, `or`, `not`  

**Problem:**  
Print:

`(10 > 5) and (8 < 12)`  
`(7 == 3) or (15 > 10)`  
`not (20 == 20)`

**Example Input:** (none)

**Expected Output:**
```
True
True
False
```

**Hint:** Evaluate each side before combining.

---

### Exercise 5 — Assignment Trace Warm-up

**Difficulty:** Easy  
**Concepts:** `+=`, `*=`, `-=`  

**Problem:**  
Start with `x = 5`. Apply `x += 3`, print `x`. Then `x *= 2`, print `x`. Then `x -= 4`, print `x`.

**Example Input:** (none)

**Expected Output:**
```
8
16
12
```

**Hint:** Each update uses the current value of `x`.

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Rectangle Area

**Difficulty:** Easy  
**Concepts:** `input`, casting, `*`  

**Problem:**  
Ask for length and width (floats). Print the area (`length * width`).

**Example Input:**
```
5
3.5
```

**Expected Output:**
```
17.5
```

**Hint:** `float(input(...))`.

---

### Exercise 7 — Simple Interest

**Difficulty:** Easy  
**Concepts:** arithmetic expression  

**Problem:**  
Given `P = 5000`, `R = 5`, `T = 3`, compute `SI = (P * R * T) / 100` and print it.

**Example Input:** (none)

**Expected Output:**
```
750.0
```

**Hint:** Parentheses help readability even when precedence works.

---

### Exercise 8 — a and b Trio

**Difficulty:** Medium  
**Concepts:** `/`, `//`, `%`  

**Problem:**  
Given `a = 12` and `b = 5`, print `a / b`, `a // b`, and `a % b` on three lines.

**Example Input:** (none)

**Expected Output:**
```
2.4
2
2
```

**Hint:** Compare float division vs floor vs remainder.

---

### Exercise 9 — Membership Checks

**Difficulty:** Easy  
**Concepts:** `in`, `not in`, strings  

**Problem:**  
For `word = "apple"`, print whether `"a"` is in `word`, and whether `"z"` is not in `word`.

**Example Input:** (none)

**Expected Output:**
```
True
True
```

**Hint:** Two print statements.

---

### Exercise 10 — None Identity

**Difficulty:** Easy  
**Concepts:** `is`, `is not`, `None`  

**Problem:**  
Set `data = None`. Print `data is None` and `data is not None`.

**Example Input:** (none)

**Expected Output:**
```
True
False
```

**Hint:** Prefer `is` for `None` checks.

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — Voting Eligibility

**Difficulty:** Medium  
**Concepts:** `input`, `int`, `>=`, minimal `if`  

**Problem:**  
Ask for age. If age ≥ 18 print `Eligible to vote`, else print `Not eligible`.

**Example Input:**
```
20
```

**Expected Output:**
```
Eligible to vote
```

**Hint:** `age >= 18`.

---

### Exercise 12 — Positive / Negative / Zero

**Difficulty:** Medium  
**Concepts:** comparisons, `if-elif-else` preview  

**Problem:**  
Ask for an integer. Print `Positive`, `Negative`, or `Zero`.

**Example Input:**
```
-4
```

**Expected Output:**
```
Negative
```

**Hint:** Check `> 0`, then `< 0`, else zero.

---

### Exercise 13 — Mini Login

**Difficulty:** Medium  
**Concepts:** `and`, string compare, `strip` optional  

**Problem:**  
Ask for username and password. Correct values: `admin` / `1234`.  
If both match, print `Access granted`, else `Access denied`.

**Example Input:**
```
admin
1234
```

**Expected Output:**
```
Access granted
```

**Hint:** `(user == "admin") and (password == "1234")`.

---

### Exercise 14 — Divisible by 3 and 5

**Difficulty:** Medium  
**Concepts:** `%`, `and`  

**Problem:**  
Ask for an integer. Print `Yes` if divisible by both 3 and 5, otherwise `No`.

**Example Input:**
```
30
```

**Expected Output:**
```
Yes
```

**Hint:** `(n % 3 == 0) and (n % 5 == 0)`.

---

### Exercise 15 — Normalized Admin Check

**Difficulty:** Medium  
**Concepts:** string methods + `==`  

**Problem:**  
Ask for a role string. Clean with `strip().lower()`. Print `True` if it equals `"admin"`, else `False`.

**Example Input:**
```
  AdMiN  
```

**Expected Output:**
```
True
```

**Hint:** Normalize before comparing.

---

### Exercise 16 — Email Gate

**Difficulty:** Medium  
**Concepts:** `in`, `and`, strings  

**Problem:**  
Ask for an email. After `strip().lower()`, print `Valid format` if it contains `@` **and** `.`, otherwise `Invalid format`.

**Example Input:**
```
student@example.com
```

**Expected Output:**
```
Valid format
```

**Hint:** `("@" in email) and ("." in email)`.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Cart Updater

**Difficulty:** Challenging  
**Concepts:** assignment operators, arithmetic  

**Problem:**  
Start `total = 0`.  
Ask for three item prices (floats). Use `+=` to add each.  
Then apply a 10% discount using `total *= 0.9`.  
Print the final total rounded to 2 decimal places.

**Example Input:**
```
100
50
50
```

**Expected Output:**
```
180.00
```

**Hint:** Sum first (200), then `* 0.9` → 180.

---

### Exercise 18 — Grade Band Expression

**Difficulty:** Challenging  
**Concepts:** comparisons, logical operators  

**Problem:**  
Ask for marks (0–100 integer). Print:

- `Excellent` if marks ≥ 90  
- `Good` if 75 ≤ marks < 90  
- `Average` if 50 ≤ marks < 75  
- `Fail` otherwise  

**Example Input:**
```
82
```

**Expected Output:**
```
Good
```

**Hint:** Use `if` / `elif` / `else` with `>=` and `<`.

---

### Exercise 19 — Even Packed Boxes

**Difficulty:** Challenging  
**Concepts:** `//`, `%`, `==`  

**Problem:**  
Ask for `items` and `box_size` (positive integers). Print:

1. Number of full boxes (`//`)  
2. Leftover (`%`)  
3. `Even leftover` if leftover is even, else `Odd leftover`

**Example Input:**
```
17
5
```

**Expected Output:**
```
3
2
Even leftover
```

**Hint:** Even leftover means `leftover % 2 == 0`.

---

### Exercise 20 — Access Policy

**Difficulty:** Challenging  
**Concepts:** `and` / `or` / `not`, membership, cleaning  

**Problem:**  
Ask for `username` and `role`.  
Clean both with `strip().lower()`.  
Allowed roles: treat as check with `role == "admin" or role == "editor"` (or `role in ["admin", "editor"]`).  
Grant access only if username is not empty **and** role is allowed.  
Print `Access granted` or `Access denied`.

**Example Input:**
```
alice
Editor
```

**Expected Output:**
```
Access granted
```

**Example Input:**
```

viewer
```

**Expected Output:**
```
Access denied
```

**Hint:** Empty username → `username == ""` after strip.

---

# Instructor Solution Guide

```python
# Exercise 1
print(23 + 19)
print(78 - 45)
print(7 * 6)
print(144 / 12)

# Exercise 2
print(15 // 4)
print(20 % 3)
print(2 ** 4)

# Exercise 3
print(10 > 5)
print(7 < 3)
print(15 == 15)
print(20 != 10)
print(8 >= 8)
print(9 <= 4)

# Exercise 4
print((10 > 5) and (8 < 12))
print((7 == 3) or (15 > 10))
print(not (20 == 20))

# Exercise 5
x = 5
x += 3
print(x)
x *= 2
print(x)
x -= 4
print(x)

# Exercise 6
length = float(input("Length: "))
width = float(input("Width: "))
print(length * width)

# Exercise 7
P, R, T = 5000, 5, 3
SI = (P * R * T) / 100
print(SI)

# Exercise 8
a, b = 12, 5
print(a / b)
print(a // b)
print(a % b)

# Exercise 9
word = "apple"
print("a" in word)
print("z" not in word)

# Exercise 10
data = None
print(data is None)
print(data is not None)

# Exercise 11
age = int(input("Age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Exercise 12
number = int(input("Number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 13
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")

# Exercise 14
n = int(input("Number: "))
if (n % 3 == 0) and (n % 5 == 0):
    print("Yes")
else:
    print("No")

# Exercise 15
role = input("Role: ").strip().lower()
print(role == "admin")

# Exercise 16
email = input("Email: ").strip().lower()
if ("@" in email) and ("." in email):
    print("Valid format")
else:
    print("Invalid format")

# Exercise 17
total = 0.0
total += float(input("Price 1: "))
total += float(input("Price 2: "))
total += float(input("Price 3: "))
total *= 0.9
print(f"{total:.2f}")

# Exercise 18
marks = int(input("Marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Fail")

# Exercise 19
items = int(input("Items: "))
box_size = int(input("Box size: "))
full_boxes = items // box_size
leftover = items % box_size
print(full_boxes)
print(leftover)
if leftover % 2 == 0:
    print("Even leftover")
else:
    print("Odd leftover")

# Exercise 20
username = input("Username: ").strip().lower()
role = input("Role: ").strip().lower()
allowed = role == "admin" or role == "editor"
if username != "" and allowed:
    print("Access granted")
else:
    print("Access denied")
```
