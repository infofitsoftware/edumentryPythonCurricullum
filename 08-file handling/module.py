"""
================================================================================
MODULE 8 — FILE HANDLING IN PYTHON (Reference Program)
================================================================================
Run:  python module.py

Prerequisites: Modules 1-7 (types, strings, control flow, collections, functions)

This script creates a temporary demo folder, runs examples, then cleans up.
This file is a REFERENCE — not an assignment.
================================================================================
"""

import os
import shutil

print("=== Module 8: File Handling ===")

# ==================================================
# 0. SETUP — demo workspace
# ==================================================
DEMO_DIR = "_module8_demo"
if os.path.exists(DEMO_DIR):
    shutil.rmtree(DEMO_DIR)
os.makedirs(DEMO_DIR)


def demo_path(name):
    return os.path.join(DEMO_DIR, name)


# ==================================================
# 1. WHY FILE HANDLING?
# ==================================================
# Programs need lasting data: logs, configs, reports, CSVs, images.
# Files survive after the program ends (unlike variables in memory).

# ==================================================
# 2. FILE MODES
# ==================================================
# "r"  read (file must exist)
# "w"  write (create/overwrite)
# "a"  append (create if missing, add at end)
# "x"  exclusive create (fail if exists)
# "rb"/"wb"/"ab" binary versions
# Optional: "t" text (default), "+" update (r+/w+/a+)

# ==================================================
# 3. WRITE WITH open/close
# ==================================================
sample = demo_path("sample.txt")
file = open(sample, "w", encoding="utf-8")
file.write("Hello, this is a test file.\n")
file.close()
print("Wrote:", sample)

# ==================================================
# 4. READ — read(), readline(), readlines()
# ==================================================
file = open(sample, "r", encoding="utf-8")
content = file.read()
file.close()
print("read():", repr(content))

# Add more lines for readline demos
with open(sample, "w", encoding="utf-8") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

with open(sample, "r", encoding="utf-8") as file:
    first = file.readline()
    print("readline():", repr(first))

with open(sample, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("readlines():", lines)

# Iterate line by line (memory friendly for large files)
print("for line in file:")
with open(sample, "r", encoding="utf-8") as file:
    for line in file:
        print(" ", line.strip())

# ==================================================
# 5. writelines()
# ==================================================
output = demo_path("output.txt")
rows = ["Alpha\n", "Beta\n", "Gamma\n"]
with open(output, "w", encoding="utf-8") as file:
    file.writelines(rows)

# ==================================================
# 6. APPEND MODE
# ==================================================
with open(output, "a", encoding="utf-8") as file:
    file.write("Delta appended\n")

with open(output, "r", encoding="utf-8") as file:
    print("After append:\n" + file.read())

# ==================================================
# 7. with STATEMENT (PREFERRED)
# ==================================================
# Automatically closes the file, even if an error occurs.


def save_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


note = demo_path("note.txt")
save_text(note, "Functions + files work great together.\n")
print("load_text:", load_text(note).strip())

# ==================================================
# 8. EXISTS / DELETE (os)
# ==================================================
print("note exists?", os.path.exists(note))

# ==================================================
# 9. "x" MODE — exclusive create
# ==================================================
exclusive = demo_path("exclusive.txt")
with open(exclusive, "x", encoding="utf-8") as file:
    file.write("Created only because it did not exist.\n")

# Opening again with "x" would raise FileExistsError:
# with open(exclusive, "x") as file:
#     pass

# ==================================================
# 10. BINARY FILES (no image dependency)
# ==================================================
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

# ==================================================
# 11. PRACTICAL: SIMPLE LOG FILE
# ==================================================
log_path = demo_path("app.log")


def log_message(message):
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")


log_message("[INFO] Backup started")
log_message("[INFO] Backup completed")
print("Log contents:")
print(load_text(log_path))

# ==================================================
# 12. PRACTICAL: CSV-LIKE WRITE/READ
# ==================================================
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

# ==================================================
# 13. COMMON MISTAKES (commented)
# ==================================================
# - Forgetting file.close() when not using with
# - Using "w" when you meant "a" (overwrites data!)
# - Reading a file opened with "w" only
# - Assuming file exists in "r" mode → FileNotFoundError
# - Hardcoding paths that only work on one OS
# - Not using encoding="utf-8" for text with non-ASCII

# ==================================================
# 14. CLEANUP DEMO FILES
# ==================================================
shutil.rmtree(DEMO_DIR)
print("Cleaned demo folder:", DEMO_DIR)

print("\n--- Module 8 file handling reference complete ---")
