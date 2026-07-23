# Module 3 — Strings in Python

**Course:** Utrains Python Fundamentals  
**Audience:** Beginners  
**Prerequisites:** Module 1 (print, input, arithmetic), Module 2 (variables, types, casting, f-strings preview)  
**Out of scope for now:** loops over strings (Module 5), regex, advanced formatting specs beyond basics

---

# Slide 1 — Title

## Strings in Python

**Today's question:**  
How does a computer store and work with **text**?

Names, passwords, file paths, emails, error messages, CSV lines —  
almost every real program manipulates strings.

**Instructor talking point:**  
Ask: "Where did you already use strings without naming them?"  
(Answer: `print("Hello")`, `input()`, Module 2 `str` type.)

---

# Slide 2 — Learning Objectives

By the end of this module, students will be able to:

1. Create strings with `'`, `"`, and `'''` / `"""`
2. Explain **immutability** and why `.upper()` returns a new string
3. Use **indexing** and **slicing** correctly (including reverse)
4. Use `len()`, `+`, `*`, and `in` / `not in`
5. Apply essential methods: case, strip, find, replace, split, join, checks
6. Format output with `.format()` and **f-strings**
7. Use escape sequences and **raw strings**
8. Clean and validate simple text (emails, filenames, usernames)

---

# Slide 3 — WHY Strings Matter (Motivation)

### Everyday situations → Python strings

| Real life | String job |
|-----------|------------|
| Name on a form | Store & display text |
| Login email | Clean + compare |
| `"report.pdf"` | Check file type |
| `"Alice,25,Dev"` | Split into parts |
| `"  hello  "` | Strip spaces before saving |

**Career connection (keep light):**

- **Backend:** request bodies, usernames, validation  
- **Data science:** cleaning columns of text  
- **AI:** prompts and labels are text  
- **Automation / DevOps:** paths, log lines, config values  

---

# Slide 4 — WHAT Is a String?

A **string** is a sequence of characters enclosed in quotes.

```python
name = "Sara"
city = 'Delhi'
```

**Analogy:**  
A string is like a **necklace of beads**.  
Each bead is a character. You can look at bead #0, #1, #2…  
but you cannot melt one bead and replace it in place — you build a new necklace.

**Ask the class:**  
Is `25` a string? Is `"25"` a string?  
(Module 2 reminder: types matter.)

---

# Slide 5 — Creating Strings (Syntax)

```python
a = 'single quotes'
b = "double quotes"
c = """multi
line
string"""
```

**Rule of thumb:**

- Use `"` when the text contains an apostrophe: `"It's fine"`
- Use `'` when the text contains double quotes: `'He said "Hi"'`
- Use triple quotes for multi-line text

```python
empty = ""          # empty string — length 0
```

**Mini challenge:**  
Write one string that contains both `'` and `"` without errors.

---

# Slide 6 — Empty String vs Space

```python
empty = ""
space = " "
```

| Value | `len(...)` | Meaning |
|-------|------------|---------|
| `""` | 0 | No characters |
| `" "` | 1 | One space character |

**Common mistake:** treating `" "` as "nothing".  
It is something — a space.

**Connection to Module 2:**  
`bool("")` is `False`, `bool(" ")` is `True`.

---

# Slide 7 — Immutability (Critical Concept)

**Immutable** = cannot be changed after creation.

```python
name = "alice"
print(name.upper())   # ALICE
print(name)           # alice  ← original unchanged
```

To "change" text, create a **new** string and reassign:

```python
name = name.upper()
print(name)           # ALICE
```

**Wrong (TypeError):**

```python
# name[0] = "A"
```

**Instructor tip:**  
Demonstrate live. Students often believe methods modify the original.

---

# Slide 8 — Indexing — WHY and WHAT

Why indexing?  
Sometimes you need **one character**: first letter, last digit, file extension tip.

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
word = "Python"
print(word[0])    # P
print(word[-1])   # n
```

**Trace:**

- `word[0]` → first character  
- `word[-1]` → last character (no need for `len`)

**Ask:** What is `word[2]`? (`t`)

---

# Slide 9 — Indexing Mistakes

```python
word = "Python"
# print(word[6])   # IndexError — valid indexes 0..5
```

| Mistake | Why it fails |
|---------|----------------|
| `word[6]` | Out of range |
| `word[-7]` | Out of range |
| Forgetting 0-based counting | First char is index 0, not 1 |

**Tip:** Last valid index = `len(word) - 1`

```python
print(len(word) - 1)  # 5
print(word[5])        # n
```

---

# Slide 10 — Slicing — SYNTAX

```python
text[start:stop:step]
```

- **start** included  
- **stop** excluded (most common beginner trap)  
- **step** optional (default 1)

```python
title = "Programming"
print(title[0:5])   # Progr
print(title[:6])    # Progra
print(title[3:])    # gramming
print(title[:])     # Programming
```

**Analogy:**  
Slicing is like cutting a ribbon — you mark where to start and where to stop cutting.  
The stop mark is **not** included in the piece you keep.

---

# Slide 11 — Trace a Slice

```python
word = "Programming"
print(word[0:5])
```

| Index | 0 | 1 | 2 | 3 | 4 | 5 | ... |
|-------|---|---|---|---|---|---|-----|
| Char | P | r | o | g | r | a | ... |

Start 0, stop 5 → include 0,1,2,3,4 → **`Progr`**

**Ask the class:**  
What is `word[0:4]`? → `Prog`

---

# Slide 12 — Step and Reverse

```python
word = "Programming"
print(word[::2])    # every 2nd character
print(word[::-1])   # reverse
```

**Trace `word[::-1]`:**  
Start from the end, step -1 → reverse the whole string.

**Practical uses:**

- Reverse for simple checks / puzzles  
- `::2` for sampling characters (less common, but teaches step)

**Mini challenge:**  
From `"Development"`, print every second character.

---

# Slide 13 — len(), +, *

```python
text = "Python"
print(len(text))          # 6

print("Hello" + " " + "World")  # Hello World
print("-" * 10)                 # ----------
print("Ha" * 3)                 # HaHaHa
```

**Connection to Module 2:**

```python
print("5" + "3")   # "53"  (concatenation, not math)
```

**Common mistake:**  
`len(text)` returns an `int`. Do not write `text.len()`.

---

# Slide 14 — Membership: `in` / `not in`

```python
email = "student@example.com"
print("@" in email)        # True
print("gmail" in email)    # False
print("xyz" not in email)  # True
```

**Why it exists:**  
Quickly ask: “Does this text contain that pattern?”

**Real use:**  
Validate that an email contains `@` before saving.

**Ask:** Does `"py" in "Python"` work?  
(Case sensitive! `"py" in "Python"` → `False`)

---

# Slide 15 — Case Methods

```python
text = "pYtHoN"

print(text.upper())       # PYTHON
print(text.lower())       # python
print(text.title())       # Python
print(text.capitalize())  # Python
print(text.swapcase())    # PyThOn
```

**Practical pattern (very common):**

```python
username = "  Admin  ".strip().lower()
```

Normalize before comparing passwords/usernames.

**Remember immutability:** assign if you need to keep the result.

---

# Slide 16 — strip / lstrip / rstrip

```python
raw = "   hello   "
print(raw.strip())   # "hello"
print(raw.lstrip())  # "hello   "
print(raw.rstrip())  # "   hello"
```

**Why?**  
Users type extra spaces. Files and CSVs often have messy whitespace.  
Cleaning text is a daily skill in data and backend work.

**Trace:**

```python
typed = "  admin  "
clean = typed.strip()
# clean → "admin"
```

---

# Slide 17 — Searching Methods

```python
text = "I love to code in Python"

print(text.find("code"))        # 10
print(text.find("Java"))        # -1  (not found)
print(text.count("o"))          # how many times
print(text.startswith("I "))    # True
print(text.endswith("Python"))  # True
```

| Method | If not found |
|--------|----------------|
| `find` | returns `-1` (safe) |
| `index` | raises `ValueError` |

**Common mistake:** treating `-1` as a valid index.

```python
# if text.find("x") == -1:  means "not found"
```

---

# Slide 18 — replace, split, join

```python
msg = "This is a bad day"
print(msg.replace("bad", "good"))

words = "Python is fun".split()
print(words)   # ['Python', 'is', 'fun']

print("-".join(["I", "love", "Python"]))  # I-love-Python
```

**Mental model:**

- `split` → string → list of pieces  
- `join` → pieces → one string  

**Common mistake:**

```python
# "-".join([1, 2, 3])   # TypeError — need strings
"-".join(["1", "2", "3"])  # OK
```

**Note for students:**  
Lists are Module 6. For now, treat `split()` / `join()` results as “a collection of text pieces” you can print.

---

# Slide 19 — Content Checks

```python
print("12345".isdigit())      # True
print("Python".isalpha())     # True
print("Hello123".isalnum())   # True
print("Hello 123".isalnum())  # False (space)
print("   ".isspace())        # True
```

**Practical:**

```python
phone = "9876543210"
print(phone.isdigit())  # basic validation
```

**Edge case:**  
`"".isdigit()` → `False` (empty is not digits)

---

# Slide 20 — Formatting: format() and f-strings

```python
name = "John"
age = 30
price = 49.99

