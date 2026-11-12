# Module 3 — Strings in Python

**For students (beginners)**  
**Prerequisites:** Module 1 (`print`, `input`, arithmetic), Module 2 (variables, types, casting)  
**Next:** Module 4 — Operators  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Create strings with `'`, `"`, and triple quotes  
2. Explain **immutability** (why `.upper()` does not change the original)  
3. Use **indexing** and **slicing** (including reverse)  
4. Use `len()`, `+`, `*`, and `in` / `not in`  
5. Apply essential methods: case, strip, find, replace, split, join, checks  
6. Format text with f-strings  
7. Use escape sequences and raw strings  
8. Clean and validate simple text (emails, filenames, usernames, prompts)

---

## 2. Why strings matter (AI era)

Almost every real program works with text:

| Place | String job |
|-------|------------|
| FastAPI / forms | usernames, emails, error messages |
| JSON / CSV | field values arrive as text |
| AI / LLM apps | **prompts**, labels, model replies |
| Automation | file paths, log lines, config keys |

**Golden rule:**  
If AI writes string code for you, check **cleaning**, **case**, and **immutability**. Those three hide most bugs.

---

## 3. What is a string?

A **string** is a sequence of characters inside quotes.

```python
name = "Sara"
city = 'Delhi'
```

Think of a string like a **necklace of beads**.  
Each bead is one character. You can look at bead #0, #1, #2…  
but you cannot melt one bead in place — you build a new necklace.

Reminder from Module 2:

- `25` is an `int`  
- `"25"` is a `str`

---

## 4. Creating strings

```python
a = 'single quotes'
b = "double quotes"
c = """multi
line
string"""
```

**Rules of thumb:**

- Use `"` when the text has an apostrophe: `"It's fine"`  
- Use `'` when the text has double quotes: `'He said "Hi"'`  
- Use triple quotes for multi-line text  

```python
empty = ""     # length 0 — no characters
space = " "    # length 1 — one space character
```

`""` and `" "` are **not** the same.  
A space is still a character.  
Also: `bool("")` is `False`, but `bool(" ")` is `True`.

---

## 5. Immutability (must understand)

**Immutable** means: you cannot change a character inside an existing string.

```python
name = "alice"
print(name.upper())   # ALICE
print(name)           # alice  ← original unchanged
```

To keep a change, **reassign**:

```python
name = name.upper()
print(name)           # ALICE
```

This is wrong (TypeError):

```python
# name[0] = "A"
```

Correct way to “edit” one letter: build a new string:

```python
name = "alice"
fixed = "A" + name[1:]
print(fixed)          # Alice
```

AI often calls `.replace()` or `.upper()` and forgets to save the result. Watch for that.

---

## 6. Indexing

Each character has a position (index). Counting starts at **0**.

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
word = "Python"
print(word[0])    # P  (first)
print(word[-1])   # n  (last)
print(word[2])    # t
```

**Common mistakes:**

- `word[6]` → IndexError (valid indexes are 0…5)  
- Thinking the first character is index 1  

Last valid index = `len(word) - 1`.

---

## 7. Slicing

```python
text[start:stop:step]
```

- **start** is included  
- **stop** is **not** included (biggest beginner trap)  
- **step** is optional (default 1)

```python
title = "Programming"
print(title[0:5])   # Progr
print(title[:6])    # Progra
print(title[3:])    # gramming
print(title[:])     # Programming
print(title[::2])   # every 2nd character
print(title[::-1])  # reverse
```

Trace `title[0:5]`:

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Char  | P | r | o | g | r | a |

Include 0–4 → **`Progr`**

---

## 8. `len()`, `+`, `*`

```python
print(len("Python"))           # 6
print("Hello" + " " + "World") # Hello World
print("Ha" * 3)                # HaHaHa
print("-" * 10)                # ----------
```

- `len(text)` returns an `int` — there is no `text.len()`  
- `"5" + "3"` is `"53"` (concatenation), not math  

---

## 9. Membership: `in` / `not in`

```python
email = "student@example.com"
print("@" in email)        # True
print("gmail" in email)    # False
print("xyz" not in email)  # True
```

Case matters: `"py" in "Python"` → `False`.

Real use: check that an email contains `@` before saving.

---

## 10. Case methods

```python
text = "pYtHoN"
print(text.upper())       # PYTHON
print(text.lower())       # python
print(text.title())       # Python
print(text.capitalize())  # Python
print(text.swapcase())    # PyThOn
```

Very common cleaning pattern:

```python
username = "  Admin  ".strip().lower()
# "admin"
```

Normalize before comparing usernames, emails, or flags.

---

## 11. Strip whitespace

```python
raw = "   hello   "
print(raw.strip())   # "hello"
print(raw.lstrip())  # "hello   "
print(raw.rstrip())  # "   hello"
```

Users type extra spaces. CSV and form data often do too.  
Cleaning text is a daily skill in backend, data, and AI pipelines.

---

## 12. Find, count, startswith, endswith

```python
sentence = "I love to code in Python"
print(sentence.find("code"))       # 10
print(sentence.find("Java"))       # -1 (not found — safe)
print(sentence.count("o"))         # 4
print(sentence.startswith("I "))   # True
print(sentence.endswith("Python")) # True
```

- `find` → `-1` means missing  
- `index` → same idea, but raises **ValueError** if missing  

File checks (automation style):

```python
script = "backup.py"
print(script.endswith(".py"))  # True
```

---

## 13. replace, split, join

```python
print("This is a bad day".replace("bad", "good"))
# This is a good day

