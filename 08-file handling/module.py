"""
================================================================================
MODULE 8 — File Handling in Python
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 7 (functions)
Next:     Module 9 (important modules)

This script creates a temporary demo folder, runs examples, then cleans up.
================================================================================
"""

import os
import shutil

print("=== Module 8: File Handling in Python ===")

# --------------------------------------------------
# 0) Setup — demo workspace (so examples stay tidy)
# --------------------------------------------------
DEMO_DIR = "_module8_demo"
if os.path.exists(DEMO_DIR):
    shutil.rmtree(DEMO_DIR)
os.makedirs(DEMO_DIR)


def demo_path(name):
    return os.path.join(DEMO_DIR, name)


# --------------------------------------------------
# 1) Write with open/close
# --------------------------------------------------
sample = demo_path("sample.txt")
file = open(sample, "w", encoding="utf-8")
file.write("Hello, this is a test file.\n")
file.close()
print("Wrote:", sample)

# --------------------------------------------------
# 2) read / readline / readlines / line loop
# --------------------------------------------------
file = open(sample, "r", encoding="utf-8")
content = file.read()
file.close()
print("read():", repr(content))

with open(sample, "w", encoding="utf-8") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

with open(sample, "r", encoding="utf-8") as file:
    first = file.readline()
    print("readline():", repr(first))

with open(sample, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("readlines():", lines)

print("for line in file:")
with open(sample, "r", encoding="utf-8") as file:
    for line in file:
        print(" ", line.strip())

# --------------------------------------------------
# 3) writelines + append
# --------------------------------------------------
output = demo_path("output.txt")
rows = ["Alpha\n", "Beta\n", "Gamma\n"]
with open(output, "w", encoding="utf-8") as file:
    file.writelines(rows)

with open(output, "a", encoding="utf-8") as file:
    file.write("Delta appended\n")

with open(output, "r", encoding="utf-8") as file:
    print("After append:\n" + file.read())

# --------------------------------------------------
# 4) with + helper functions (Module 7 combo)
# --------------------------------------------------


def save_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


note = demo_path("note.txt")
save_text(note, "Functions + files work great together.\n")
print("load_text:", load_text(note).strip())

# --------------------------------------------------
# 5) exists / exclusive create "x"
# --------------------------------------------------
print("note exists?", os.path.exists(note))

exclusive = demo_path("exclusive.txt")
with open(exclusive, "x", encoding="utf-8") as file:
    file.write("Created only because it did not exist.\n")

# Opening again with "x" would raise FileExistsError:
# with open(exclusive, "x") as file:
#     pass

# --------------------------------------------------
# 6) Binary files
# --------------------------------------------------
binary_path = demo_path("data.bin")
payload = bytes([10, 20, 30, 40, 50])
with open(binary_path, "wb") as file:
    file.write(payload)

with open(binary_path, "rb") as file:
    data = file.read()
print("Binary bytes:", data)

copy_path = demo_path("data_copy.bin")
with open(copy_path, "wb") as file:
    file.write(data)
print("Binary copy exists?", os.path.exists(copy_path))

# --------------------------------------------------
# 7) Practical: simple log file
# --------------------------------------------------
log_path = demo_path("app.log")


def log_message(message):
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")


log_message("[INFO] Backup started")
log_message("[INFO] Backup completed")
print("Log contents:")
print(load_text(log_path))

# --------------------------------------------------
# 8) Practical: CSV-like write/read
# --------------------------------------------------
csv_path = demo_path("students.csv")
with open(csv_path, "w", encoding="utf-8") as file:
    file.write("name,score\n")
    file.write("Ada,90\n")
    file.write("Bob,75\n")

records = []
with open(csv_path, "r", encoding="utf-8") as file:
    header = file.readline()  # skip header
    for line in file:
        name, score = line.strip().split(",")
        records.append({"name": name, "score": int(score)})
print("CSV records:", records)

# --------------------------------------------------
# 9) AI-era preview: save cleaned prompt + count lines
# --------------------------------------------------


def save_prompt(path, prompt):
    clean = prompt.strip()
    with open(path, "w", encoding="utf-8") as file:
        file.write(clean + "\n")


def count_lines(path):
    count = 0
    with open(path, "r", encoding="utf-8") as file:
        for _ in file:
            count += 1
    return count


prompt_path = demo_path("prompt.txt")
save_prompt(prompt_path, "  Summarize this article in 3 bullets.  ")
print("Saved prompt:", load_text(prompt_path).strip())
print("Line count sample.txt:", count_lines(sample))

# AI bug reminder: "w" vs "a"
# Using "w" on a log file would wipe history. Logs should use "a".

# --------------------------------------------------
# 10) Common mistakes (commented)
# --------------------------------------------------
# - Forgetting file.close() when not using with
# - Using "w" when you meant "a" (overwrites data!)
# - Reading a file opened with "w" only
# - Assuming file exists in "r" mode → FileNotFoundError
# - Hardcoding paths that only work on one OS
# - Not using encoding="utf-8" for text with non-ASCII

# --------------------------------------------------
# 11) Cleanup demo files
# --------------------------------------------------
shutil.rmtree(DEMO_DIR)
print("Cleaned demo folder:", DEMO_DIR)

print("\n--- Module 8 complete. Open module_exercises.md and practice. ---")
