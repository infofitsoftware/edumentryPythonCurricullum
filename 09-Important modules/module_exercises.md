# Module 9 — Practice Exercises: Important Modules

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use the **standard library only** (no pip packages required).

---

## A. math / random / statistics

### A1. [E] Square root
Print `math.sqrt(144)`.

Expected: `12.0`

### A2. [E] Ceil and floor
Print `math.ceil(3.2)` and `math.floor(3.8)`.

### A3. [E] Dice roll
Print a random integer from 1 to 6 inclusive.

### A4. [E] Random choice
From `["python", "java", "go"]`, print one random language.

### A5. [E] Mean score
For `[80, 90, 100]`, print the mean.

Expected: `90`

### A6. [M] Seeded demo
Set `random.seed(42)`, then print `random.randint(1, 10)` twice in one program  
after resetting the seed before the second call too. Write a comment about reproducibility.

### A7. [M] Sample and shuffle
Sample 3 numbers from `range(1, 11)`, then shuffle `[1, 2, 3, 4, 5]` and print both.

---

## B. datetime / time / sys

### B1. [E] Today’s date
Print today’s date as `YYYY-MM-DD`.

### B2. [E] Formatted now
Print current datetime as `YYYY-MM-DD HH:MM:SS`.

### B3. [M] Parse a date
Parse `"2026-07-23"` with `strptime` and print `.date()`.

### B4. [M] Tiny timer
Record `time.time()` before and after `time.sleep(0.1)`. Print elapsed seconds rounded to 2 decimals.

### B5. [M] sys info
Print `sys.version.split()[0]` and `sys.platform`.

### B6. [C] argv awareness
Print `sys.argv`. Write a comment explaining what `argv[0]` is.

---

## C. os + files

### C1. [E] cwd and join
Print current working directory. Build a path with `os.path.join("data", "file.txt")` and print it.

### C2. [M] Make folder + file
Create a folder `_practice9` (or similar), write `hello.txt` inside it, print whether the file exists, then delete the folder with `shutil.rmtree`.

### C3. [M] Environment variable
Set `os.environ["COURSE_NAME"] = "PythonFundamentals"`, then print it with `.get`.  
Also print a missing key with default `"missing"`.

### C4. [C] AI bug: hardcoded slash
An AI wrote:
```python
path = "data\\file.txt"
```
Rewrite with `os.path.join` and explain why in a comment.

---

## D. json / csv

### D1. [E] dumps / loads
Convert `{"name": "Ada", "age": 36}` to a JSON string and back. Print the name.

### D2. [M] dump / load file
Save that dict to `person.json` with `json.dump`, reload with `json.load`, print the dict.  
Clean up the file afterward if you want.

### D3. [M] dumps vs dump
Write a comment: when do you use `dumps` vs `dump`?

### D4. [M] CSV write/read
Write two rows (`Ada,90` and `Bob,75`) with `csv.DictWriter`, then read with `DictReader`  
and print each name with `int(score)`.

### D5. [C] AI bug: CSV types
An AI printed `row["score"] + 1` without casting. Show the bug idea, then fix with `int(...)`.

---

## E. Combined / real-world

### E1. [M] summarize_scores
Write a function that returns a dict with `count`, `mean`, `max`, and `generated_at` (date string).  
Print it as JSON.

### E2. [M] stamp
Write `stamp(message)` that returns `"[YYYY-MM-DD HH:MM:SS] message"`.

### E3. [M] random_team
Write `random_team(names, size)` using `random.sample`. Test with 5 names and size 3.

### E4. [M] load_config
Save a small JSON config file, write `load_config(path)` using `json.load`, print one field.

### E5. [C] Mini score logger
Append one CSV row with today’s date, a student name, and a score.  
Then read all rows and print the mean score with `statistics.mean`.

### E6. [C] Prompt metadata (AI era)
Create a dict like:
```python
{"task": "summarize", "prompt": "Explain lists", "created_at": "..."}
```
Save it as JSON and reload it.

---

## F. Short written answers (as comments)

### F1. Standard library vs pip package?
Answer:

### F2. Why use `os.path.join`?
Answer:

### F3. Why use `random.seed` in demos/tests?
Answer:

### F4. Why must CSV scores often be cast with `int()`?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.

**Keep only these lesson files in this folder:**
- `module_notes.md`
- `module.py`
- `module_exercises.md`
- `module_quiz.xml`
