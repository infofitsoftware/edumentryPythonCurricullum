# Module 9 — Practice Exercises: Important Modules

**Instructions:** Attempt before opening the Instructor Solution Guide. Use the standard library only (no pip packages required).

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Square Root

**Difficulty:** Easy  
**Concepts:** `math`  

**Problem:** Print `math.sqrt(144)`.

**Expected Output:**
```
12.0
```

**Hint:** `import math`

---

### Exercise 2 — Dice Roll

**Difficulty:** Easy  
**Concepts:** `random`  

**Problem:** Print a random integer from 1 to 6 inclusive.

**Hint:** `random.randint(1, 6)` (output varies)

---

### Exercise 3 — Random Choice

**Difficulty:** Easy  
**Concepts:** `random.choice`  

**Problem:** From `["python", "java", "go"]`, print one random language.

**Hint:** Output varies.

---

### Exercise 4 — Today’s Date

**Difficulty:** Easy  
**Concepts:** `datetime`  

**Problem:** Print today’s date in `YYYY-MM-DD` format.

**Hint:** `datetime.date.today().strftime("%Y-%m-%d")`

---

### Exercise 5 — Mean Score

**Difficulty:** Easy  
**Concepts:** `statistics`  

**Problem:** For `[80, 90, 100]`, print the mean.

**Expected Output:**
```
90
```

**Hint:** `statistics.mean(...)`

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Ceil and Floor

**Difficulty:** Easy  
**Concepts:** `math`  

**Problem:** Print `math.ceil(3.2)` and `math.floor(3.2)` on two lines.

**Expected Output:**
```
4
3
```

---

### Exercise 7 — Seeded Random

**Difficulty:** Medium  
**Concepts:** `random.seed`  

**Problem:** Call `random.seed(1)` then print `random.randint(1, 100)` twice in a fresh mental model: with seed reset before each program run, first value is reproducible.  
Print one value after `seed(1)`.

**Expected Output:**
```
18
```
(Using Python’s RNG after `seed(1)` → first `randint(1,100)` is 18 in current CPython; if your version differs, print your value and note it.)

**Hint:** Instructor solution uses `seed(1)` then one `randint`.

---

### Exercise 8 — Format Now

**Difficulty:** Easy  
**Concepts:** `strftime`  

**Problem:** Print current datetime formatted as `YYYY-MM-DD HH:MM` (minute precision is fine).

**Hint:** `"%Y-%m-%d %H:%M"`

---

### Exercise 9 — Join Path

**Difficulty:** Easy  
**Concepts:** `os.path.join`  

**Problem:** Print `os.path.join("data", "raw", "input.csv")`.

**Hint:** Do not hardcode `data/raw/...` with slashes only.

---

### Exercise 10 — Env Default

**Difficulty:** Easy  
**Concepts:** `os.environ.get`  

**Problem:** Print `os.environ.get("NOT_A_REAL_KEY", "missing")`.

**Expected Output:**
```
missing
```

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — JSON Round-Trip String

**Difficulty:** Medium  
**Concepts:** `json.dumps` / `loads`  

**Problem:** Convert `{"course": "Python", "level": 1}` to a JSON string and back. Print the `course` value after loading.

**Expected Output:**
```
Python
```

---

### Exercise 12 — JSON File Save/Load

**Difficulty:** Medium  
**Concepts:** `json.dump` / `load`, files  

**Problem:** Save `{"name": "Ada", "score": 95}` to `student.json`, load it, print `score`.

**Expected Output:**
```
95
```

---

### Exercise 13 — CSV Write/Read

**Difficulty:** Medium  
**Concepts:** `csv.DictWriter` / `DictReader`  

**Problem:** Write `scores.csv` with header `name,score` and rows Ada/90, Bob/80. Read and print each `name:score`.

**Expected Output:**
```
Ada:90
Bob:80
```

**Hint:** `newline=""` when opening for csv.

---

### Exercise 14 — List Directory Count

**Difficulty:** Medium  
**Concepts:** `os.listdir`, files  

**Problem:** Create folder `demo9` with two text files. Print how many items `os.listdir("demo9")` returns.

**Expected Output:**
```
2
```

---

### Exercise 15 — Summary Dict + JSON

