"""
================================================================================
MODULE 11 — Exception Handling
Student lesson file (beginner, small module)
================================================================================
How to use:
  1. Read module_notes.md
  2. Run:  python module.py
  3. Change values and rerun failing cases
  4. Then open module_exercises.md

Goal: understand WHY try/except exists, not every advanced pattern.
================================================================================
"""

print("=== Module 11: Exception Handling ===")

# --------------------------------------------------
# 1) Without handling → program crashes
# --------------------------------------------------
# Uncomment to see a crash:
# print(10 / 0)

print("Demo: we will HANDLE errors instead of crashing.")

# --------------------------------------------------
# 2) Basic try / except
# --------------------------------------------------
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Caught ZeroDivisionError: cannot divide by zero.")

# --------------------------------------------------
# 3) ValueError from casting (very common)
# --------------------------------------------------
raw_age = "twenty"  # pretend this came from input()
try:
    age = int(raw_age)
    print("Age:", age)
except ValueError:
    print("Caught ValueError: age must be digits, got:", raw_age)

# Good input path
raw_age = "21"
try:
    age = int(raw_age)
    print("Valid age:", age)
except ValueError:
    print("Invalid age")

# --------------------------------------------------
# 4) except ... as e  (see the message)
# --------------------------------------------------
try:
    number = int("3.14")  # int() does not accept "3.14"
except ValueError as e:
    print("Error details:", e)

# --------------------------------------------------
# 5) FileNotFoundError
# --------------------------------------------------
try:
    with open("this_file_does_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Caught FileNotFoundError: file is missing.")

# --------------------------------------------------
# 6) else + finally (simple)
# --------------------------------------------------
try:
    value = int("42")
except ValueError:
    print("Not a number")
else:
    print("try succeeded, value =", value)
finally:
    print("finally always runs")

# --------------------------------------------------
# 7) Real-world: safe calculator helper
# --------------------------------------------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

# --------------------------------------------------
# 8) Real-world: Postgres localhost connection pattern
# --------------------------------------------------
# Common local learning credentials:
#   host=localhost  port=5432
#   user=postgres   password=postgres
#   dbname=postgres
#
# This demo does NOT require Postgres to be installed.
# It shows the SAME defensive pattern used in real apps.

print("\n--- Postgres connection demo (safe pattern) ---")

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "postgres",
    "dbname": "postgres",
}

try:
    import psycopg2  # may not be installed on every student machine
    conn = psycopg2.connect(
        host=PG_CONFIG["host"],
        port=PG_CONFIG["port"],
        user=PG_CONFIG["user"],
        password=PG_CONFIG["password"],
        dbname=PG_CONFIG["dbname"],
        connect_timeout=3,
    )
    print("Connected to Postgres on localhost:5432")
    conn.close()
except ImportError:
    print("psycopg2 not installed — that is OK for this lesson.")
    print("In a real project you would: pip install psycopg2-binary")
except Exception as e:
    # Wrong password, DB not running, etc. all land here.
    print("Could not connect to Postgres:", type(e).__name__, "-", e)

print("App continues after DB attempt (no crash).")

# --------------------------------------------------
# 9) Other important places (preview only)
# --------------------------------------------------
print("\n--- Where else exceptions matter ---")
print("Forms/API: bad JSON or missing fields")
print("Files: missing path / permission denied")
print("AI APIs: timeout, invalid key, rate limit")
print("Network: server unreachable")

# Tiny simulated "API key missing" check
api_key = None
try:
    if api_key is None:
        raise ValueError("API key is missing")
    print("Calling AI service...")
except ValueError as e:
    print("AI call blocked:", e)

print("\n--- Module 11 complete. Open module_exercises.md ---")
