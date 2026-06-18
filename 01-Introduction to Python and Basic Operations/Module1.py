"""
================================================================================
MODULE 1: Introduction to Python and Basic Operations
================================================================================
Learning Goals (by the end of this module you will be able to):
  - Explain what Python is and where it is used in the industry
  - Install Python and run code in the REPL and from a .py file
  - Use print() and input() for basic programs
  - Perform arithmetic operations
  - Write comments and read simple error messages

Career Paths This Module Supports:
  Backend Web Dev  -> Django/Flask APIs start with print/input & scripts
  Data Science     -> Jupyter notebooks use the same Python basics
  AI / ML          -> Every model script begins with variables and I/O
  Automation       -> Scripts that read input and print status messages
  DevOps           -> pip, virtual environments, and CLI commands
================================================================================
"""

# =============================================================================
# 1. WHAT IS PYTHON?
# =============================================================================
"""
Python is a high-level, interpreted programming language created by
Guido van Rossum (first released in 1991). "High-level" means Python handles
many low-level details (memory, compilation) for you so you focus on logic.

Key characteristics:
  - Readable syntax (looks close to plain English)
  - Interpreted (runs line by line — no separate compile step)
  - Dynamically typed (you don't declare types; Python figures them out)
  - Cross-platform (Windows, macOS, Linux)
  - Huge ecosystem (libraries for web, data, AI, automation, DevOps)

Real-world example:
  A backend developer writes:  print("Server started on port 8000")
  A data analyst writes:      print("Loaded 10,000 rows from CSV")
  Same language, different domains — fundamentals are identical.
"""

# =============================================================================
# 2. WHY PYTHON? (Features and Industry Applications)
# =============================================================================
"""
Why companies hire Python developers:
  - Fast to learn and maintain (lower cost, quicker prototypes)
  - One language for many roles (backend, data, AI, scripting)
  - Strong community and documentation

Applications by career path:
  | Path              | Tools / Frameworks        | Example Task                    |
  |-------------------|---------------------------|---------------------------------|
  | Backend Web       | Django, Flask, FastAPI    | Build REST APIs                 |
  | Data Science      | Pandas, NumPy, Matplotlib | Analyze sales data              |
  | AI / ML           | TensorFlow, PyTorch, scikit-learn | Train image classifiers |
  | Automation        | scripts, Selenium, schedule | Auto-generate reports       |
  | DevOps            | Ansible, pip, venv        | Deploy and manage servers       |

Tip: You do NOT need to pick a path now. Module 1 builds the foundation
every path shares.
"""

# =============================================================================
# 3. PYTHON 3 vs PYTHON 2 (Important for Interviews)
# =============================================================================
"""
Always use Python 3. Python 2 reached end-of-life in 2020.
On some systems the command is `python`, on others `python3`.
Check your version — it should start with 3.x:

  Windows / macOS / Linux terminal:
      python --version
      python3 --version

Expected output example:  Python 3.12.4
"""

# =============================================================================
# 4. INSTALLING PYTHON AND SETTING UP YOUR ENVIRONMENT
# =============================================================================
"""
--- Windows ---
  1. Download from https://www.python.org/downloads/
  2. Run installer — CHECK "Add Python to PATH"
  3. Open Command Prompt or PowerShell and verify:
         python --version

--- macOS ---
  python3 --version
  If missing:  brew install python

--- Linux (Ubuntu/Debian) ---
  python3 --version
  If missing:  sudo apt install python3 python3-pip python3-venv

--- Recommended Editor / IDE ---
  - VS Code (free) + Python extension  ← great for beginners
  - PyCharm Community (free)
  - Cursor (AI-assisted coding)

--- pip (Package Installer) ---
  pip installs third-party libraries (Django, Pandas, etc.):
      pip --version
      pip install requests

--- Virtual Environment (brief preview — used in every professional project) ---
  Keeps project dependencies isolated (critical for DevOps & backend teams):
      python -m venv myenv
      # Windows:   myenv\\Scripts\\activate
      # macOS/Linux: source myenv/bin/activate

You will use venv in depth later; for now, know it exists.
"""

# =============================================================================
# 5. TWO WAYS TO RUN PYTHON CODE
# =============================================================================
"""
A) Interactive Mode (REPL — Read-Eval-Print Loop)
   Open terminal, type:  python   (or python3)
   You see >>> prompt. Type one line, press Enter, see result immediately.
   Great for quick experiments.

B) Script Mode (how real projects work)
   Save code in a file, e.g. hello.py, then run:
       python hello.py
   The entire file executes top to bottom.
"""

