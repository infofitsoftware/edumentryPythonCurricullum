# Module 8 — File Handling in Python

**For students (beginners)**  
**Prerequisites:** Modules 1–7 (I/O, types, strings, operators, control flow, collections, functions)  
**Next:** Module 9 — Important Modules  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Explain why programs use files  
2. Choose correct modes: `r`, `w`, `a`, `x`, and binary  
3. Open/close files safely (prefer `with`)  
4. Use `read`, `readline`, `readlines`, and line iteration  
5. Use `write` / `writelines` / append  
6. Check existence and delete with `os`  
7. Handle simple binary data  
8. Wrap file logic in functions  
9. Spot AI mistakes: `"w"` vs `"a"`, forgotten `with`, missing encoding  

---

## 2. Why file handling matters (AI era)

Variables live in memory. When the program ends, they disappear.  
**Files** keep data after the program stops.

| Place | File job |
|-------|----------|
| FastAPI / backend | logs, uploads, exports |
| Data pipelines | CSV / JSON / text datasets |
| AI / LLM apps | prompts saved to disk, prediction outputs, datasets |
| Automation / DevOps | reports, configs, inventory dumps |

```
Memory (variables)  → temporary
Files on disk       → persistent
```

**Golden rule:**  
If AI writes file code for you, check **mode (`w` vs `a`)**, **`with open(...)`**, and **`encoding="utf-8"`** for text. Those three hide most beginner disasters.

---

## 3. What is file handling?

File handling = opening a file, reading or writing text/bytes, then closing it.

Analogy: a notebook.

1. Open the notebook  
2. Read or write pages  
3. Close it so nothing is lost / locked  

---

## 4. File modes cheat sheet

| Mode | Meaning |
|------|---------|
| `"r"` | Read (file must exist) |
| `"w"` | Write (create / **overwrite**) |
| `"a"` | Append (add at the end) |
| `"x"` | Create only if missing |
| `"rb"` / `"wb"` / `"ab"` | Binary versions |

**Danger:** `"w"` erases existing content.  
AI often uses `"w"` when you meant `"a"`. Always double-check.

---

## 5. `open()` and `close()`

```python
file = open("sample.txt", "w", encoding="utf-8")
file.write("Hello\n")
file.close()
```

Always close — or better, use `with` (next section).

`encoding="utf-8"` is recommended for text (names, emoji, non-English characters).

---

## 6. `with` (preferred)

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
# file is auto-closed here
```

**Why prefer `with`?**

- Closes automatically  
- Safer if an error happens  
- Cleaner habit for professional code  

In modern Python (and AI-assisted coding), `with open(...)` is the default style.

---

## 7. Writing text

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

```python
lines = ["A\n", "B\n", "C\n"]
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

**Note:** `writelines` does **not** add newlines for you. Include `\n` yourself.

---

## 8. Append mode

```python
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("New line\n")
```

Use for logs and “add without destroying history”.

| Mode | Effect on existing file |
|------|-------------------------|
| `"w"` | wipe and rewrite |
| `"a"` | keep old content, add more |

---

## 9. Reading: `read()`

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

Reads the **entire** file into one string.  
Fine for small files. Be careful with huge files.

---

## 10. `readline` / `readlines` / loop

```python
line = file.readline()      # one line (includes \n)
lines = file.readlines()    # list of all lines
```

Best for large files — iterate line by line:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### Trace a read

File contents:

```
Line 1
Line 2
```

```python
with open("sample.txt", encoding="utf-8") as f:
    print(repr(f.readline()))
```

`repr` shows the hidden newline: `'Line 1\n'`  
`strip()` removes surrounding whitespace/newline.

---

## 11. Missing files and existence checks

```python
import os

if os.path.exists("data.txt"):
    print("Found")
else:
    print("File not found")
```

Opening with `"r"` when the file is missing → `FileNotFoundError`.

---

## 12. Delete files

```python
import os
os.remove("old.txt")
```

Only delete when you are sure. Prefer an exists-check first in beginner programs.

---

## 13. Exclusive create `"x"`

```python
with open("report.txt", "x", encoding="utf-8") as file:
    file.write("Fresh report\n")
```

If the file already exists → `FileExistsError`.  
Useful to avoid accidental overwrite.

---

## 14. Binary mode

```python
data = bytes([10, 20, 30])
with open("data.bin", "wb") as file:
    file.write(data)

with open("data.bin", "rb") as file:
    copied = file.read()
```

Use binary for images, audio, and other non-text formats.  
Do not mix text assumptions with binary data.

---

## 15. Functions + files (Module 7 combo)

```python
def save_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
```

This is how real projects package file logic.

---

## 16. Real-world preview (still beginner level)

### Logging

```python
def log_message(path, message):
    with open(path, "a", encoding="utf-8") as file:
        file.write(message + "\n")
```

### CSV-like data

```python
with open("students.csv", "w", encoding="utf-8") as file:
    file.write("name,score\n")
    file.write("Ada,90\n")
```

Then read lines, `split(",")`, convert types (Module 2).  
Later libraries (`csv`, `pandas`) build on this same idea.

### Save a cleaned AI prompt

```python
def save_prompt(path, prompt):
    clean = prompt.strip()
    with open(path, "w", encoding="utf-8") as file:
        file.write(clean + "\n")
```

You are not building FastAPI or pandas today.  
You are learning the exact file skills those systems rely on.

---

## 17. Common mistakes checklist

1. Using `"w"` instead of `"a"` and losing data  
2. Forgetting `with` / `close()`  
3. Not handling missing files in `"r"`  
4. Ignoring `\n` when comparing lines  
5. Treating binary and text as the same  
6. Hardcoded paths that only work on one machine  
7. Shipping AI file code without checking the mode  

---

## 18. How to study this lesson

1. Read one section  
2. Run `module.py` (it creates a demo folder, then deletes it)  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask whether mode should be `w` or `a`  
- Re-type the `with open(...)` block yourself  
- Run and open the file to verify  

---

## 19. Mini self-check (before the quiz)

Can you answer these out loud?

1. Difference between `"w"` and `"a"`?  
2. Why prefer `with`?  
3. `read` vs `readlines`?  
4. When do you use binary mode?  
5. What does `"x"` prevent?  
6. What error happens if you `"r"` a missing file?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 20. What “confident” means after Module 8

You can:

- persist program output to disk  
- reload saved data  
- build simple logs and CSV-like files  
- wrap load/save logic in functions  
- avoid common overwrite and missing-file bugs  
- review AI-generated file code for mode and `with` safety  

Next lesson (Module 9) covers **important modules** — `os`, `datetime`, `math`, `random`, and friends often used together with files.
