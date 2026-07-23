# Module 8 — Practice Exercises: File Handling

**Instructions**

- Attempt before opening the Instructor Solution Guide.
- Create files in your working folder (or a subfolder you choose).
- Prefer `with open(...)` and `encoding="utf-8"` for text.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Write a Greeting File

**Difficulty:** Easy  
**Concepts:** write mode  

**Problem:** Write `"Hello, File Handling!\n"` to `hello.txt`, then read and print the content.

**Expected Output:**
```
Hello, File Handling!
```

**Hint:** `"w"` then `"r"`.

---

### Exercise 2 — Write Three Lines

**Difficulty:** Easy  
**Concepts:** write / writelines  

**Problem:** Write these three lines to `lines.txt`:

```
Python
Files
Rocks
```

Then print the file contents.

**Hint:** Include `\n` on each line.

---

### Exercise 3 — Append a Line

**Difficulty:** Easy  
**Concepts:** append  

**Problem:** Start from Exercise 2’s `lines.txt` (or recreate it). Append `Again`. Print all contents.

**Expected Output:**
```
Python
Files
Rocks
Again
```

**Hint:** mode `"a"`.

---

### Exercise 4 — Count Lines

**Difficulty:** Easy  
**Concepts:** for line in file  

**Problem:** Create a file with 4 lines. Write a program that prints how many lines it has.

**Expected Output:**
```
4
```

**Hint:** `count = 0` then increment per line.

---

### Exercise 5 — Exists Check

**Difficulty:** Easy  
**Concepts:** `os.path.exists`  

**Problem:** Check whether `hello.txt` exists. Print `Found` or `Missing`.

**Hint:** `import os`

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — readline Practice

**Difficulty:** Easy  
**Concepts:** readline  

**Problem:** Given a file with at least two lines, print only the first line using `readline()`, stripped.

**Hint:** `line.strip()`

---

### Exercise 7 — readlines Practice

**Difficulty:** Easy  
**Concepts:** readlines  

**Problem:** Read all lines into a list and print the list length and the second line stripped.

**Hint:** `lines[1].strip()`

---

### Exercise 8 — Save/Load Functions

**Difficulty:** Medium  
**Concepts:** functions + files  

**Problem:** Write `save_text(path, text)` and `load_text(path)`. Save `"Module 8\n"` to `note.txt`, load it, print stripped.

**Expected Output:**
```
Module 8
```

**Hint:** Use `with` inside both functions.

---

### Exercise 9 — Overwrite Danger Demo

**Difficulty:** Medium  
**Concepts:** `"w"` vs `"a"`  

**Problem:**

1. Write `"first\n"` to `demo.txt` with `"w"`.  
2. Open again with `"w"` and write `"second\n"`.  
3. Print file contents.

**Expected Output:**
```
second
```

**Hint:** Second `"w"` overwrites.

---

### Exercise 10 — Safe Create with x

**Difficulty:** Medium  
**Concepts:** `"x"`, try/except optional  

**Problem:** Create `unique.txt` with mode `"x"` and write `"created\n"`.  
If you run the create step twice, the second time should fail with `FileExistsError` (catch and print `Already exists`).

**Hint:** `try/except FileExistsError` is a gentle preview of error handling.

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — Log Writer

**Difficulty:** Medium  
**Concepts:** append, functions  

**Problem:** Write `log(path, message)` that appends `message + "\n"`.  
Log two messages to `app.log`, then print the file.

**Expected Output (example):**
```
started
finished
```

**Hint:** mode `"a"`.

---

### Exercise 12 — Copy Text File

**Difficulty:** Medium  
**Concepts:** read + write  

**Problem:** Copy contents from `source.txt` to `copy.txt` using Python (not OS copy command). Print `copy.txt`.

**Hint:** `content = load...` then save to new path.

---

### Exercise 13 — Strip and Collect

**Difficulty:** Medium  
**Concepts:** lists + files  

**Problem:** Read a multi-line file into a list of stripped lines (no `\n`). Print the list.

**Example file:**
```
apple
banana
```

**Expected Output:**
```
['apple', 'banana']
```

**Hint:** `[line.strip() for line in file]` or append in a loop.

---

### Exercise 14 — Word Count in File

**Difficulty:** Medium  
**Concepts:** read, split  

**Problem:** Write text with multiple words to a file. Print total word count.

**Example content:** `Python is fun to learn`

**Expected Output:**
```
5
```

**Hint:** `len(content.split())`

---

### Exercise 15 — Filter Lines

**Difficulty:** Medium  
**Concepts:** loop, condition, write  

**Problem:** Input file has mixed lines. Write only lines containing `"error"` (case-insensitive) to `errors.txt`.

**Hint:** `if "error" in line.lower():`

---

### Exercise 16 — CSV-like Scores

**Difficulty:** Challenging  
**Concepts:** split, casting, lists/dicts  

**Problem:** Create `scores.csv`:

```
name,score
Ada,90
Bob,75
Cam,95
```

Read it (skip header), store dicts, print the average score as float.

**Expected Output:**
```
86.666...
```
(or `86.67` if you round)