print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
print(f"The price of the book is ${price}")
print(f"Price: ${price:.2f}")
```

**Why f-strings?**  
Readable, less error-prone, preferred in modern Python 3.

**Connection:** Module 2 introduced f-strings; Module 3 uses them heavily with string methods.

---

# Slide 21 — Escape Sequences and Raw Strings

```python
print("Hello\nWorld")     # newline
print("Name:\tAlice")     # tab
print("C:\\Users\\Ada")   # backslash
```

**Raw string** — backslashes stay literal:

```python
print(r"C:\newfolder\test")
print(r"Line1\nLine2")    # shows \n as text
```

**When to use raw strings:**  
Windows paths; later, regex patterns.

---

# Slide 22 — Trace Combined Example

```python
raw = "  sara  "
name = raw.strip().title()
print(f"Hello, {name}!")
```

**Trace:**

1. `raw` = `"  sara  "`  
2. `raw.strip()` → `"sara"`  
3. `"sara".title()` → `"Sara"`  
4. f-string → `Hello, Sara!`

**Ask:** What if we forget `.strip()`?  
Spaces remain inside the greeting.

---

# Slide 23 — Common Beginner Mistakes

1. **Expecting methods to mutate**  
   `name.upper()` without assignment leaves `name` unchanged.

2. **Off-by-one in slicing**  
   `"Python"[0:3]` is `"Pyt"`, not `"Pyth"`.

3. **IndexError**  
   Using an index ≥ `len(text)`.

4. **`find` → -1**  
   Thinking `-1` means last character (that is `text[-1]`).

5. **Case sensitivity**  
   `"Python".find("python")` → `-1`.

6. **`+` with int**  
   `"Age: " + 25` → `TypeError` (Module 2 casting).

7. **join with non-strings**  
   `",".join([1, 2])` → `TypeError`.

---

# Slide 24 — Professional Connection

| Task | String tools |
|------|----------------|
| Normalize email | `strip().lower()` |
| Check upload type | `endswith(".pdf")` |
| Parse CSV line | `split(",")` |
| Build log message | f-string |
| Clean user input | `strip()`, content checks |
| Mask / rebuild text | slicing + concatenation |

**Message:**  
Professionals clean and format text constantly. This module is not “just theory.”

---

# Slide 25 — Concept Recap

- Strings store text; created with quotes  
- Immutable → methods return new strings  
- Indexing / slicing access parts  
- `len`, `+`, `*`, `in`  
- Methods: case, strip, find, replace, split, join, is*  
- Formatting: `format`, f-strings  
- Escapes + raw strings  

---

# Slide 26 — Syntax Cheat Sheet

```python
s = "Python"
s[0], s[-1]
s[1:4], s[::-1]
len(s)
s + t, s * 3
"x" in s
s.upper(), s.lower(), s.title(), s.strip()
s.find("th"), s.count("t")
s.startswith("Py"), s.endswith("on")
s.replace("a", "b")
s.split(), "-".join(parts)
s.isdigit(), s.isalpha(), s.isalnum()
f"{name} is {age}"
r"C:\path"
```

---

# Slide 27 — Common Mistakes Checklist

- [ ] Did I assign the result of `.upper()` / `.strip()` if I need it later?  
- [ ] Is my slice stop exclusive?  
- [ ] Is my index within range?  
- [ ] Did I handle `find() == -1`?  
- [ ] Did I normalize case before comparing?  
- [ ] Did I cast numbers before concatenating with `+`?  

---

# Slide 28 — “Can You Explain This?”

Ask students to explain in their own words:

1. Why is a string immutable?  
2. Difference between `find` and `index`?  
3. Difference between `s[-1]` and `s.find("x") == -1`?  
4. Why `"Admin" == "admin"` is False?  
5. What does `stop` mean in a slice?  

---

# Slide 29 — Mini Coding Challenges (Live)

1. From `"hello world"`, produce `"HELLO"` without changing the original variable permanently unless assigned.  
2. Clean `"  User@Mail.COM "` into `"user@mail.com"`.  
3. From `"report.PDF"`, print whether it is a PDF (case-insensitive).  
4. Build: `Ada-Lovelace` from first and last name using `join` or `+`.  

---

# Slide 30 — What You Should Now Be Able To Do

Students should be able to:

- Read and trace string expressions  
- Predict outputs of indexing/slicing/methods  
- Spot and fix common string bugs  
- Write small programs that clean and format text  
- Combine strings with Module 1–2 skills (`input`, casting, f-strings)

---

# Slide 31 — Next Module Connection

**Module 4 — Operators and Expressions**

You will reuse strings with:

- comparison operators (`==`, `!=`)  
- membership operators (deeper practice)  
- logical operators in validations  

Later: loops (Module 5) to walk character by character; collections (Module 6) to store many strings.

---

# Slide 32 — Lab Directions

1. Study `module.py` — run it, read comments  
2. Complete `module_exercises.md` Levels 1 → 4  
3. Take the quiz (`module_quiz.json` / Moodle import as configured)  

**Instructor reminder:**  
Quiz tests understanding. Exercises build writing ability. Both are required.

---

*End of Module 3 teaching slides*
