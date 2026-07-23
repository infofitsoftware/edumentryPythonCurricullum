"""
================================================================================
MODULE 4 — OPERATORS AND EXPRESSIONS (Reference Program)
================================================================================
Run:  python module.py

Prerequisites:
  Module 1 — print, input, arithmetic intro
  Module 2 — variables, types, casting, None, bool
  Module 3 — strings (indexing, methods, in for strings)

This file is a REFERENCE — not an assignment.
================================================================================
"""

# ==================================================
# 1. WHAT IS AN OPERATOR? WHAT IS AN EXPRESSION?
# ==================================================
# Operator  = a symbol that performs an action (+, ==, and, ...)
# Operand   = the value(s) the operator works on
# Expression = combination that produces a result

score = 10 + 5          # expression using +
print("Score:", score)  # 15

is_passing = score >= 15
print("Passing?:", is_passing)  # True

# ==================================================
# 2. ARITHMETIC OPERATORS
# ==================================================
# Revisit Module 1 with more precision and real uses.

price = 10
quantity = 3

print("Addition:", price + quantity)       # 13
print("Subtraction:", price - quantity)    # 7
print("Multiplication:", price * quantity) # 30
print("Division:", price / quantity)       # 3.333...  (always float in Python 3)
print("Floor Division:", price // quantity)  # 3
print("Modulus:", price % quantity)        # 1  (remainder)
print("Exponent:", 2 ** 3)                 # 8

# Practical: even / odd check uses modulus
number = 14
print("Remainder when divided by 2:", number % 2)  # 0 → even

# Practical: pagination / packing leftover items
items = 17
box_size = 5
full_boxes = items // box_size
leftover = items % box_size
print("Full boxes:", full_boxes, "| Leftover:", leftover)

# ==================================================
# 3. OPERATOR PRECEDENCE (BEGINNER VIEW)
# ==================================================
# Rough order (high → low): ** then * / // % then + - then comparisons then not/and/or
# When unsure: use parentheses.

print(2 + 3 * 4)        # 14  (multiply first)
print((2 + 3) * 4)      # 20  (parentheses first)
print(2 ** 3 ** 2)      # 512 (exponentiation is right-associative: 2 ** (3 ** 2))
print((2 ** 3) ** 2)    # 64

# ==================================================
# 4. COMPARISON (RELATIONAL) OPERATORS
# ==================================================
# Always return bool: True or False

student_age = 20
voting_age = 18

print(student_age > voting_age)    # True
print(student_age < voting_age)    # False
print(student_age == 20)           # True  (equal to)
print(student_age != 18)           # True  (not equal)
print(student_age >= 18)           # True
print(student_age <= 17)           # False

# Common mistake: = assigns, == compares
account_balance = 100              # assignment
print(account_balance == 100)      # comparison → True

# String comparisons (Module 3) — case sensitive
print("admin" == "Admin")          # False
print("apple" < "banana")          # True (dictionary / lexicographic order)

# ==================================================
# 5. LOGICAL OPERATORS — and, or, not
# ==================================================
# Combine True/False results. Essential for validation rules.

has_ticket = True
has_id = False

print(has_ticket and has_id)   # False — both must be True
print(has_ticket or has_id)    # True  — at least one True
print(not has_id)              # True  — reverses False → True

# Truth table quick demo
print(True and True)     # True
print(True and False)    # False
print(False or True)     # True
print(False or False)    # False
print(not True)          # False

# Practical: login check (values only — decision structure in Module 5)
username = "admin"
password = "1234"
entered_user = "admin"
entered_pass = "1234"
credentials_ok = (entered_user == username) and (entered_pass == password)
print("Credentials OK?:", credentials_ok)

# Practical: divisible by both 3 and 5
value = 30
divisible_by_both = (value % 3 == 0) and (value % 5 == 0)
print("Divisible by 3 and 5?:", divisible_by_both)

# ==================================================
# 6. TRUTHY / FALSY WITH LOGICAL OPERATORS (BRIEF)
# ==================================================
# From Module 2: 0, "", None are falsy. Non-empty strings / non-zero numbers are truthy.
# and / or return one of the operands (advanced detail) — beginners: focus on True/False results
# when both sides are already comparisons.

print(bool(0))
print(bool(5))
print(bool(""))
print(bool("hi"))

# ==================================================
# 7. ASSIGNMENT OPERATORS
# ==================================================
# Update a variable using its current value.

cart_total = 10
cart_total += 5      # cart_total = cart_total + 5
print(cart_total)    # 15

cart_total *= 2      # 30
print(cart_total)

cart_total -= 4      # 26
print(cart_total)

cart_total /= 2      # 13.0  (/= always can produce float)
print(cart_total)

points = 17
points //= 5         # 3
print(points)
points = 17
points %= 5          # 2
print(points)
base = 2
base **= 3           # 8
print(base)

# ==================================================
# 8. MEMBERSHIP OPERATORS — in / not in
# ==================================================
# Module 3 used these with strings. Same idea for other sequences later.

email_address = "student@example.com"
print("@" in email_address)          # True
print("gmail" not in email_address)  # True

# Preview with a simple list (collections fully covered in Module 6)
allowed_roles = ["admin", "editor", "viewer"]
print("editor" in allowed_roles)     # True
print("guest" not in allowed_roles)  # True

# ==================================================
# 9. IDENTITY OPERATORS — is / is not
# ==================================================
# is  → True if both names refer to the SAME object in memory
# ==  → True if values are equal (may be different objects)

# Most important beginner use: None checks (Module 2 style)
result = None
print(result is None)        # True  (preferred)
print(result is not None)    # False

# Classic is vs == demonstration with lists (preview of Module 6)
list_a = [1, 2, 3]
list_b = list_a              # same object
list_c = [1, 2, 3]           # equal values, different object

print(list_a is list_b)      # True
print(list_a is list_c)      # False
print(list_a == list_c)      # True  (same content)

# Caution: do NOT use `is` to compare ordinary numbers or strings for equality.
# Use == for values. Use `is` mainly for None (and advanced identity cases).

# ==================================================
# 10. COMBINED EXPRESSIONS (Modules 1–4)
# ==================================================
product_price = 499.5
item_count = 2
discount_ok = True
subtotal = product_price * item_count
if discount_ok:
    payable = subtotal * 0.9
else:
    payable = subtotal
print(f"Payable: {payable:.2f}")

# Input + cast + comparison (non-interactive demo)
typed_age = "20"
age = int(typed_age)
can_vote = age >= 18
print("Can vote?:", can_vote)

# String clean + comparison (Module 3 + Module 4)
typed_name = "  Admin "
is_admin = typed_name.strip().lower() == "admin"
print("Is admin?:", is_admin)

# ==================================================
# 11. COMMON MISTAKES (commented demos)
# ==================================================
# Mistake 1: using = instead of ==
# if age = 18:          # SyntaxError — assignment in condition (Python 3)

# Mistake 2: chaining confusion beginners invent
# print(5 < x < 3) is valid Python (smart chaining) but learn pairwise first

# Mistake 3: confusing / and //
# print(5 / 2)   → 2.5
# print(5 // 2)  → 2

# Mistake 4: confusing is and ==
# Use == for values; is for identity / None

# Mistake 5: operator precedence without parentheses
# Write (a and b) or c when intent must be clear

print("\n--- Module 4 operators reference complete ---")
