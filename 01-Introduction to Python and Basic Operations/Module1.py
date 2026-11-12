"""
================================================================================
MODULE 1 — INTRODUCTION TO PYTHON AND BASIC OPERATIONS (Reference)
================================================================================
Run:  python module.py

AI-Era Track goals:
  - Master the absolute fundamentals
  - See where each idea appears in FastAPI / AI / automation (preview only)
  - Practice TRACE -> PREDICT -> VERIFY (how you evaluate AI-generated code)

Prerequisites: None
Next: Module 2 — Variables, Data Types, Type Conversion
================================================================================
"""

print("=== Module 1: Introduction to Python (AI-Era Track) ===")

# ==================================================
# 1. WHY PYTHON IN THE AI ERA?
# ==================================================
# Python is the shared language of:
#   - Backend APIs (FastAPI, Django)
#   - AI / LLM apps (PyTorch, LangChain, OpenAI SDK)
#   - Data (Pandas) and Automation / DevOps scripts
#
# Vibe coding helps you draft faster.
# Fundamentals help you VERIFY and fix what AI writes.
# Interviews test understanding, not prompt typing.

# ==================================================
# 2. HELLO WORLD — YOUR FIRST OUTPUT CHANNEL
# ==================================================
# print() sends information to the terminal.
# Later cousins: logging, API responses, model status messages.

print("Hello, World!")
print("[INFO] app starting")          # looks like a backend log line
print("[INFO] model warmup: ok")      # looks like an AI script log line

# ==================================================
# 3. COMMENTS — UNDERSTAND BEFORE YOU SHIP
# ==================================================
# Use comments for WHY.
# AI-era rule: never ship code you cannot explain.

# This script demonstrates Module 1 fundamentals for beginners.
course_name = "Python Fundamentals"  # shown to students on day 1
print("Course:", course_name)

# ==================================================
# 4. print() DETAILS — DEBUGGING SUPERPOWER
# ==================================================
print("Score:", 95, "Grade:", "A")
print("2026", "07", "23", sep="-")    # 2026-07-23

print("Loading", end="...")
print(" Done!")                       # Loading... Done!

# FastAPI / AI debugging PREVIEW (same skill, richer tools later):
request_path = "/users"
tokens_used = 120
print("[DEBUG] path:", request_path)
print("[DEBUG] tokens_used:", tokens_used)

# ==================================================
# 5. ARITHMETIC — METRICS, BATCHES, COSTS
# ==================================================
price = 10
quantity = 3

print("total:", price * quantity)     # billing-style calculation
print("division:", 10 / 4)            # 2.5  (float in Python 3)
print("floor:", 10 // 4)              # 2
print("remainder:", 10 % 4)           # 2
print("power:", 2 ** 8)               # 256

# Batching pattern (AI training / API uploads / job queues)
items = 17
batch_size = 5
full_batches = items // batch_size
leftover = items % batch_size
print("full_batches:", full_batches, "| leftover:", leftover)

# Token-cost style estimate (concept numbers only)
tokens = 1500
price_per_token = 0.000002
estimated_cost = tokens * price_per_token
print("estimated_cost:", estimated_cost)

# Pagination-style math (APIs)
page = 3
page_size = 20
offset = (page - 1) * page_size
print("sql_offset_style:", offset)

# ==================================================
# 6. input() — RECEIVE DATA (ALWAYS str)
# ==================================================
# Today: keyboard input
# Later: FastAPI request fields, CLI args, chat prompts — same idea:
#        receive text -> convert/validate -> process -> respond

# Non-interactive demos (so this file runs without blocking):
typed_name = "Ada"
typed_a = "5"
typed_b = "3"

print("Hello,", typed_name)

# THE classic trap
print("string concat:", typed_a + typed_b)          # 53
print("numeric sum:", int(typed_a) + int(typed_b))  # 8  (casting preview; Module 2)

# Interactive versions (uncomment in lab):
# name = input("Enter name: ")
# print("Hello,", name)
# a = int(input("First number: "))
# b = int(input("Second number: "))
# print("Sum:", a + b)

# ==================================================
# 7. RECEIVE -> PROCESS -> RESPOND (API SHAPE)
# ==================================================
# This is the skeleton of almost every backend handler / AI call.

user_name = "Sam"
status = "ok"
print("status:", status)
print("message: welcome", user_name)

# Conceptual FastAPI cousin (DO NOT need to write FastAPI yet):
# @app.get("/welcome")
# def welcome(name: str):
#     return {"status": "ok", "message": f"welcome {name}"}

# ==================================================
# 8. INDENTATION PREVIEW
# ==================================================
# AI tools sometimes break indentation. You must notice.

if True:
    print("inside block")
print("outside block")

# ==================================================
# 9. ERROR LITERACY (BEGINNER DEBUGGING)
# ==================================================
# Common errors you will see (including in AI-generated drafts):
#   SyntaxError      -> missing : or )
#   NameError        -> used a name before creating it
#   TypeError        -> e.g. 5 + "3"
#   IndentationError -> bad spaces
#
# Method: read the LAST line of the traceback first.

# Demonstrations kept commented so the file runs cleanly:
# print(unknown_variable)   # NameError
# print(5 + "3")            # TypeError

# ==================================================
# 10. VERIFY WORKFLOW DEMO
# ==================================================
# Goal: compute leftover items after packing boxes of 4.
total_items = 23
box_size = 4
# Predict first: 23 // 4 = 5, 23 % 4 = 3
print("packed:", total_items // box_size)
print("left:", total_items % box_size)

print("\n--- Module 1 complete. Do module_exercises.md next. ---")
