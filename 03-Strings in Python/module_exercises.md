# Module 3 — Practice Exercises: Strings in Python

**Instructions for students**

- Attempt each exercise yourself before looking at solutions.
- Use only concepts from Modules 1–3 (no loops required).
- Test your programs by running them.
- Solutions are in the **Instructor Solution Guide** at the end — do not open until you have tried.

**Difficulty key:** Easy / Medium / Challenging

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — First and Last Character

**Difficulty:** Easy  
**Concepts:** indexing  

**Problem:**  
Create a string `greet` with the value `"Hello, World!"`. Print the first character and the last character on separate lines.

**Example Input:**  
(none)

**Expected Output:**
```
H
!
```

**Hint:** Use index `0` and index `-1`.

---

### Exercise 2 — Slice Out a Word

**Difficulty:** Easy  
**Concepts:** slicing  

**Problem:**  
Given `text = "PythonProgramming"`, print only the substring `"Programming"` using slicing.

**Example Input:**  
(none)

**Expected Output:**
```
Programming
```

**Hint:** Find where `"Programming"` starts (after `"Python"`).

---

### Exercise 3 — Reverse a Word

**Difficulty:** Easy  
**Concepts:** slicing with step  

**Problem:**  
Reverse the string `"Learning"` using slicing and print the result.

**Example Input:**  
(none)

**Expected Output:**
```
gninraeL
```

**Hint:** Use a step of `-1`.

---

### Exercise 4 — Concatenate with a Space

**Difficulty:** Easy  
**Concepts:** concatenation  

**Problem:**  
Concatenate `"Hello"` and `"Python"` with a single space between them and print the result.

**Example Input:**  
(none)

**Expected Output:**
```
Hello Python
```

**Hint:** `" " ` is a string containing one space.

---

### Exercise 5 — Case Conversion

**Difficulty:** Easy  
**Concepts:** `upper()`, `lower()`  

**Problem:**  
For `text = "pYtHoN"`, print the uppercase version, then the lowercase version, on two lines.

**Example Input:**  
(none)

**Expected Output:**
```
PYTHON
python
```

**Hint:** Methods return new strings; print them directly.

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Count a Letter

**Difficulty:** Easy  
**Concepts:** `count()`  

**Problem:**  
Count how many times the letter `'o'` appears in `"Hello, how are you?"` (case-sensitive as written). Print the count.

**Example Input:**  
(none)

**Expected Output:**
```
3
```

**Hint:** Use `.count("o")`.

---

### Exercise 7 — Replace a Word

**Difficulty:** Easy  
**Concepts:** `replace()`  

**Problem:**  
In the sentence `"This is a bad day."`, replace `"bad"` with `"good"` and print the new sentence.

**Example Input:**  
(none)

**Expected Output:**
```
This is a good day.
```

**Hint:** `replace` does not change the original unless you assign the result.

---

### Exercise 8 — Digits Only?

**Difficulty:** Easy  
**Concepts:** `isdigit()`  

**Problem:**  
Check whether `"123456"` contains only digits. Print the boolean result.

**Example Input:**  
(none)

**Expected Output:**
```
True
```

**Hint:** Use `.isdigit()`.

---

### Exercise 9 — Trim Spaces

**Difficulty:** Easy  
**Concepts:** `strip()`  

**Problem:**  
Remove leading and trailing spaces from `" Trim me "` and print the cleaned string between square brackets like `[Trim me]`.

**Example Input:**  
(none)

**Expected Output:**
```
[Trim me]
```

**Hint:** Concatenate `"["`, stripped text, and `"]"`.

---

### Exercise 10 — Extract Pieces

**Difficulty:** Medium  
**Concepts:** slicing  

**Problem:**  
Using slicing only:

1. Print the first three characters of `"Artificial Intelligence"`.
2. Print the last five characters of `"Technology"`.
3. Print every second character of `"Development"`.

**Example Input:**  
(none)

**Expected Output:**
```
Art
ology
Dvlpet
```

**Hint:** Last five → negative start index or `len`-based slice; every second → step `2`.

---

### Exercise 11 — HELLO from hello world

**Difficulty:** Medium  
**Concepts:** slicing, `upper()`, immutability  

