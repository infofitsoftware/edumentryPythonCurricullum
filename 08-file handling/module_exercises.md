# Module 8 — Practice Exercises: File Handling

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Prefer `with open(...)` and `encoding="utf-8"` for text.  
Create practice files in your working folder (or a subfolder you choose).

---

## A. Write and read basics

### A1. [E] Write a greeting
Write `"Hello, File Handling!\n"` to `hello.txt`, then read and print the content.

Expected:
```
Hello, File Handling!
```

### A2. [E] Write three lines
Write these lines to `lines.txt`, then print the file contents:

```
Python
Files
Rocks
```

### A3. [E] Append a line
Append `Again` to `lines.txt` and print all contents.

Expected:
```
Python
Files
Rocks
Again
```

### A4. [E] Exists check
Check whether `hello.txt` exists. Print `Found` or `Missing`.

### A5. [M] w vs a
Write a short comment explaining what would happen if Exercise A3 used `"w"` instead of `"a"`.

---

## B. Reading methods

### B1. [E] readline
Given a file with at least two lines, print only the first line using `readline()`, stripped.

### B2. [E] readlines
Read all lines into a list. Print the list length and the second line stripped.

### B3. [E] Count lines
Create a file with 4 lines. Print how many lines it has using a loop.

Expected: `4`

### B4. [M] Trace newlines
Write `"Line 1\n"` to a file. Print `repr(file.readline())` and then the stripped version.  
Write a comment about what `\n` is.

### B5. [M] Memory-friendly loop
Print every line of `lines.txt` using `for line in file:` (not `readlines()`).

---

## C. Functions + files

### C1. [M] save_text / load_text
Write:

```python
def save_text(path, text):
    ...

def load_text(path):
    ...
```

Save a short note, then load and print it.

### C2. [M] log_message
Write `log_message(path, message)` that **appends** a message plus newline.  
Log two messages and print the file.

### C3. [M] count_lines function
Write `count_lines(path)` that returns the number of lines. Test it.

### C4. [C] safe_load
Write `safe_load(path)` that returns the file text if it exists, otherwise returns `None`  
(use `os.path.exists`). Print a clear message for both cases.

---

## D. Modes, binary, exclusive create

### D1. [M] Exclusive create
Create `report.txt` with mode `"x"` and write one line.  
Then try creating it again in a commented block and write what error would occur.

### D2. [M] Binary round-trip
Write `bytes([1, 2, 3, 4])` to `data.bin` with `"wb"`, read it back with `"rb"`, and print the bytes.

### D3. [C] AI bug: overwrite log
An AI wrote:
```python
with open("app.log", "w", encoding="utf-8") as f:
    f.write("New event\n")
```
Explain why this is dangerous for a log file. Fix the mode.

---

## E. Real-world style (still beginner)

### E1. [M] CSV-like write
Create `students.csv` with:

```
name,score
Ada,90
Bob,75
```

### E2. [M] CSV-like read
Read `students.csv`, skip the header, and build a list of dicts like  
`{"name": "Ada", "score": 90}`. Print the list.

### E3. [M] Save cleaned prompt (AI era)
Write `save_prompt(path, prompt)` that strips the prompt and saves it.  
Test with `"  Summarize this article.  "`

### E4. [M] Append daily note
Create or append to `journal.txt` with today’s note string of your choice  
(use `"a"` so older notes survive).

### E5. [C] Score report
Read the CSV records from E2. Write `report.txt` containing:  
total students, average score, and the top scorer’s name.

### E6. [C] Cleanup helper
Write `delete_if_exists(path)` that removes a file only if it exists.  
Test it on a temporary practice file.

---

## F. Short written answers (as comments)

### F1. Why prefer `with open(...)`?
Answer:

### F2. Difference between `"w"` and `"a"`?
Answer:

### F3. When should you use binary mode?
Answer:

### F4. What does mode `"x"` prevent?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
