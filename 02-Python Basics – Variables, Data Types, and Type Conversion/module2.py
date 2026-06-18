"""
================================================================================
MODULE 2: Python Basics - Variables, Data Types, and Type Conversion
================================================================================
Learning Goals (by the end of this module you will be able to):
  - Create variables and follow Python naming conventions
  - Identify and use int, float, str, bool, and None
  - Check types with type() and isinstance()
  - Convert between types using int(), float(), str(), and bool()
  - Fix the classic input() + math bug using type casting

Career Paths This Module Supports:
  Backend Web Dev  -> Request params, JSON fields, database values as typed data
  Data Science     -> Columns are int/float/str; cleaning requires casting
  AI / ML          -> Feature tensors need correct numeric types
  Automation       -> Config values from files/env vars are often strings first
  DevOps           -> Port numbers, flags, thresholds parsed from strings
================================================================================
"""

# =============================================================================
# 1. VARIABLES — NAMES FOR VALUES IN MEMORY
# =============================================================================
"""
A variable is a name (label) that refers to a value stored in memory.
In Python you do NOT declare the type — you assign a value and Python
figures out the type automatically (dynamic typing).

Syntax:
    variable_name = value
"""

name = "Alice"        # str  — text
age = 25              # int  — whole number
height = 5.6          # float — decimal number
is_student = True     # bool — True or False

print(name, age, height, is_student)

# Variables can be reassigned — the name can point to a new value (and new type)
score = 90
print("Before:", score, type(score))
score = 95.5          # now a float
print("After:", score, type(score))

# Multiple assignment in one line
x, y, z = 1, 2, 3
print(x, y, z)

# Swap two values (Pythonic — no temporary variable needed)
a, b = 10, 20
a, b = b, a
print("Swapped:", a, b)   # 20 10

# =============================================================================
# 2. CONSTANTS (BY CONVENTION)
# =============================================================================
"""
Python has no true "constant" keyword. By convention, ALL_CAPS names
signal "do not change this value" to other developers.

Used everywhere: API keys labels, math constants, config limits.
"""

PI = 3.14159
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_PORT = 8000

print("Pi:", PI, "| Max attempts:", MAX_LOGIN_ATTEMPTS)

# =============================================================================
# 3. VARIABLE NAMING RULES (PEP 8)
# =============================================================================
"""
Rules:
  - Start with a letter (a-z, A-Z) or underscore _
  - After that: letters, digits, underscores only
  - Case-sensitive: age and Age are different variables
  - Cannot use reserved keywords (if, while, class, import, ...)

Style guide (PEP 8): use snake_case for variables
  user_name, total_price, is_active

Valid examples:
"""
my_variable = 10
_myVar = "Python"
age_2024 = 30

# Invalid examples (commented — these would cause SyntaxError):
# 2name = "John"       # cannot start with a digit
# my-variable = 50     # hyphens not allowed (minus operator)
# if = 25             # 'if' is a reserved keyword

# =============================================================================
# 4. DYNAMIC TYPING
# =============================================================================
"""
Dynamic typing = the type is determined by the value at assignment time,
and can change when you reassign.

Compare to Java/C++ where you write:  int x = 10;  (type is fixed)
"""
dynamic = 10
print(type(dynamic))    # <class 'int'>
dynamic = "Python"
print(type(dynamic))    # <class 'str'>  — same name, different type now

# Career note: JSON from a web API arrives as strings; you cast to int/float
# when building database models or doing calculations.

# =============================================================================
# 5. BUILT-IN DATA TYPES
# =============================================================================
"""
| Type     | Description              | Example           | Common use              |
|----------|--------------------------|-------------------|-------------------------|
| int      | Whole numbers            | 10, -5, 0         | counts, IDs, ages       |
| float    | Decimal numbers          | 3.14, 2.0         | prices, scores, metrics |
| str      | Text (sequence of chars) | "Hello", 'Py'     | names, messages, JSON   |
| bool     | True or False            | True, False       | flags, conditions       |
| NoneType | Absence of a value       | None              | optional fields, defaults |
"""

age = 25
price = 19.99
message = "Hello, World!"
is_python_easy = True
nothing = None          # "no value yet" — common in APIs and databases

print(type(age))              # <class 'int'>
print(type(price))            # <class 'float'>
print(type(message))          # <class 'str'>
print(type(is_python_easy))   # <class 'bool'>
print(type(nothing))          # <class 'NoneType'>