# --- Script Mode Example: Your First Python Program ---
print("Hello, World!")

# =============================================================================
# 6. COMMENTS — DOCUMENTING YOUR CODE
# =============================================================================
# This is a single-line comment. Python ignores it. Use comments to explain WHY.

"""
This is a multi-line string (docstring).
Often used at the top of a file or function to describe purpose.
It does NOT run as code when written at module level in some contexts,
but triple quotes are the standard for documentation.
"""

name = "Sara"  # inline comment — explains this variable

# =============================================================================
# 7. BASIC ARITHMETIC OPERATIONS
# =============================================================================
# Numbers are building blocks for data science, games, finance, and APIs.

a = 10
b = 5

print("Addition:       ", a + b)   # 15
print("Subtraction:    ", a - b)   # 5
print("Multiplication: ", a * b)   # 50
print("Division:       ", a / b)   # 2.0  (always returns float in Python 3)
print("Floor Division: ", a // b)  # 2    (drops decimal part)
print("Modulus:        ", a % b)   # 0    (remainder — used for even/odd checks)
print("Exponent:       ", a ** b)  # 100000  (10 to the power 5)

# Real-world: modulus (%) checks if a number is divisible
# DevOps example: if disk_usage % 10 == 0: alert every 10% threshold

# =============================================================================
# 8. THE print() FUNCTION — DISPLAYING OUTPUT
# =============================================================================
print("Welcome to Python!")
print("My name is John.")
print("The sum of 5 and 3 is:", 5 + 3)

# sep — separator between multiple values (default is a space)
print("2024", "06", "18", sep="-")   # Output: 2024-06-18

# end — what to print at the end (default is newline \n)
print("Loading", end="...")
print(" Done!")   # Output: Loading... Done!

# print() can show multiple types at once
print("Score:", 95, "Grade:", "A")

# =============================================================================
# 9. THE input() FUNCTION — TAKING USER INPUT
# =============================================================================
# input() ALWAYS returns a STRING, even if the user types digits.
# You will learn type conversion (int, float) in Module 2.

# Uncomment the lines below to try interactively (or run in REPL):
# name = input("Enter your name: ")
# print("Hello, " + name + "! Welcome to Python.")

# String concatenation with + only works when both sides are strings:
# print("Hello, " + name)  # OK if name is str
# print("Age: " + 25)      # ERROR — cannot add str and int

# =============================================================================
# 10. EXAMPLE: SIMPLE INTERACTIVE PROGRAM
# =============================================================================
# A mini calculator — combines input(), type conversion, and print()

# Uncomment to run interactively:
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
#
# num1 = int(num1)   # convert string -> integer (Module 2 covers this in depth)
# num2 = int(num2)
#
# print("Sum:", num1 + num2)

# Why int()?  input("5") returns "5" (string).  "5" + "3" = "53" (wrong!)
#             int("5") + int("3") = 8 (correct!)

# =============================================================================
# 11. INDENTATION PREVIEW (Critical for All Future Modules)
# =============================================================================
# Python uses indentation (spaces) to define code blocks — not curly braces {}.
# Standard is 4 spaces. Wrong indentation causes IndentationError.

if True:
    print("This line is indented - it belongs to the if block.")
print("This line is NOT indented — it always runs.")

# =============================================================================
# 12. READING ERROR MESSAGES (Beginner Debugging)
# =============================================================================
"""
When something goes wrong, Python shows a traceback. Example:

  SyntaxError: invalid syntax
      -> You made a typo or forgot a colon/parenthesis

  NameError: name 'x' is not defined
      -> You used a variable before creating it

  TypeError: unsupported operand type(s) for +: 'int' and 'str'
      -> You mixed incompatible types (e.g. 5 + "hello")

Read the LAST line of the error first — it usually tells you the problem.
"""

# =============================================================================
# 13. MINI PROJECT IDEA — PUT IT ALL TOGETHER
# =============================================================================
# Build a "Personal Introduction Card" (see exercise.py for full assignment):
#
#   1. Ask for name, city, and favorite technology
#   2. Print a formatted welcome message
#   3. Ask for two numbers and print sum, difference, product, quotient
#
# This mirrors what backend APIs do: receive input -> process -> return output.

print("\n--- Module 1 demo complete. Open exercise.py for hands-on practice. ---")
