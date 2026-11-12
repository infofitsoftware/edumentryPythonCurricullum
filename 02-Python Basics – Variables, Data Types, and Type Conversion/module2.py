"""
================================================================================
MODULE 2 — Variables, Data Types, and Type Conversion
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module2.py
  3. Change values and rerun
  4. Then open exercise.py

Previous: Module 1 (print, input, arithmetic)
Next:     Module 3 (strings)
================================================================================
"""

print("=== Module 2: Variables, Data Types, Type Conversion ===")

# --------------------------------------------------
# 1) Variables = labeled boxes for values
# --------------------------------------------------
name = "Alice"         # text  -> str
age = 25               # whole number -> int
height = 5.6           # decimal -> float
is_student = True      # yes/no -> bool

print("Profile:", name, age, height, is_student)

# A variable can be changed later
score = 90
print("score before:", score, type(score))
score = 95.5
print("score after:", score, type(score))

# Multiple assignment and swap
x, y, z = 1, 2, 3
print("x y z:", x, y, z)

a, b = 10, 20
a, b = b, a
print("swapped:", a, b)

# --------------------------------------------------
# 2) Naming style (professional habit)
# --------------------------------------------------
user_name = "Sara"
total_price = 499.5
is_active = True
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_PORT = 8000

print(user_name, total_price, is_active, MAX_LOGIN_ATTEMPTS, DEFAULT_PORT)

# Invalid names (keep commented — they crash the file):
# 2user = "x"
# my-name = "x"
# if = 1

# --------------------------------------------------
# 3) The five core types
# --------------------------------------------------
user_id = 101                 # int
rating = 4.8                  # float
message = "order created"     # str
payment_done = False          # bool
middle_name = None            # None = missing value

print(type(user_id))
print(type(rating))
print(type(message))
print(type(payment_done))
print(type(middle_name))

print("float surprise:", 0.1 + 0.2)

# --------------------------------------------------
# 4) Checking types
# --------------------------------------------------
print("isinstance 42 int?", isinstance(42, int))
print("isinstance '42' int?", isinstance("42", int))
print("3.14 int or float?", isinstance(3.14, (int, float)))

# --------------------------------------------------
# 5) Casting (type conversion)
# --------------------------------------------------
print(int("42"))
print(float("3.14"))
print(str(100))
print(int(3.9))          # truncates -> 3
print(bool(0), bool(1))
print(bool(""), bool("hi"))
print(bool(None))

# Dangerous surprise for beginners:
print('bool("false") =>', bool("false"))  # True (!), because string is not empty

# Correct way to parse a text flag (config / JSON-like values):
flag_text = "true"
is_debug = flag_text.lower() == "true"
print("is_debug:", is_debug)

# This would crash (keep commented):
# print(int("10.5"))
print("float then int:", int(float("10.5")))

# --------------------------------------------------
# 6) input() always returns str  (Module 1 trap, fixed here)
# --------------------------------------------------
# Non-interactive demo so this file runs without waiting:
raw_a = "5"
raw_b = "3"
print("wrong concat:", raw_a + raw_b)                 # 53
print("correct sum:", int(raw_a) + int(raw_b))        # 8

# Try these in terminal during practice:
# n1 = int(input("First number: "))
# n2 = int(input("Second number: "))
# print("Sum:", n1 + n2)
# price = float(input("Price: "))
# qty = int(input("Qty: "))
# print("Total:", price * qty)

# --------------------------------------------------
# 7) Real-world preview: JSON-like request fields
# --------------------------------------------------
# Imagine an API/AI tool sent this data as text fields:
request_data = {
    "name": "Ada",
    "age": "25",          # still text!
    "temperature": "0.7", # AI model setting as text
    "active": "true",
}

# Convert before using in logic:
age_number = int(request_data["age"])
temperature = float(request_data["temperature"])
active = request_data["active"].lower() == "true"

print("validated age:", age_number, type(age_number))
print("validated temperature:", temperature, type(temperature))
print("validated active:", active, type(active))

# FastAPI cousin (read only — you will write this much later):
# age: int
# temperature: float
# The framework helps, but YOU must still understand casting.

# --------------------------------------------------
# 8) AI-generated bug hunt (common mistake)
# --------------------------------------------------
# Bad AI draft idea:
# age = input("Age: ")
# print("Next year:", age + 1)   # TypeError
#
# Fixed idea:
# age = int(input("Age: "))
# print("Next year:", age + 1)

demo_age = "20"
print("Next year:", int(demo_age) + 1)

# --------------------------------------------------
# 9) f-strings for clear output
# --------------------------------------------------
student = "Ravi"
marks = 87.5
print(f"{student} scored {marks}%")
print(f"Bill total: {19.99 * 2:.2f}")
print(f"Employee: EMP-{42:05d}")

# --------------------------------------------------
# 10) None means missing
# --------------------------------------------------
email = None
if email is None:
    print("Email not provided")

# --------------------------------------------------
# 11) Tiny end-to-end example
# --------------------------------------------------
product = "Mouse"
unit_price = float("499.5")
quantity = int("2")
in_stock = True
print(f"{product} | qty={quantity} | total={unit_price * quantity:.2f} | stock={in_stock}")

print("\n--- Module 2 complete. Open exercise.py and practice. ---")