**Difficulty:** Medium  
**Concepts:** statistics + datetime + json  

**Problem:** For scores `[70, 80, 90]`, build dict with `mean` and `date` (today `YYYY-MM-DD`). Print `json.dumps` result containing both keys.

**Hint:** Use `statistics.mean` and `datetime.date.today()`.

---

### Exercise 16 — Parse Date

**Difficulty:** Medium  
**Concepts:** `strptime`  

**Problem:** Parse `"2026-12-25"` with `"%Y-%m-%d"` and print the month number.

**Expected Output:**
```
12
```

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Random Team Picker Function

**Difficulty:** Medium  
**Concepts:** functions + random  

**Problem:** Write `pick_team(names, k)` returning `random.sample(names, k)`.  
Demo with 5 names and `k=2`, print length of result.

**Expected Output:**
```
2
```

---

### Exercise 18 — CLI Arg Echo

**Difficulty:** Medium  
**Concepts:** `sys.argv`  

**Problem:** Write a script that prints `No argument` if only script name is present, else prints the first CLI argument.

**Example:**
```
python echo_arg.py hello
```
→ `hello`

**Hint:** `len(sys.argv)`

---

### Exercise 19 — CSV Average

**Difficulty:** Challenging  
**Concepts:** csv + casting + statistics  

**Problem:** Using the CSV from Exercise 13 (or recreate), compute average score and print as float.

**Expected Output:**
```
85.0
```

---

### Exercise 20 — Mini Config Tool

**Difficulty:** Challenging  
**Concepts:** json + os + functions  

**Problem:**

1. Write `save_config(path, data)` and `load_config(path)` using JSON.  
2. Save `{"env": "dev", "debug": True}` to `config.json`.  
3. Load and print `env`.

**Expected Output:**
```
dev
```

---

# Instructor Solution Guide

```python
import math
import random
import statistics
import datetime
import os
import sys
import json
import csv

# Exercise 1
print(math.sqrt(144))

# Exercise 2
print(random.randint(1, 6))

# Exercise 3
print(random.choice(["python", "java", "go"]))

# Exercise 4
print(datetime.date.today().strftime("%Y-%m-%d"))

# Exercise 5
print(statistics.mean([80, 90, 100]))

# Exercise 6
print(math.ceil(3.2))
print(math.floor(3.2))

# Exercise 7
random.seed(1)
print(random.randint(1, 100))

# Exercise 8
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

# Exercise 9
print(os.path.join("data", "raw", "input.csv"))

# Exercise 10
print(os.environ.get("NOT_A_REAL_KEY", "missing"))

# Exercise 11
text = json.dumps({"course": "Python", "level": 1})
data = json.loads(text)
print(data["course"])

# Exercise 12
with open("student.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Ada", "score": 95}, f)
with open("student.json", "r", encoding="utf-8") as f:
    print(json.load(f)["score"])

# Exercise 13
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Ada", "score": "90"})
    writer.writerow({"name": "Bob", "score": "80"})
with open("scores.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(f"{row['name']}:{row['score']}")

# Exercise 14
os.makedirs("demo9", exist_ok=True)
open(os.path.join("demo9", "a.txt"), "w", encoding="utf-8").write("a")
open(os.path.join("demo9", "b.txt"), "w", encoding="utf-8").write("b")
print(len(os.listdir("demo9")))

# Exercise 15
payload = {
    "mean": statistics.mean([70, 80, 90]),
    "date": datetime.date.today().strftime("%Y-%m-%d"),
}
print(json.dumps(payload))

# Exercise 16
dt = datetime.datetime.strptime("2026-12-25", "%Y-%m-%d")
print(dt.month)

# Exercise 17
def pick_team(names, k):
    return random.sample(names, k)

print(len(pick_team(["Ada", "Bob", "Cam", "Dee", "Eve"], 2)))

# Exercise 18
if len(sys.argv) < 2:
    print("No argument")
else:
    print(sys.argv[1])

# Exercise 19
scores = []
with open("scores.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        scores.append(float(row["score"]))
print(statistics.mean(scores))

# Exercise 20
def save_config(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

save_config("config.json", {"env": "dev", "debug": True})
print(load_config("config.json")["env"])
```
