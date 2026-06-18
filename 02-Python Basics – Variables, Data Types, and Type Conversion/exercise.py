"""
================================================================================
MODULE 2 — EXERCISES: Variables, Data Types, and Type Conversion
================================================================================
Instructions:
  - Complete each section in order.
  - Write your code below each "# YOUR CODE HERE" marker.
  - Run:  python exercise.py
  - Sections D onward use input() — test in terminal.

Difficulty:  [E] Easy   [M] Medium   [C] Challenge
================================================================================
"""

# =============================================================================
# SECTION A — VARIABLES & NAMING  [E]
# =============================================================================

# A1. Create four variables: your name (str), age (int), height in meters (float),
#     and whether you are learning Python (bool). Print all four on one line.
# YOUR CODE HERE


# A2. Create two constants using ALL_CAPS: COURSE_NAME and MAX_SCORE.
#     Print them with a short label.
# YOUR CODE HERE


# A3. [M] Swap two variables a = 100 and b = 200 WITHOUT a third variable.
#     Print before and after swapping.
# YOUR CODE HERE


# A4. [M] Use multiple assignment to set red, green, blue = 255, 128, 0
#     and print:  RGB(255, 128, 0)
# YOUR CODE HERE


# =============================================================================
# SECTION B — DATA TYPES & type()  [E]
# =============================================================================

# B1. Create one variable of each type: int, float, str, bool, None.
#     Print each value AND its type using type().
# YOUR CODE HERE


# B2. [M] Dynamic typing demo: assign x = 42, print type(x).
#     Reassign x = "forty-two", print type(x) again.
# YOUR CODE HERE


# B3. [M] Predict then verify: what is type(3.0)? What is type(3)?
#     Print both results.
# YOUR CODE HERE


# B4. [E] Use isinstance() to check:
#     - Is 99 an int?
#     - Is "99" an int?
#     - Is 3.14 either int or float?  (use tuple: (int, float))
# YOUR CODE HERE


# =============================================================================
# SECTION C — TYPE CASTING  [E] / [M]
# =============================================================================

# C1. Convert integer 100 to string and print type(result).
# YOUR CODE HERE


# C2. Convert string "3.14" to float and print the value.
# YOUR CODE HERE


# C3. What does int(7.8) return? Print it. What does int(-7.8) return? Print it.
# YOUR CODE HERE


# C4. [M] Truthy/falsy: print bool() of each:
#     0, 1, "", "hello", None, 42
# YOUR CODE HERE


# C5. [M] Fix this code so it prints 15 (not "153"):
broken_a = "10"
broken_b = "5"
# print(broken_a + broken_b)  # wrong
# YOUR CODE HERE (cast and add as integers)


# C6. [C] Ask: why does int("10.5") fail but float("10.5") works?
#     Write your answer as a comment, then demonstrate with code.
# Answer:


# =============================================================================
# SECTION D — input() + TYPE CONVERSION  [M]
# =============================================================================

# D1. Ask for name (str) and age (int). Print:
#     Hello, <name>! You are <age> years old.
# YOUR CODE HERE


# D2. Ask for two integers. Print sum, difference, product, quotient.
# YOUR CODE HERE


# D3. Ask for price (float) and quantity (int). Print total bill.
# YOUR CODE HERE


# D4. Ask for a decimal number (e.g. 9.7). Store as float, convert to int,
#     print both:  Original: 9.7  As integer: 9
# YOUR CODE HERE


# D5. [M] Ask for temperature in Celsius (float). Convert to Fahrenheit:
#     F = C * 9/5 + 32   Print with one decimal using round(F, 1).
# YOUR CODE HERE


# =============================================================================
# SECTION E — f-strings & FORMATTING  [M]
# =============================================================================

# E1. Given: product = "Laptop", price = 45999.50, in_stock = True
#     Print using an f-string:
#     Laptop | Price: Rs.45999.5 | In stock: True
# YOUR CODE HERE


# E2. [M] BMI calculator: weight_kg and height_m as floats (hard-code or input).
#     BMI = weight / (height ** 2)
#     Print:  Your BMI is 22.86 (round to 2 decimals).
# YOUR CODE HERE


# =============================================================================
# SECTION F — None & OPTIONAL VALUES  [M]
# =============================================================================

# F1. Create middle_name = None and full_name built from first + last only.
#     If middle_name is None, print two-part name; else print three-part.
#     Demo both cases with comments explaining.
# YOUR CODE HERE


# F2. [M] Simulate API response: email = None
#     If email is None, print "Email not provided".
#     Else print the email. Use:  if email is None:
# YOUR CODE HERE


# =============================================================================
# SECTION G — CAREER-CONNECTED MINI PROJECTS  [M] / [C]
# =============================================================================

# G1. [M] STUDENT PROFILE BUILDER (Backend / Data)
#     Ask for: name, age, gpa (float), enrolled ("yes"/"no" -> bool)
#     Print a profile card using f-strings:
#     ==============================
#     Name: ...
#     Age: ...
#     GPA: ...
#     Enrolled: True/False
#     ==============================
# YOUR CODE HERE


# G2. [M] DATA CLEANING PREVIEW (Data Science)
#     Given dirty string values in a list (hard-code):
#     raw_scores = ["85", "92", "N/A", "78", "88"]
#     Convert valid entries to int, skip "N/A" (treat as None).
#     Print the cleaned list and the average of valid scores.
# YOUR CODE HERE


# G3. [M] CONFIG PARSER (DevOps / Automation)
#     Given string env-style values (hard-code):
#     PORT = "8080"
#     DEBUG = "true"
#     TIMEOUT = "30.5"
#     Cast to int, bool, float respectively and print typed values + types.
#     Hint: bool("true") is True (non-empty string!) — for real apps you'd
#     compare DEBUG.lower() == "true". Demonstrate the correct approach.
# YOUR CODE HERE


# G4. [C] SIMPLE INVOICE WITH VALIDATION
#     Ask for item name, unit price (float), quantity (int).
#     If quantity <= 0 or price < 0, print "Invalid input" and stop.
#     Else print line total, 18% GST, grand total (all rounded to 2 decimals).
# YOUR CODE HERE


# =============================================================================
# SECTION H — REFLECTION (Written answers as comments)
# =============================================================================

# H1. What is dynamic typing? How is it different from languages like Java?
# Answer:


# H2. Why does input() always require casting for numeric calculations?
# Answer:


# H3. When would you use None in a backend API or database model?
# Answer:


# H4. What is the difference between type() and isinstance()?
# Answer:


# =============================================================================
# BONUS CHALLENGES (Optional)
# =============================================================================

# BONUS 1. [C] Currency split: ask for total amount (float) and number of people (int).
#            Print each person's share rounded to 2 decimal places.


# BONUS 2. [C] Type detective: write a function-less script that takes input()
#            and prints whether it's int, float, or "not a number" using try/except
#            (preview — full lesson on try/except comes later).


# BONUS 3. [C] Employee ID: ask for emp_id as input. Validate it's numeric with
#            .isdigit(), convert to int, print formatted: EMP-00042 (zero-pad to 5 digits).
#            Hint: f"EMP-{emp_id:05d}"