**Hint:** `int(score)` then average.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Binary Round-Trip

**Difficulty:** Medium  
**Concepts:** `"wb"`/`"rb"`  

**Problem:** Write bytes `b"ABC"` to `data.bin`, read them back, print the bytes and their length.

**Expected Output:**
```
b'ABC'
3
```

**Hint:** `"wb"` / `"rb"`.

---

### Exercise 18 — Delete if Exists

**Difficulty:** Easy  
**Concepts:** exists, remove  

**Problem:** If `temp.txt` exists, delete it and print `Deleted`; else print `Nothing to delete`.  
Create `temp.txt` first so you can test both branches.

**Hint:** `os.remove`

---

### Exercise 19 — Line Number Reporter

**Difficulty:** Challenging  
**Concepts:** enumerate, files  

**Problem:** Print each line of a file prefixed with line numbers:

```
1: first
2: second
```

**Hint:** `for i, line in enumerate(file, start=1):`

---

### Exercise 20 — Merge Two Files

**Difficulty:** Challenging  
**Concepts:** read/write multiple files  

**Problem:** Given `a.txt` and `b.txt`, create `merged.txt` containing all lines from both (a then b). Print `merged.txt`.

**Hint:** Read both strings/lists, write combined output.

---

# Instructor Solution Guide

```python
import os

# Exercise 1
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, File Handling!\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Exercise 2
with open("lines.txt", "w", encoding="utf-8") as f:
    f.write("Python\nFiles\nRocks\n")
with open("lines.txt", "r", encoding="utf-8") as f:
    print(f.read().rstrip())

# Exercise 3
with open("lines.txt", "a", encoding="utf-8") as f:
    f.write("Again\n")
with open("lines.txt", "r", encoding="utf-8") as f:
    print(f.read().rstrip())

# Exercise 4
with open("four.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\nd\n")
count = 0
with open("four.txt", "r", encoding="utf-8") as f:
    for _ in f:
        count += 1
print(count)

# Exercise 5
if os.path.exists("hello.txt"):
    print("Found")
else:
    print("Missing")

# Exercise 6
with open("lines.txt", "r", encoding="utf-8") as f:
    print(f.readline().strip())

# Exercise 7
with open("lines.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines))
print(lines[1].strip())

# Exercise 8
def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

save_text("note.txt", "Module 8\n")
print(load_text("note.txt").strip())

# Exercise 9
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("first\n")
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("second\n")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Exercise 10
try:
    with open("unique.txt", "x", encoding="utf-8") as f:
        f.write("created\n")
except FileExistsError:
    print("Already exists")

# Exercise 11
def log(path, message):
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")

if os.path.exists("app.log"):
    os.remove("app.log")
log("app.log", "started")
log("app.log", "finished")
with open("app.log", "r", encoding="utf-8") as f:
    print(f.read().rstrip())

# Exercise 12
with open("source.txt", "w", encoding="utf-8") as f:
    f.write("copy me\n")
with open("source.txt", "r", encoding="utf-8") as f:
    content = f.read()
with open("copy.txt", "w", encoding="utf-8") as f:
    f.write(content)
with open("copy.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Exercise 13
with open("fruit.txt", "w", encoding="utf-8") as f:
    f.write("apple\nbanana\n")
with open("fruit.txt", "r", encoding="utf-8") as f:
    items = [line.strip() for line in f]
print(items)

# Exercise 14
with open("words.txt", "w", encoding="utf-8") as f:
    f.write("Python is fun to learn")
with open("words.txt", "r", encoding="utf-8") as f:
    print(len(f.read().split()))

# Exercise 15
with open("mixed.txt", "w", encoding="utf-8") as f:
    f.write("ok\nERROR disk\ninfo\nerror again\n")
with open("mixed.txt", "r", encoding="utf-8") as src, open("errors.txt", "w", encoding="utf-8") as dst:
    for line in src:
        if "error" in line.lower():
            dst.write(line)

# Exercise 16
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write("name,score\nAda,90\nBob,75\nCam,95\n")
scores = []
with open("scores.csv", "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        _, score = line.strip().split(",")
        scores.append(int(score))
print(sum(scores) / len(scores))

# Exercise 17
with open("data.bin", "wb") as f:
    f.write(b"ABC")
with open("data.bin", "rb") as f:
    data = f.read()
print(data)
print(len(data))

# Exercise 18
with open("temp.txt", "w", encoding="utf-8") as f:
    f.write("tmp\n")
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("Deleted")
else:
    print("Nothing to delete")

# Exercise 19
with open("numbered.txt", "w", encoding="utf-8") as f:
    f.write("first\nsecond\n")
with open("numbered.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")

# Exercise 20
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("A1\nA2\n")
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("B1\n")
with open("a.txt", "r", encoding="utf-8") as fa, open("b.txt", "r", encoding="utf-8") as fb:
    merged = fa.read() + fb.read()
with open("merged.txt", "w", encoding="utf-8") as f:
    f.write(merged)
with open("merged.txt", "r", encoding="utf-8") as f:
    print(f.read().rstrip())
```
