"""
================================================================================
MODULE 2 — EXERCISES (for students)
================================================================================
How to practice:
  1. Read Module2_Slides.md
  2. Run module2.py and understand each print
  3. Solve exercises below in order
  4. Write code under each "# YOUR CODE HERE"
  5. Run: python exercise.py

Tips:
  - Predict output before running
  - If you use AI, explain every line yourself
  - Casting bugs are normal — fix them carefully

Difficulty tags: [E] Easy  [M] Medium  [C] Challenge
================================================================================
"""

# =============================================================================
# A. VARIABLES & NAMING
# =============================================================================

# A1. [E] Create variables for your name (str), age (int), height (float),
#     and learning_python (bool). Print all four.
# YOUR CODE HERE


# A2. [E] Create COURSE_NAME and MAX_SCORE as ALL_CAPS "constants". Print them.
# YOUR CODE HERE


# A3. [M] Swap a=100 and b=200 without a third variable. Print before and after.
# YOUR CODE HERE


# A4. [E] Set red, green, blue = 255, 128, 0 and print: RGB(255, 128, 0)
# YOUR CODE HERE


# =============================================================================
# B. TYPES
# =============================================================================

# B1. [E] Make one variable each of int, float, str, bool, None.
#     Print value and type(...) for each.
# YOUR CODE HERE


# B2. [M] Assign x = 42, print type. Then x = "forty-two", print type again.
# YOUR CODE HERE


# B3. [E] Print type(3) and type(3.0). Write a short comment: what is different?
# YOUR CODE HERE


# B4. [M] Use isinstance to check:
#     - 99 is int?
#     - "99" is int?
#     - 3.14 is int or float?
# YOUR CODE HERE


# =============================================================================
# C. CASTING
# =============================================================================

# C1. [E] Convert 100 to str and print its type.
# YOUR CODE HERE


# C2. [E] Convert "3.14" to float and print it.
# YOUR CODE HERE


# C3. [E] Print int(7.8) and int(-7.8).
# YOUR CODE HERE


# C4. [M] Print bool() for: 0, 1, "", "hello", None, "false"
#     Then write a comment explaining bool("false").
# YOUR CODE HERE


# C5. [M] Fix this so it prints 15 (not 105):
left = "10"
right = "5"
# YOUR CODE HERE


# C6. [C] Show why int("10.5") fails but float("10.5") works.
#     Write explanation in comments + working conversion to int via float.
# YOUR CODE HERE


# =============================================================================
# D. input() + CASTING  (run these in terminal)
# =============================================================================

# D1. [M] Ask name and age. Print: Hello, <name>! You are <age> years old.
# YOUR CODE HERE


# D2. [M] Ask two integers. Print sum, difference, product, quotient.
# YOUR CODE HERE


# D3. [M] Ask price (float) and quantity (int). Print total.
# YOUR CODE HERE


# D4. [M] Ask a decimal number. Print original float and int version.
# YOUR CODE HERE


# D5. [M] Celsius to Fahrenheit: F = C * 9/5 + 32. Print round(F, 1).
# YOUR CODE HERE


# =============================================================================
# E. f-strings
# =============================================================================

# E1. [E] product="Laptop", price=45999.5, in_stock=True
#     Print: Laptop | Price: 45999.5 | In stock: True   (use f-string)
# YOUR CODE HERE


# E2. [M] BMI = weight / (height ** 2). Print with 2 decimals.
# YOUR CODE HERE


# =============================================================================
# F. None
# =============================================================================

# F1. [M] middle_name = None. Build a full name from first/last only when middle is None.
# YOUR CODE HERE


# F2. [M] email = None. If email is None print "Email not provided", else print email.
# YOUR CODE HERE


# =============================================================================
# G. REAL-WORLD STYLE PRACTICE (still beginner level)
# =============================================================================

# G1. [M] STUDENT PROFILE
#     Ask name, age, gpa, enrolled (yes/no).
#     Convert types correctly.
#     enrolled should become True only if answer is yes/YES/Yes.
#     Print a neat profile card with f-strings.
# YOUR CODE HERE


# G2. [M] JSON-LIKE REQUEST VALIDATION
#     Given this dict (hard-code):
#     data = {"user_id": "42", "score": "88.5", "active": "true"}
#     Convert to int, float, and real bool.
#     Print values with their types.
# YOUR CODE HERE


# G3. [M] AI SETTINGS PARSER
#     settings = {"temperature": "0.2", "max_tokens": "128", "stream": "false"}
#     Convert correctly and print a one-line summary with f-string.
# YOUR CODE HERE


# G4. [C] FIX THE AI BUG
#     An AI wrote:
#         qty = input("Qty: ")
#         price = input("Price: ")
#         print("Total:", qty * price)
#     Recreate the bug with demo strings, show wrong behavior,
#     then show the fixed version.
# YOUR CODE HERE


# G5. [C] INVOICE
#     Ask item, unit price, quantity.
#     If price < 0 or quantity <= 0: print Invalid input
#     Else print line total, 18% tax, grand total (2 decimals).
# YOUR CODE HERE


# =============================================================================
# H. SHORT WRITTEN ANSWERS (as comments)
# =============================================================================

# H1. Why does input() need casting for math?
# Answer:


# H2. Why can AI-generated code fail even if it "looks right"?
# Answer:


# H3. What is None used for?
# Answer:


# H4. Why is bool("false") True?
# Answer:
