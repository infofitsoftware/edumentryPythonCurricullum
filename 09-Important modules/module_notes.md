# Module 9 — Important Modules

**Course:** Utrains Python Fundamentals  
**Prerequisites:** Modules 1–8  
**Focus:** Python standard library essentials (+ career preview)

---

# Slide 1 — Title

## Important Python Modules

**Big idea:** Don’t reinvent tools that already ship with Python.

```
import module
# use ready-made functions/classes
```

---

# Slide 2 — Learning Objectives

1. Explain what a module is and how to `import`  
2. Use `math`, `random`, `statistics`  
3. Work with `datetime` / `time`  
4. Use `os` / `os.path` and env vars  
5. Read basic `sys` info (`version`, `platform`, `argv`)  
6. Save/load data with `json` and `csv`  
7. Combine modules with functions and files  
8. Know which third-party modules come next by career path  

---

# Slide 3 — WHY Modules?

| Without modules | With modules |
|-----------------|--------------|
| Write square root yourself | `math.sqrt` |
| Hand-roll date formatting | `datetime` |
| Manual CSV parsing only | `csv` |
| Custom JSON text building | `json` |

Modules = productivity + fewer bugs.

---

# Slide 4 — WHAT Is a Module?

A **module** is a Python file containing reusable code.

Kinds:

1. **Standard library** — included with Python  
2. **Third-party** — install with `pip`  
3. **Your modules** — your own `.py` files  

This module focuses on (1).

---

# Slide 5 — Import Syntax

```python
import math
print(math.sqrt(9))

from math import sqrt
print(sqrt(9))

from math import sqrt as square_root
```

**Ask:** Why might `import math` be clearer than many `from math import *`?

---

# Slide 6 — math

```python
import math
math.pi
math.sqrt(16)
math.ceil(3.2)    # 4
math.floor(3.8)   # 3
math.factorial(5) # 120
```

Useful in games, geometry, ML feature scaling later.

---

# Slide 7 — random

```python
import random
random.randint(1, 6)
random.choice(["a", "b", "c"])
random.sample(range(1, 11), 3)
random.shuffle(my_list)
```

```python
random.seed(42)  # reproducible results for demos/tests
```

**Career:** simulations, train/test splits (conceptual), randomized quizzes.

---

# Slide 8 — statistics

```python
import statistics
statistics.mean([90, 80, 70])
statistics.median([1, 3, 2])
```

Lightweight data summary before pandas.

---

# Slide 9 — datetime

```python
import datetime
now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")
datetime.datetime.strptime("2026-07-23", "%Y-%m-%d")
```

**Analogy:** calendar + clock object.

Logs, reports, scheduling all need timestamps.

---

# Slide 10 — time

```python
import time
time.time()     # seconds since epoch
time.sleep(1)   # pause
```

Use for simple delays and timing code.

---

# Slide 11 — os basics

```python
import os
os.getcwd()
os.listdir(".")
os.makedirs("data", exist_ok=True)
os.path.join("data", "file.txt")
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)
```

Connects tightly to Module 8 file handling.

---

# Slide 12 — Environment Variables

```python
os.environ["APP_ENV"] = "dev"
print(os.environ.get("APP_ENV"))
print(os.environ.get("API_KEY", "missing"))
```

**Why:** keep secrets/config out of source code (DevOps/backend practice).

Preview: later tools like `python-dotenv` load `.env` files.

---

# Slide 13 — sys

```python
import sys
sys.version
sys.platform
sys.argv   # command-line arguments
```

```bash
python app.py input.csv
# sys.argv[0] -> app.py
# sys.argv[1] -> input.csv
```

---

# Slide 14 — json (CRITICAL)

JSON = common data format for APIs and configs.

```python
import json
text = json.dumps({"name": "Ada", "age": 36})
data = json.loads(text)

json.dump(data, file)
data = json.load(file)
```

| Function | Direction |
|----------|-----------|
| `dumps`/`loads` | Python ↔ string |
| `dump`/`load` | Python ↔ file |

**Career:** backend APIs, AI prompts/metadata, automation payloads.

---

# Slide 15 — Trace JSON

```python
person = {"name": "Ada", "skills": ["python"]}
text = json.dumps(person)
back = json.loads(text)
print(back["skills"][0])
```

**Trace:** dict → string → dict → `"python"`

---

# Slide 16 — csv

```python
import csv
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Ada", "score": "90"})
```

```python
with open("scores.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], int(row["score"]))
```

`newline=""` avoids blank-line issues on Windows.

---

# Slide 17 — Combining Modules

```python
summary = {
    "mean": statistics.mean(scores),
    "generated_at": datetime.datetime.now().strftime("%Y-%m-%d"),
}
json.dumps(summary)
```

Real scripts mix: `os` + `json`/`csv` + `datetime` + your functions.

---

# Slide 18 — Career Preview (Third-Party)

| Path | Next modules (pip) |
|------|---------------------|
| Backend | `requests`, Flask/FastAPI/Django |
| Data | `pandas`, `matplotlib` |
| AI/ML | `numpy`, `scikit-learn`, PyTorch |
| Automation | `requests`, schedule libraries |
| DevOps | `boto3`, cloud CLIs, later Docker SDKs |

All of them assume Modules 1–9 fundamentals.

---

# Slide 19 — What We Intentionally Deferred

Advanced/third-party topics from older notes (Docker SDK, Kubernetes, Terraform, Jenkins API) are **career electives**, not beginner required installs.

Learn them after you are solid with:

functions · collections · files · json · os

---

# Slide 20 — Common Mistakes

1. Forgetting to `import`  
2. Confusing `json.dumps` (string) vs `json.dump` (file)  
3. Not converting CSV strings with `int()`/`float()`  
4. Hardcoding `\` paths instead of `os.path.join`  
5. Expecting `random` to be reproducible without `seed`  
6. Using third-party imports without `pip install`  

---

# Slide 21 — Concept Recap

- import styles  
- math / random / statistics  
- datetime / time  
- os / env / sys  
- json / csv  
- standard library first, pip later  

---

# Slide 22 — Syntax Cheat Sheet

```python
import math, random, json, csv, os, sys, datetime, statistics
math.sqrt(9)
random.randint(1, 10)
json.dumps(data); json.loads(text)
os.path.join("a", "b")
datetime.datetime.now().strftime("%Y-%m-%d")
```

---

# Slide 23 — Mistakes Checklist

- [ ] Imported the module?  
- [ ] Used `dumps/loads` vs `dump/load` correctly?  
- [ ] Cast CSV values?  
- [ ] Used `newline=""` with csv on Windows?  
- [ ] Built paths with `os.path.join`?  

---

# Slide 24 — “Can You Explain This?”

1. Standard library vs pip package?  
2. `dumps` vs `dump`?  
3. Why `os.path.join`?  
4. Why `random.seed`?  
5. What is `sys.argv` for?  

---

# Slide 25 — Mini Challenges

1. Mean of a list with `statistics`  
2. Save a dict to `data.json` and reload  
3. Write/read two CSV rows  
4. Print today’s date as `YYYY-MM-DD`  

---

# Slide 26 — What You Can Do Now

- Use built-in modules confidently  
- Persist structured data (JSON/CSV)  
- Handle dates, randomness, basic OS paths  
- Prepare for framework/library learning  

---

# Slide 27 — Course Capstone Direction

You can now build small tools such as:

- quiz score logger (csv + datetime)  
- config loader (json + os)  
- random practice generator (random + functions)  

---

# Slide 28 — Lab Directions

1. Run `module.py`  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 9 teaching slides*