**Problem:**  
From `text = "hello world"`, print `"HELLO"` without relying on loops. The original `text` variable may stay `"hello world"` unless you intentionally reassign.

**Example Input:**  
(none)

**Expected Output:**
```
HELLO
```

**Hint:** Slice the first five characters, then call `.upper()`.

---

### Exercise 12 — Format Two Ways

**Difficulty:** Medium  
**Concepts:** `.format()`, f-strings  

**Problem:**  

1. Using `.format()`, print: `My name is John and I am 30 years old.` where name and age are variables.  
2. Using an f-string, print: `The price of the book is $49.99` where `price = 49.99`.

**Example Input:**  
(none)

**Expected Output:**
```
My name is John and I am 30 years old.
The price of the book is $49.99
```

**Hint:** Placeholders `{}` for format; `{price}` inside an f-string.

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 13 — Search and Prefix/Suffix

**Difficulty:** Medium  
**Concepts:** `find()`, `startswith()`, `endswith()`  

**Problem:**  

1. Find the index of `"code"` in `"I love to code in Python."` and print it.  
2. For `"Welcome"`, print whether it starts with `"Wel"` and whether it ends with `"me"` (two boolean lines).

**Example Input:**  
(none)

**Expected Output:**
```
10
True
True
```

**Hint:** `find` returns the starting index of the substring.

---

### Exercise 14 — Split and Join

**Difficulty:** Medium  
**Concepts:** `split()`, `join()`  

**Problem:**  

1. Split `"Python is fun to learn"` into words and print the list.  
2. Join `["I", "love", "Python"]` into one string with dashes `-` between words and print it.

**Example Input:**  
(none)

**Expected Output:**
```
['Python', 'is', 'fun', 'to', 'learn']
I-love-Python
```

**Hint:** Default `split()` uses whitespace; `"-".join(...)`.

---

### Exercise 15 — Clean Login Input

**Difficulty:** Medium  
**Concepts:** `input()`, `strip()`, `lower()`, f-strings  

**Problem:**  
Ask the user for a username. Clean it with `strip()` and `lower()`, then print:

`Welcome, <cleaned_username>!`

**Example Input:**
```
  AlIcE  
```

**Expected Output:**
```
Welcome, alice!
```

**Hint:** Chain methods: `username.strip().lower()`.

---

### Exercise 16 — Email Quick Check

**Difficulty:** Medium  
**Concepts:** `input()`, `strip()`, `lower()`, `in`, f-strings  

**Problem:**  
Ask for an email. Normalize with `strip().lower()`. Print the stored email, then print `True` or `False` depending on whether it contains `@`.

**Example Input:**
```
  Student@Example.COM  
```

**Expected Output:**
```
student@example.com
True
```

**Hint:** Membership test: `"@" in email`.

---

### Exercise 17 — Length and Safe Last Character

**Difficulty:** Medium  
**Concepts:** `len()`, indexing, Module 2 types  

**Problem:**  
Ask the user for any text. Print:

1. Its length  
2. Its last character  

If the user enters an empty string after stripping spaces, print `Empty input` instead of trying to index.

**Example Input:**
```
Python
```

**Expected Output:**
```
6
n
```

**Example Input (empty):**
```
   
```

**Expected Output:**
```
Empty input
```

**Hint:** Use `strip()`, then check `len(text) == 0`. You may use a simple `if` (preview of Module 5) **or** instruct students who have not learned `if` yet to assume non-empty input — **Instructor note:** prefer teaching a minimal `if` for safety, or provide two versions. For this curriculum, a minimal `if` is allowed as a guided preview.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 18 — Filename Normalizer

**Difficulty:** Challenging  
**Concepts:** strip, lower, endswith, f-strings  

**Problem:**  
Ask the user for a filename (e.g. `"  Report.PDF  "`).  
Normalize it (`strip` + `lower`). Print:

1. The normalized name  
2. `PDF file` if it ends with `.pdf`, otherwise `Other file`

**Example Input:**
```
  Report.PDF  
```

**Expected Output:**
```
report.pdf
PDF file
```

**Hint:** Check `endswith(".pdf")` after normalizing. Minimal `if`/`else` is OK here.

---

