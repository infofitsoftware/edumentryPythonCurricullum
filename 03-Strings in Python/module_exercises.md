# Module 3 — Practice Exercises: Strings in Python

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use only Modules 1–3 (no loops required unless you already know them).

---

## A. Indexing & slicing

### A1. [E] First and last
Create `greet = "Hello, World!"`. Print the first character and the last character on separate lines.

Expected:
```
H
!
```

### A2. [E] Slice a word
Given `text = "PythonProgramming"`, print only `"Programming"` using slicing.

### A3. [E] Reverse
Reverse `"Learning"` with slicing and print it.

Expected: `gninraeL`

### A4. [M] Exclusive stop
Predict, then print:

```python
word = "Programming"
print(word[0:5])
print(word[0:4])
print(word[3:])
```

Write a one-line comment: why stop is exclusive.

### A5. [M] Every second character
From `"Development"`, print every second character.

---

## B. len, +, *, membership

### B1. [E] Length
Print `len("SKU-4421")` and the last valid index number.

### B2. [E] Concatenate
Print `"Hello"` and `"Python"` with one space between them.

### B3. [E] Repeat
Print `"Ha" * 3` and `"-" * 10`.

### B4. [M] Email check
Given `email = "student@example.com"`, print whether it contains `"@"`, whether it contains `"gmail"`, and whether `"xyz"` is not in it.

### B5. [M] Case trap
Print `"py" in "Python"` and explain the result in a comment.

---

## C. Cleaning & case

### C1. [E] Case methods
For `text = "pYtHoN"`, print `upper()`, `lower()`, and `title()`.

### C2. [E] Strip
For `raw = "   hello   "`, print `strip()`, `lstrip()`, and `rstrip()` with `|` markers around each result.

### C3. [M] Username normalize
Turn `"  Admin  "` into `"admin"` using `strip()` and `lower()`. Print it.

### C4. [M] Immutability check
```python
name = "alice"
print(name.upper())
print(name)
```
Predict both lines. Then reassign so `name` becomes `"ALICE"`.

### C5. [M] AI bug: forgotten assign
```python
msg = "bad"
msg.replace("bad", "good")
print(msg)
```
Show the bug, then the fixed version.

---

## D. Search, replace, split, join

### D1. [E] find / count
Using `"I love to code in Python"`:
- print `find("code")`
- print `find("Java")`
- print `count("o")`

### D2. [E] startswith / endswith
Check whether `"backup.py"` starts with `"back"` and ends with `".py"`.

### D3. [E] replace
Print `"This is a bad day".replace("bad", "good")`.

### D4. [M] CSV split
Split `"Alice,25,Engineer"` on commas and print the list.

### D5. [M] join
Join `["I", "love", "Python"]` with `"-"` so you get `I-love-Python`.

### D6. [C] Chain clean + slice
From `"  hello world  "`, produce `"HELLO"` using strip, slice, and upper (in any valid order).

---

## E. Checks & formatting

### E1. [E] isdigit / isalnum
Print:
- `"12345".isdigit()`
- `"Hello123".isalnum()`
- `"Hello 123".isalnum()`
- `"".isdigit()`

### E2. [E] f-string
Given `name = "John"` and `age = 30`, print `John is 30` with an f-string.

### E3. [M] Money format
Given `price = 49.99`, print `Price: $49.99` using `:.2f`.

### E4. [M] Raw string
Print `r"Line1\nLine2"` and a normal `"Line1\nLine2"`. Write a comment about the difference.

---

## F. Real-world style (still beginner)

### F1. [M] Clean email
Simulate messy input:
```python
raw_email = "  Student@Example.COM  "
```
Store a cleaned lowercase email, print it, and print whether it contains `"@"`.

### F2. [M] Filename checker
```python
uploaded = "  Invoice_March.PDF  "
```
Normalize with strip + lower. Print whether it ends with `.pdf` and whether it ends with `.py`.

### F3. [M] Profile line
Clean and title-case:
- first = `"  sara  "`
- last = `"KHAN"`
- role = `"data analyst"`

Print: `Sara Khan | Role: Data Analyst`

### F4. [M] AI prompt length
```python
prompt = "  Summarize this article in 3 bullets.  "
```
Strip it, then print the cleaned prompt and its length with an f-string.

### F5. [C] JSON-like row parse
```python
row = "  Ada , 25 , true "
```
Split on commas, strip each part, convert age to `int`, convert active with `.lower() == "true"`.  
Print name, age (with type), and active (with type).

### F6. [C] Fix the AI draft
An AI wrote:
```python
filename = "  Report.PDF  "
print(filename.endswith(".pdf"))
```
Show why this prints `False`, then fix it.

---

## G. Short written answers (as comments)

### G1. Why are strings immutable?
Answer:

### G2. Why is slice stop exclusive?
Answer:

### G3. Why can AI string code “look right” but fail?
Answer:

### G4. When do you use a raw string?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
