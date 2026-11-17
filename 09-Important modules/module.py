"""
================================================================================
MODULE 9 — Important Modules
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 8 (file handling)
Next:     Module 10 (classes and objects)

Focus: Python STANDARD LIBRARY only (no pip installs required).
Creates a temporary demo folder, then cleans it up.
================================================================================
"""

import os
import sys
import math
import random
import json
import csv
import datetime
import time
import statistics
import shutil

print("=== Module 9: Important Modules ===")

# --------------------------------------------------
# 1) math
# --------------------------------------------------
print("pi:", math.pi)
print("sqrt(16):", math.sqrt(16))
print("ceil(3.2):", math.ceil(3.2))
print("floor(3.8):", math.floor(3.8))
print("pow(2, 5):", math.pow(2, 5))
print("factorial(5):", math.factorial(5))

from math import sqrt as square_root
print("alias sqrt:", square_root(49))

# --------------------------------------------------
# 2) random
# --------------------------------------------------
random.seed(42)  # reproducible demos/tests
print("randint 1..6:", random.randint(1, 6))
print("choice:", random.choice(["red", "green", "blue"]))
print("sample:", random.sample(range(1, 11), 3))
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("shuffled:", nums)

# --------------------------------------------------
# 3) datetime & time
# --------------------------------------------------
now = datetime.datetime.now()
print("now:", now)
print("today:", datetime.date.today())
print("formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

parsed = datetime.datetime.strptime("2026-07-23", "%Y-%m-%d")
print("parsed:", parsed.date())

start = time.time()
time.sleep(0.05)
elapsed = time.time() - start
print("slept about:", round(elapsed, 2), "seconds")

# --------------------------------------------------
# 4) statistics
# --------------------------------------------------
scores = [90, 75, 88, 92, 70]
print("mean:", statistics.mean(scores))
print("median:", statistics.median(scores))

# --------------------------------------------------
# 5) os / os.path (extends Module 8)
# --------------------------------------------------
print("cwd:", os.getcwd())
print("os.name:", os.name)

DEMO = "_module9_demo"
if os.path.exists(DEMO):
    shutil.rmtree(DEMO)
os.makedirs(DEMO)

demo_file = os.path.join(DEMO, "hello.txt")
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("hello modules\n")

print("listdir:", os.listdir(DEMO))
print("exists hello?", os.path.exists(demo_file))
print("isfile?", os.path.isfile(demo_file))
print("isdir demo?", os.path.isdir(DEMO))
print("join example:", os.path.join("data", "input", "file.csv"))

os.environ["COURSE_NAME"] = "PythonFundamentals"
print("COURSE_NAME:", os.environ.get("COURSE_NAME"))
print("Missing env:", os.environ.get("NOT_SET", "default"))

# --------------------------------------------------
# 6) sys
# --------------------------------------------------
print("python version:", sys.version.split()[0])
print("platform:", sys.platform)
print("argv:", sys.argv)

# --------------------------------------------------
# 7) json (critical for APIs / config / AI payloads)
# --------------------------------------------------
person = {"name": "Ada", "age": 36, "skills": ["python", "math"]}
json_text = json.dumps(person)
print("dumps:", json_text)

back = json.loads(json_text)
print("loads name:", back["name"])
print("skills[0]:", back["skills"][0])

json_path = os.path.join(DEMO, "person.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("loaded from file:", loaded)

# --------------------------------------------------
# 8) csv
# --------------------------------------------------
csv_path = os.path.join(DEMO, "scores.csv")
rows = [
    {"name": "Ada", "score": "90"},
    {"name": "Bob", "score": "75"},
]

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("csv row:", row["name"], int(row["score"]))

# --------------------------------------------------
# 9) Combined helpers (functions + modules)
# --------------------------------------------------


def random_team(names, size):
    """Return a random sample of names."""
    return random.sample(names, size)


def summarize_scores(values):
    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "max": max(values),
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d"),
    }


def stamp(message):
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{now_str}] {message}"


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


team = random_team(["Ada", "Bob", "Cam", "Dee", "Eve"], 3)
summary = summarize_scores([80, 90, 70, 100])
print("team:", team)
print("summary json:", json.dumps(summary))
print(stamp("Backup completed"))
print("config name:", load_config(json_path)["name"])

# --------------------------------------------------
# 10) Career preview (do NOT require installs here)
# --------------------------------------------------
# After fundamentals, common third-party modules include:
#   requests      -> HTTP APIs
#   pandas/numpy  -> data / AI arrays
#   fastapi/flask -> web backends
#   boto3         -> cloud automation
# Install later with:  pip install requests
# They build on: functions, dicts/lists, json, files, os.

# Common AI bug: importing requests/pandas without installing them.

# --------------------------------------------------
# 11) Cleanup
# --------------------------------------------------
shutil.rmtree(DEMO)
print("cleaned:", DEMO)

print("\n--- Module 9 complete. Open module_exercises.md and practice. ---")
