# Module 9 — Important Modules

**For students (beginners)**  
**Prerequisites:** Modules 1–8 (especially files + functions)  
**Next:** Module 10 — Classes and Objects  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Explain what a module is and how to `import`  
2. Use `math`, `random`, and `statistics`  
3. Work with `datetime` / `time`  
4. Use `os` / `os.path` and environment variables  
5. Read basic `sys` info (`version`, `platform`, `argv`)  
6. Save/load data with `json` and `csv`  
7. Combine modules with functions and files  
8. Know which third-party modules come next by career path (preview only)  

---

## 2. Why modules matter (AI era)

Don’t reinvent tools that already ship with Python.

| Place | Module job |
|-------|------------|
| FastAPI / backend | `json` payloads, `datetime` timestamps, `os` config |
| Data scripts | `csv`, `statistics` |
| AI / LLM apps | `json` for messages/metadata, `random` for sampling demos |
| Automation / DevOps | `os`, `sys.argv`, env vars, logs with timestamps |

**Golden rule:**  
If AI writes `import` code for you, check whether the module is **standard library** (no install) or **third-party** (`pip install`). Beginners often crash on missing packages.

---

## 3. What is a module?

A **module** is a Python file containing reusable code.

Kinds:

1. **Standard library** — included with Python (today’s focus)  
2. **Third-party** — install with `pip` later  
3. **Your modules** — your own `.py` files  

```
import module
# use ready-made functions/classes
```

---

## 4. Import syntax

```python
import math
print(math.sqrt(9))

from math import sqrt
print(sqrt(9))

from math import sqrt as square_root
print(square_root(9))
```

Prefer clear imports. Avoid `from math import *` — it hides where names come from (harder to debug AI code too).

---

## 5. `math`

```python
import math
print(math.pi)
print(math.sqrt(16))
print(math.ceil(3.2))     # 4
print(math.floor(3.8))    # 3
print(math.factorial(5))  # 120
```

Useful in games, geometry, and later ML feature work.

---

## 6. `random`

```python
import random
random.seed(42)  # reproducible demos/tests
print(random.randint(1, 6))
print(random.choice(["a", "b", "c"]))
print(random.sample(range(1, 11), 3))

my_list = [1, 2, 3, 4]
random.shuffle(my_list)
```

Without `seed`, results change every run.  
With `seed`, demos and tests can match.

---

## 7. `statistics`

```python
import statistics
print(statistics.mean([90, 80, 70]))
print(statistics.median([1, 3, 2]))
```

Lightweight summaries before you learn pandas later.

---

## 8. `datetime` and `time`

```python
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.date.today())

parsed = datetime.datetime.strptime("2026-07-23", "%Y-%m-%d")
```

Analogy: calendar + clock object.  
Logs, reports, and scheduling all need timestamps.

```python
import time
print(time.time())   # seconds since epoch
time.sleep(1)        # pause
```

---

## 9. `os` / `os.path` (extends Module 8)

```python
import os
print(os.getcwd())
print(os.listdir("."))
os.makedirs("data", exist_ok=True)
path = os.path.join("data", "file.txt")
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir("data"))
```

Use `os.path.join` instead of hardcoding `\` or `/` so paths work across machines.

### Environment variables

```python
os.environ["APP_ENV"] = "dev"
print(os.environ.get("APP_ENV"))
print(os.environ.get("API_KEY", "missing"))
```

**Why:** keep secrets/config out of source code.  
Later tools like `python-dotenv` can load `.env` files — preview only for now.

---

## 10. `sys`

```python
import sys
print(sys.version)
print(sys.platform)
print(sys.argv)   # command-line arguments
```

```bash
python app.py input.csv
# sys.argv[0] -> app.py
# sys.argv[1] -> input.csv
```

---

## 11. `json` (critical)

JSON is the common data format for APIs, configs, and AI payloads.

```python
import json

text = json.dumps({"name": "Ada", "age": 36})  # dict → string
data = json.loads(text)                        # string → dict

# file versions:
# json.dump(data, file)
# data = json.load(file)
```

| Function | Direction |
|----------|-----------|
| `dumps` / `loads` | Python ↔ string |
| `dump` / `load` | Python ↔ file |

### Trace

```python
person = {"name": "Ada", "skills": ["python"]}
text = json.dumps(person)
back = json.loads(text)
print(back["skills"][0])  # python
```

dict → string → dict → `"python"`

AI tip: confusing `dumps` with `dump` is one of the most common bugs.

---

## 12. `csv`

```python
import csv

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Ada", "score": "90"})

with open("scores.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], int(row["score"]))
```

CSV values arrive as **strings** — cast with `int()` / `float()` when needed.  
`newline=""` avoids blank-line issues on Windows.

---

## 13. Combining modules

```python
import statistics
import datetime
import json

scores = [80, 90, 70]
summary = {
    "mean": statistics.mean(scores),
    "generated_at": datetime.datetime.now().strftime("%Y-%m-%d"),
}
print(json.dumps(summary))
```

Real scripts mix: `os` + `json`/`csv` + `datetime` + your functions.

---

## 14. Real-world preview (still beginner level)

### Config loader

```python
import json

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
```

### Timestamped log line

```python
import datetime

def stamp(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{now}] {message}"
```

### Random practice question picker

```python
import random

def pick_question(bank):
    return random.choice(bank)
```

You are not installing FastAPI or pandas today.  
You are learning the standard-library skills those tools expect.

---

## 15. Career preview (third-party — later)

| Path | Next modules (`pip`) |
|------|----------------------|
| Backend | `requests`, FastAPI / Flask / Django |
| Data | `pandas`, `matplotlib` |
| AI/ML | `numpy`, `scikit-learn`, PyTorch |
| Automation | `requests`, scheduling libs |
| DevOps | `boto3`, cloud CLIs |

All of them assume Modules 1–9 fundamentals.

Intentionally deferred for later electives: Docker SDK, Kubernetes clients, Terraform/Jenkins APIs.

---

## 16. Common mistakes checklist

1. Forgetting to `import`  
2. Confusing `json.dumps` (string) vs `json.dump` (file)  
3. Not converting CSV strings with `int()` / `float()`  
4. Hardcoding `\` paths instead of `os.path.join`  
5. Expecting `random` to be reproducible without `seed`  
6. Using third-party imports without `pip install`  
7. Shipping AI code that imports packages you never installed  

---

## 17. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask: “Is this standard library or pip?”  
- Re-type the import and one call yourself  
- Run and verify  

---

## 18. Mini self-check (before the quiz)

Can you answer these out loud?

1. Standard library vs pip package?  
2. `dumps` vs `dump`?  
3. Why `os.path.join`?  
4. Why `random.seed`?  
5. What is `sys.argv` for?  
6. Why cast CSV values?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 19. What “confident” means after Module 9

You can:

- use built-in modules confidently  
- persist structured data with JSON/CSV  
- handle dates, randomness, and basic OS paths  
- combine modules with functions and files  
- prepare for framework/library learning without drowning in installs  

Next lesson (Module 10) covers **classes and objects** — modeling real entities with your own types.