print("Python is fun".split())
# ['Python', 'is', 'fun']

print("Alice,25,Engineer".split(","))
# ['Alice', '25', 'Engineer']

print("-".join(["I", "love", "Python"]))
# I-love-Python
```

Notes:

- `replace` returns a **new** string (assign if you need it)  
- `join` needs a list of **strings** — `"-".join([1, 2, 3])` is TypeError  

---

## 14. Content checks

```python
print("12345".isdigit())      # True
print("Python".isalpha())     # True
print("Hello123".isalnum())   # True
print("Hello 123".isalnum())  # False (space)
print("   ".isspace())        # True
print("".isdigit())           # False
```

Useful for simple validation: phone digits, usernames, empty input.

---

## 15. f-strings (preferred formatting)

```python
name = "John"
age = 30
price = 49.99
print(f"{name} is {age}")
print(f"Price: ${price:.2f}")
print(f"Total: {3 * 12.5}")
```

You may also see `.format()`:

```python
print("My name is {}.".format(name))
```

In new code, prefer f-strings.

---

## 16. Escape sequences and raw strings

```python
print("Hello\nWorld")           # newline
print("Name:\tAlice")           # tab
print("Path: C:\\Users\\Ada")   # backslashes
print("She said \"Hi\"")
```

**Raw strings** (`r"..."`) treat `\` as a normal character — useful for Windows paths:

```python
print(r"C:\newfolder\test")
print(r"Line1\nLine2")   # prints \n literally
```

---

## 17. Real-world preview (still beginner level)

### Clean an email before storing

```python
raw = "  Student@Example.COM  "
email = raw.strip().lower()
print(email)            # student@example.com
print("@" in email)     # True
```

### Normalize a filename

```python
uploaded = "  Invoice_March.PDF  "
name = uploaded.strip().lower()
print(name.endswith(".pdf"))  # True
```

### AI prompt cleaning idea

```python
prompt = "  Summarize this article.  "
clean_prompt = prompt.strip()
print(f"Prompt length: {len(clean_prompt)}")
```

You are not building FastAPI or an LLM app today.  
You are learning the exact string skills those systems need.

---

## 18. Common mistakes checklist

1. Believing `.upper()` / `.replace()` changes the original without assignment  
2. Forgetting slice **stop** is exclusive (`"Python"[0:3]` → `"Pyt"`)  
3. Treating `find(...) == -1` as a real character index  
4. Using `" "` as if it were empty  
5. Joining numbers without converting to `str` first  
6. Case-sensitive membership (`"py" in "Python"` is False)  
7. Shipping AI string code without `strip()` / `lower()` when comparing text  

---

## 19. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask it to explain **why**  
- Re-type the fix yourself  
- Run and verify  

---

## 20. Mini self-check (before the quiz)

Can you answer these out loud?

1. What does immutable mean for strings?  
2. What is `"Programming"[0:5]`?  
3. Why does `name.upper()` leave `name` unchanged?  
4. What does `find` return when text is missing?  
5. How do you clean `"  Admin  "` into `"admin"`?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 21. What “confident” means after Module 3

You can:

- create and index/slice strings safely  
- clean and normalize text  
- use the core string methods without guessing  
- spot AI mistakes around immutability and case  
- connect strings to forms, files, CSV, and AI prompts  

Next lesson (Module 4) covers **operators** — the rules that power comparisons and conditions.
