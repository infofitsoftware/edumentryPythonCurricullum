# Module 8 — File Handling in Python

**Course:** Utrains Python Fundamentals  
**Prerequisites:** Modules 1–7  
**Next:** Module 9 — Important Modules

---

# Slide 1 — Title

## File Handling in Python

**Big idea:** Save and load data that outlives your program.

```
Memory (variables)  → temporary
Files on disk       → persistent
```

---

# Slide 2 — Learning Objectives

1. Explain why programs use files  
2. Choose correct modes: `r`, `w`, `a`, `x`, binary  
3. Open/close files safely (prefer `with`)  
4. Use `read`, `readline`, `readlines`, line iteration  
5. Use `write` / `writelines` / append  
6. Check existence and delete with `os`  
7. Handle simple binary data  
8. Wrap file logic in functions  

---

# Slide 3 — WHY Files Matter

| Real need | File use |
|-----------|----------|
| App logs | append to `.log` |
| Settings | read config |
| Reports | write `.txt` / `.csv` |
| Images | binary read/write |
| Automation | process many files |

**Career:** backend logs, data pipelines, DevOps scripts, ML dataset loading.

---

# Slide 4 — WHAT Is File Handling?

File handling = opening a file, reading/writing bytes or text, then closing it.

**Analogy:** a notebook.

- Open notebook  
- Read or write pages  
- Close notebook so nothing is lost / locked  

---

# Slide 5 — File Modes Cheat Sheet

| Mode | Meaning |
|------|---------|
| `"r"` | Read (must exist) |
| `"w"` | Write (create/overwrite) |
| `"a"` | Append (add at end) |
| `"x"` | Create only if missing |
| `"rb"`/`"wb"`/`"ab"` | Binary versions |

**Danger:** `"w"` erases existing content.

---

# Slide 6 — open() and close()

```python
file = open("sample.txt", "w", encoding="utf-8")
file.write("Hello\n")
file.close()
```

Always close — or use `with` (next slide).

`encoding="utf-8"` recommended for text.

---

# Slide 7 — with (PREFERRED)

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
# auto-closed here
```

**Why prefer `with`?**

- Closes automatically  
- Safer if errors occur  
- Cleaner beginner habit for professional code  

---

# Slide 8 — Writing Text

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

**Note:** `writelines` does not add newlines for you.

---

# Slide 9 — Append Mode

```python
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("New line\n")
```

Use for logs and “add without destroying history”.

**Ask:** What would `"w"` do instead?

---

# Slide 10 — Reading: read()

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

Reads **entire** file into one string.  
Fine for small files; careful with huge files.

---

# Slide 11 — readline / readlines / loop

```python
line = file.readline()      # one line (includes \n)
lines = file.readlines()    # list of lines
```

Best for large files:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

---

# Slide 12 — Trace a Read

File contents:

```
Line 1
Line 2
```

```python
with open("sample.txt") as f:
    print(repr(f.readline()))
```

Output idea: `'Line 1\n'`  
`strip()` removes surrounding whitespace/newline.

---

# Slide 13 — FileNotFoundError & Exists

```python
import os

if os.path.exists("data.txt"):
    ...
else:
    print("File not found")
```

`"r"` on missing file → `FileNotFoundError`.

---

# Slide 14 — Delete Files

```python
import os
os.remove("old.txt")
```

Only delete when you are sure. Prefer exists-check first in beginner programs.

---

# Slide 15 — Exclusive Create `"x"`

```python
with open("report.txt", "x", encoding="utf-8") as file:
    file.write("Fresh report\n")
```

If file already exists → `FileExistsError`.  
Useful to avoid accidental overwrite.

---

# Slide 16 — Binary Mode

```python
data = bytes([10, 20, 30])
with open("data.bin", "wb") as file:
    file.write(data)

with open("data.bin", "rb") as file:
    copied = file.read()
```

Use binary for images, audio, non-text formats.

---

# Slide 17 — Functions + Files

```python
def save_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
```

This is how Module 7 + Module 8 combine in real projects.

---

# Slide 18 — Mini Pattern: Logging

```python
def log_message(path, message):
    with open(path, "a", encoding="utf-8") as file:
        file.write(message + "\n")
```

Automation / DevOps style: append status lines over time.

---

# Slide 19 — Mini Pattern: CSV-like Data

```python
with open("students.csv", "w", encoding="utf-8") as file:
    file.write("name,score\n")
    file.write("Ada,90\n")
```

Then read lines, `split(",")`, convert types (Module 2).  
Later libraries (`csv`, `pandas`) build on this idea.

---

# Slide 20 — Common Beginner Mistakes

1. Using `"w"` instead of `"a"` and losing data  
2. Forgetting `with` / `close()`  
3. Not handling missing files in `"r"`  
4. Ignoring `\n` when comparing lines  
5. Assuming binary and text are the same  
6. Hardcoded paths that break on other machines  

---

# Slide 21 — Professional Connection

| Domain | Files |
|--------|-------|
| Backend | logs, uploads, exports |
| Data science | CSV/JSON datasets |
| AI | model weights, prediction outputs |
| Automation | report generation |
| DevOps | configs, inventory dumps |

---

# Slide 22 — Concept Recap

- Modes: r/w/a/x + binary  
- Prefer `with open(...)`  
- read / readline / readlines / iterate  
- write / writelines / append  
- `os.path.exists`, `os.remove`  

---

# Slide 23 — Syntax Cheat Sheet

```python
with open(path, "w", encoding="utf-8") as f:
    f.write("text\n")

with open(path, "r", encoding="utf-8") as f:
    data = f.read()

with open(path, "a", encoding="utf-8") as f:
    f.write("more\n")

os.path.exists(path)
os.remove(path)
```

---

# Slide 24 — Mistakes Checklist

- [ ] Correct mode (`w` vs `a`)?  
- [ ] Using `with`?  
- [ ] Encoding set for text?  
- [ ] Exists-check before read/delete?  
- [ ] Newlines included where needed?  

---

# Slide 25 — “Can You Explain This?”

1. Difference between `"w"` and `"a"`?  
2. Why prefer `with`?  
3. `read` vs `readlines`?  
4. When use binary mode?  
5. What does `"x"` prevent?  

---

# Slide 26 — Mini Challenges

1. Write three lines to a file, then print them  
2. Append a fourth line  
3. Count lines in a file with a loop  
4. Wrap load/save in functions  

---

# Slide 27 — What You Can Do Now

- Persist program output to disk  
- Reload saved data  
- Build simple logs and CSV-like files  
- Avoid common overwrite bugs  

---

# Slide 28 — Next Module

**Module 9 — Important Modules**  
`os`, `datetime`, `math`, `random`, etc., often used together with files.

---

# Slide 29 — Lab Directions

1. Run `module.py` (creates then deletes a demo folder)  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 8 teaching slides*
