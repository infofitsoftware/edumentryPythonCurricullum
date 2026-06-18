"""
================================================================================
MODULE 1 — EXERCISES: Introduction to Python and Basic Operations
================================================================================
Instructions:
  - Complete each section in order.
  - Write your code below each "# YOUR CODE HERE" marker.
  - Run this file:  python exercise.py
  - For input()-based tasks, test in terminal (not all IDEs pass stdin well).

Difficulty:  [E] Easy   [M] Medium   [C] Challenge
================================================================================
"""

# =============================================================================
# SECTION A — SETUP & VERIFICATION  [E]
# =============================================================================

# A1. Verify Python is installed.
#     Open terminal and run:  python --version   (or python3 --version)
#     Write the version you see as a comment below:
#     # My Python version: _______________


# A2. Create a file named hello.py with exactly one line:
#         print("Python is installed successfully!")
#     Run it from terminal:  python hello.py
#     Paste the output as a comment:
#     # Output: _______________


# =============================================================================
# SECTION B — print() PRACTICE  [E]
# =============================================================================

# B1. Print your full name on one line.
# YOUR CODE HERE


# B2. Print three facts about Python on three separate lines using ONE print()
#     call with sep="\n" (newline separator).
# YOUR CODE HERE


# B3. Print "Loading data..." on the same line as "Complete!" using end=
#     Expected output:  Loading data...Complete!
# YOUR CODE HERE


# B4. Print your name and favorite programming language using comma separation
#     (not string concatenation).
#     Example format:  My name is Alice and my favorite language is Python
# YOUR CODE HERE


# =============================================================================
# SECTION C — ARITHMETIC OPERATIONS  [E]
# =============================================================================

# C1. Create variables x = 17 and y = 4. Print all seven operations:
#     +, -, *, /, //, %, **
#     Label each result clearly.
# YOUR CODE HERE


# C2. [M] A store sells items for ₹250 each. A customer buys 7 items and
#     gets ₹100 off. Calculate and print the final bill using variables.
# YOUR CODE HERE


# C3. [M] A DevOps script monitors disk usage: total = 500 GB, used = 347 GB.
#     Print used, free, and usage percentage (round to 2 decimal places).
#     Hint: percentage = (used / total) * 100
# YOUR CODE HERE


# =============================================================================
# SECTION D — input() & INTERACTIVE PROGRAMS  [M]
# =============================================================================

# D1. Ask the user for their name and print:  Hello, <name>! Welcome to Python.
# YOUR CODE HERE


# D2. Ask for two numbers, convert with int(), print sum, difference,
#     product, and quotient (use / for division).
# YOUR CODE HERE


# D3. Ask for the user's age (integer). Print how old they will be in 5 years.
# YOUR CODE HERE


# D4. [M] Simple currency converter: ask for an amount in USD, multiply by 83.5
#     (example rate), print the amount in INR with a clear label.
# YOUR CODE HERE


# =============================================================================
# SECTION E — COMMENTS & CODE QUALITY  [E]
# =============================================================================

# E1. Write a short program (3-5 lines) that prints a tip about Python.
#     Include at least one single-line comment (#) explaining what the code does.
# YOUR CODE HERE


# E2. [M] Fix the buggy code below (uncomment and correct):
# broken_name = input("Enter name: ")
# print("Hello " + broken_name + " you are " + 25 + " years old")
# Hint: input returns str; 25 must be converted or use commas in print.


# =============================================================================
# SECTION F — CAREER-CONNECTED MINI PROJECTS  [M] / [C]
# =============================================================================

# F1. [M] PERSONAL INTRODUCTION CARD (Backend / General)
#     Ask for: name, city, dream job (e.g. "AI Developer")
#     Print a bordered card like:
#     -------------------------
#     Name: ...
#     City: ...
#     Goal: ...
#     -------------------------
# YOUR CODE HERE


# F2. [M] DATA SNAPSHOT (Data Science preview)
#     Given (or hard-code) values: students=45, avg_score=78.5, pass_rate=0.92
#     Print a one-line dashboard:  Students: 45 | Avg: 78.5 | Pass rate: 92%
#     Use variables and print with sep.
# YOUR CODE HERE


# F3. [C] AUTOMATION LOG SIMULATOR (Automation / DevOps preview)
#     Print three timestamp-style log lines for a backup script:
#       [INFO] Backup started
#       [INFO] 150 files copied
#       [INFO] Backup completed
#     Use variables for file_count and a final success message with end=.
# YOUR CODE HERE


# F4. [C] SIMPLE RECEIPT GENERATOR
#     Ask for item name, quantity, and price per item.
#     Print item line, subtotal, 18% tax, and grand total.
#     Use float() for prices. Format output neatly.
# YOUR CODE HERE


# =============================================================================
# SECTION G — REFLECTION (Written answers — add as comments)
# =============================================================================

# G1. List three key features of Python and why they matter for beginners.
# Answer:


# G2. How is Python used in backend development vs data science?
#     (Write 2-3 sentences each.)
# Answer:


# G3. Why does input() require int() or float() before doing math?
# Answer:


# G4. What is the difference between / and // in Python?
# Answer:


# =============================================================================
# BONUS CHALLENGES (Optional)
# =============================================================================

# BONUS 1. [C] Ask for radius of a circle, print area and circumference.
#          Use 3.14159 for pi.  area = pi * r**2,  circumference = 2 * pi * r


# BONUS 2. [C] Convert seconds (input) to hours, minutes, seconds.
#          Example: 3661 -> 1 hour, 1 minute, 1 second


# BONUS 3. [C] Print your initials in ASCII art using multiple print() calls.
