"""
================================================================================
MODULE 4 — Operators and Expressions
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 3 (strings)
Next:     Module 5 (control flow)
================================================================================
"""

print("=== Module 4: Operators and Expressions ===")

# --------------------------------------------------
# 1) Operator, operand, expression
# --------------------------------------------------
score = 10 + 5
print("Score:", score)                 # 15
is_passing = score >= 15
print("Passing?:", is_passing)         # True

# --------------------------------------------------
# 2) Arithmetic operators
# --------------------------------------------------
price = 10
quantity = 3
print("Add:", price + quantity)        # 13
print("Sub:", price - quantity)        # 7
print("Mul:", price * quantity)        # 30
print("Div:", price / quantity)        # 3.333... float
print("Floor:", price // quantity)     # 3
print("Mod:", price % quantity)        # 1
print("Power:", 2 ** 3)                # 8

# Even / odd uses modulus
number = 14
print("14 % 2:", number % 2)           # 0 → even
print("15 % 2:", 15 % 2)               # 1 → odd

# Boxes and leftovers (pagination / packing idea)
items = 17
box_size = 5
full_boxes = items // box_size
leftover = items % box_size
print("Full boxes:", full_boxes)       # 3
print("Leftover:", leftover)           # 2

# --------------------------------------------------
# 3) Precedence — when unsure, use parentheses
# --------------------------------------------------
print(2 + 3 * 4)                       # 14
print((2 + 3) * 4)                     # 20
print(2 ** 3 ** 2)                     # 512 → 2 ** (3 ** 2)
print((2 ** 3) ** 2)                   # 64

# --------------------------------------------------
# 4) Comparison operators → always bool
# --------------------------------------------------
student_age = 20
print(student_age > 18)                # True
print(student_age < 18)                # False
print(student_age == 20)               # True
print(student_age != 18)               # True
print(student_age >= 18)               # True
print(student_age <= 17)               # False

# = assigns, == compares  (AI bug magnet)
account_balance = 100
print(account_balance == 100)          # True

# Strings: case matters (Module 3)
print("admin" == "Admin")              # False
print("apple" < "banana")              # True (dictionary order)

# --------------------------------------------------
# 5) Logical operators — and / or / not
# --------------------------------------------------
has_ticket = True
has_id = False
print(has_ticket and has_id)           # False
print(has_ticket or has_id)            # True
print(not has_id)                      # True

print(True and True)                   # True
print(True and False)                  # False
print(False or True)                   # True
print(False or False)                  # False
print(not True)                        # False

# Login-style rule (expression only — if comes in Module 5)
username = "admin"
password = "1234"
entered_user = "admin"
entered_pass = "1234"
credentials_ok = (entered_user == username) and (entered_pass == password)
print("Credentials OK?:", credentials_ok)

# Divisible by both 3 and 5
value = 30
divisible_by_both = (value % 3 == 0) and (value % 5 == 0)
print("Divisible by 3 and 5?:", divisible_by_both)

value = 10
print("10 by 3 and 5?:", (value % 3 == 0) and (value % 5 == 0))  # False

# --------------------------------------------------
# 6) Truthy / falsy reminder (Module 2)
# --------------------------------------------------
print(bool(0))                         # False
print(bool(5))                         # True
print(bool(""))                        # False
print(bool("hi"))                      # True
print(bool(None))                      # False

# --------------------------------------------------
# 7) Assignment operators
# --------------------------------------------------
cart_total = 10
cart_total += 5
print("After += 5:", cart_total)       # 15
cart_total *= 2
print("After *= 2:", cart_total)       # 30
cart_total -= 4
print("After -= 4:", cart_total)       # 26
cart_total /= 2
print("After /= 2:", cart_total)       # 13.0

points = 17
points //= 5
print("17 //= 5 →", points)            # 3

points = 17
points %= 5
print("17 %= 5 →", points)             # 2

base = 2
base **= 3
print("2 **= 3 →", base)               # 8

# Trace chain (same as notes)
x = 5
x += 3
print("x after +=3:", x)               # 8
x *= 2
print("x after *=2:", x)               # 16
x -= 4
print("x after -=4:", x)               # 12

# --------------------------------------------------
# 8) Membership — in / not in
# --------------------------------------------------
email_address = "student@example.com"
print("@" in email_address)            # True
print("gmail" not in email_address)    # True
print("py" in "Python")                # False — case sensitive

# Light list preview (full collections in Module 6)
allowed_roles = ["admin", "editor", "viewer"]
print("editor" in allowed_roles)       # True
print("guest" not in allowed_roles)    # True

# --------------------------------------------------
# 9) Identity — is / is not (especially None)
# --------------------------------------------------
result = None
print(result is None)                  # True (preferred)
print(result is not None)              # False

list_a = [1, 2, 3]
list_b = list_a                        # same object
list_c = [1, 2, 3]                     # equal values, different object
print("a is b:", list_a is list_b)     # True
print("a is c:", list_a is list_c)     # False
print("a == c:", list_a == list_c)     # True

# AI smell: do not use `is` for ordinary value equality
# Prefer: score == 100
# Avoid:  score is 100

# --------------------------------------------------
# 10) Combine Modules 1–4 (clean → compare → decide later)
# --------------------------------------------------
typed_age = "20"
age = int(typed_age)
can_vote = age >= 18
print("Can vote?:", can_vote)

typed_name = "  Admin "
is_admin = typed_name.strip().lower() == "admin"
print("Is admin?:", is_admin)

product_price = 499.5
item_count = 2
subtotal = product_price * item_count
print("Subtotal:", subtotal)           # 999.0
print("With 10% off:", subtotal * 0.9) # 899.1
print("Over 500?:", subtotal > 500)    # True

# AI / automation style thresholds
tokens_used = 1200
budget = 1000
print("Over budget?:", tokens_used > budget)

cpu_percent = 92
print("CPU alert?:", cpu_percent > 90)

# Email gate expression
raw_email = "  Student@Example.COM  "
email = raw_email.strip().lower()
looks_valid = ("@" in email) and ("." in email)
print("Clean email:", email)
print("Looks valid?:", looks_valid)

# --------------------------------------------------
# 11) Common AI / beginner bugs (shown safely)
# --------------------------------------------------
# Bug: forgot to cast input text before comparing as a number
# String compare can lie: "9" > "18" is True as text, but 9 > 18 is False
age_text = "9"
print("Wrong compare (text):", age_text > "18")   # True — lexicographic trap
print("Right compare (int):", int(age_text) > 18) # False — correct numeric check

# Bug: = vs ==  (assignment vs comparison) — comparison version:
flag = 10
print("Compared with == :", flag == 10)

# Bug: / vs //
print("5 / 2  →", 5 / 2)               # 2.5
print("5 // 2 →", 5 // 2)              # 2

print("\n--- Module 4 complete. Open module_exercises.md and practice. ---")