# int can be arbitrarily large (unlike some languages with 32-bit limits)
big_number = 10 ** 20
print("Big int:", big_number)

# Float gotcha: tiny rounding errors (important in finance/data science)
print(0.1 + 0.2)   # 0.30000000000000004 — use round() or decimal module later

# =============================================================================
# 6. TYPE CHECKING — type() and isinstance()
# =============================================================================
"""
type(x)       -> returns the type object (good for learning/debugging)
isinstance(x, T) -> True/False — preferred in production code
"""

x = 42
y = "Python"
z = 3.14

print(type(x))                    # <class 'int'>
print(type(y))                    # <class 'str'>
print(isinstance(42, int))        # True
print(isinstance("Python", float))  # False
print(isinstance(3.14, (int, float)))  # True — matches int OR float

# Backend example: validate API input before saving
user_id = "101"
if isinstance(user_id, str) and user_id.isdigit():
    user_id = int(user_id)
    print("Valid user ID:", user_id)

# =============================================================================
# 7. TYPE CASTING (TYPE CONVERSION)
# =============================================================================
"""
Casting = converting a value from one type to another.

| Function  | Converts to | Example                    |
|-----------|-------------|----------------------------|
| int(x)    | Integer     | int(3.9) -> 3              |
| float(x)  | Float       | float("10") -> 10.0        |
| str(x)    | String      | str(123) -> "123"          |
| bool(x)   | Boolean     | bool(0) -> False           |
"""

num = 10
print(type(num))

num_str = str(num)
print(type(num_str), num_str)   # <class 'str'> '10'

pi = "3.14"
pi_float = float(pi)
print(type(pi_float), pi_float)  # <class 'float'> 3.14

# int() truncates decimals (does NOT round)
print(int(3.9))    # 3
print(int(-3.9))   # -3

# bool() — truthy and falsy values (critical for if-statements in Module 5)
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False  — empty string
print(bool("hello"))  # True — non-empty string
print(bool(None))    # False

# Casting can fail — produces ValueError
# int("hello")   # ValueError: invalid literal for int()
# Always validate user input in real applications.

# =============================================================================
# 8. WHY TYPE CASTING MATTERS WITH input()
# =============================================================================
"""
input() ALWAYS returns str — even when the user types digits.

Wrong (string concatenation):
    "5" + "3"  ->  "53"

Right (after casting):
    int("5") + int("3")  ->  8
"""

# Demo without input (shows the trap):
num1_str = "5"
num2_str = "3"
print("String concat:", num1_str + num2_str)       # 53
print("Integer math:", int(num1_str) + int(num2_str))  # 8

# Interactive version — uncomment to try:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum:", num1 + num2)
#
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))
# print("Total:", price * quantity)

# =============================================================================
# 9. DISPLAYING VARIABLES — f-strings (Preview)
# =============================================================================
"""
f-strings embed variables directly in text (Python 3.6+).
You'll use these in every career path.
"""
student = "Ravi"
marks = 87.5
print(f"{student} scored {marks}%")
print(f"Next year {student} will be {age + 1} years old (using age={age})")

# =============================================================================
# 10. None — THE "NO VALUE" PLACEHOLDER
# =============================================================================
"""
None means "nothing here yet" or "optional field not set".

Backend: user.middle_name = None
Data:    missing sensor reading = None
AI:      optional hyperparameter not provided = None
"""
result = None
if result is None:
    print("No result returned yet.")

# Use 'is None' / 'is not None' — not == None (PEP 8 style)

# =============================================================================
# 11. COMMON ERRORS IN THIS MODULE
# =============================================================================
"""
| Error        | Cause                              | Fix                        |
|--------------|------------------------------------|----------------------------|
| NameError    | Variable used before assignment    | Assign before use            |
| TypeError    | int + str, wrong operation         | Cast to matching type        |
| ValueError   | int("abc"), float("text")          | Validate input first         |
| SyntaxError  | Invalid variable name              | Follow naming rules          |
"""

# =============================================================================
# 12. MINI PROJECT PREVIEW
# =============================================================================
# See exercise.py — "Student Profile Builder":
#   - Store name (str), age (int), gpa (float), enrolled (bool)
#   - Cast input() values correctly
#   - Print a formatted profile with f-strings

print("\n--- Module 2 demo complete. Open exercise.py for hands-on practice. ---")