### Exercise 19 — Simple Receipt Line

**Difficulty:** Challenging  
**Concepts:** casting, f-strings, string methods  

**Problem:**  
Ask for:

- item name (string)  
- quantity (integer)  
- unit price (float)  

Clean the item name with `strip().title()`.  
Print one receipt line:

`Item: <Name> | Qty: <q> | Total: <qty * price>`

Round the total display to 2 decimal places using an f-string format like `{total:.2f}`.

**Example Input:**
```
  wireless mouse  
2
499.5
```

**Expected Output:**
```
Item: Wireless Mouse | Qty: 2 | Total: 999.00
```

**Hint:** `int(input(...))`, `float(input(...))`, then multiply.

---

### Exercise 20 — Password Strength Preview (No Loops)

**Difficulty:** Challenging  
**Concepts:** len, isdigit/isalpha/isalnum, in, strip  

**Problem:**  
Ask for a password (as text). After `strip()`, print four lines:

1. `Length: <n>`  
2. `Has digit: True/False` — True if **any** character is a digit?  
   Without loops, approximate with: print whether the whole password is digits-only is NOT enough.  
   Instead, check these beginner-safe rules and print:

   - `Length OK: True` if length >= 8 else `False`  
   - `Has @ or #: True` if `"@" in password or "#" in password` else `False`  
   - `All letters: True/False` using `isalpha()`  
   - `All digits: True/False` using `isdigit()`

**Example Input:**
```
Secret@1
```

**Expected Output:**
```
Length OK: True
Has @ or #: True
All letters: False
All digits: False
```

**Hint:** Combine `len`, membership, and `is*` methods. Full “contains a digit somewhere” needs loops (Module 5) — this exercise uses rules available now.

---

# Instructor Solution Guide

> For instructors / self-check after attempting. Prefer clear beginner code.

```python
# Exercise 1
greet = "Hello, World!"
print(greet[0])
print(greet[-1])

# Exercise 2
text = "PythonProgramming"
print(text[6:])

# Exercise 3
print("Learning"[::-1])

# Exercise 4
print("Hello" + " " + "Python")

# Exercise 5
text = "pYtHoN"
print(text.upper())
print(text.lower())

# Exercise 6
print("Hello, how are you?".count("o"))

# Exercise 7
print("This is a bad day.".replace("bad", "good"))

# Exercise 8
print("123456".isdigit())

# Exercise 9
print("[" + " Trim me ".strip() + "]")

# Exercise 10
print("Artificial Intelligence"[:3])
print("Technology"[-5:])
print("Development"[::2])

# Exercise 11
text = "hello world"
print(text[:5].upper())

# Exercise 12
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
price = 49.99
print(f"The price of the book is ${price}")

# Exercise 13
print("I love to code in Python.".find("code"))
word = "Welcome"
print(word.startswith("Wel"))
print(word.endswith("me"))

# Exercise 14
print("Python is fun to learn".split())
print("-".join(["I", "love", "Python"]))

# Exercise 15
username = input("Enter username: ").strip().lower()
print(f"Welcome, {username}!")

# Exercise 16
email = input("Enter email: ").strip().lower()
print(email)
print("@" in email)

# Exercise 17
text = input("Enter text: ").strip()
if len(text) == 0:
    print("Empty input")
else:
    print(len(text))
    print(text[-1])

# Exercise 18
filename = input("Enter filename: ").strip().lower()
print(filename)
if filename.endswith(".pdf"):
    print("PDF file")
else:
    print("Other file")

# Exercise 19
item_name = input("Item: ").strip().title()
quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: "))
total = quantity * unit_price
print(f"Item: {item_name} | Qty: {quantity} | Total: {total:.2f}")

# Exercise 20
password = input("Password: ").strip()
print(f"Length OK: {len(password) >= 8}")
print(f"Has @ or #: {'@' in password or '#' in password}")
print(f"All letters: {password.isalpha()}")
print(f"All digits: {password.isdigit()}")
```

---

**Assumptions**

- Exercises 17–20 use a minimal `if` for realistic validation; treat as a gentle preview of Module 5 if `if` has not been taught yet in lecture.  
- Full character-by-character scanning is deferred until loops.
