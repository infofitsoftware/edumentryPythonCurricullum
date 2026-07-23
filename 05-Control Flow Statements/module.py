"""
================================================================================
MODULE 5 — CONTROL FLOW STATEMENTS (Reference Program)
================================================================================
Run:  python module.py

Prerequisites:
  Module 1 — print, input, arithmetic
  Module 2 — variables, types, casting, bool, None
  Module 3 — strings
  Module 4 — operators and expressions (==, and/or/not, %, +=, ...)

This file is a REFERENCE — not an assignment.
Interactive input() demos are commented so the file runs without blocking.
================================================================================
"""

# ==================================================
# 1. WHY CONTROL FLOW?
# ==================================================
# So far programs ran top-to-bottom, every line.
# Real programs must CHOOSE paths and REPEAT work.
# Control flow = decisions (if) + repetition (for/while).

print("=== Module 5: Control Flow ===")

# ==================================================
# 2. THE if STATEMENT
# ==================================================
# Executes a block ONLY when the condition is True.
# Colon : and indentation (4 spaces) define the block.

temperature = 36

if temperature > 30:
    print("It is hot today.")

# If condition is False, the indented block is skipped.
temperature = 20
if temperature > 30:
    print("This will NOT print.")
print("This always prints (outside the if).")

# ==================================================
# 3. if-else
# ==================================================
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ==================================================
# 4. if-elif-else (MULTIPLE BRANCHES)
# ==================================================
# Only ONE branch runs. First True condition wins.

score = 0

if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Zero")

# Grade bands (uses Module 4 comparisons)
marks = 82

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Fail")

# ==================================================
# 5. INDENTATION RULES (CRITICAL)
# ==================================================
# Python uses indentation instead of { }.
# Inconsistent indentation → IndentationError.

age = 20
if age >= 18:
    print("Eligible")
    print("You may vote")
# print("bad indent")  # would error if wrongly indented under if without belonging

# ==================================================
# 6. COMBINING WITH OPERATORS (Module 4)
# ==================================================
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")

value = 30
if value % 3 == 0 and value % 5 == 0:
    print("Divisible by both 3 and 5")

# Nested if (decision inside decision)
account_active = True
balance = 500
if account_active:
    if balance >= 100:
        print("Withdrawal allowed")
    else:
        print("Insufficient balance")
else:
    print("Account inactive")

# ==================================================
# 7. range() — FOUNDATION FOR for LOOPS
# ==================================================
# range(stop)           → 0 .. stop-1
# range(start, stop)    → start .. stop-1
# range(start, stop, step)

print("range(5):", list(range(5)))           # [0, 1, 2, 3, 4]
print("range(1, 6):", list(range(1, 6)))     # [1, 2, 3, 4, 5]
print("range(0, 10, 2):", list(range(0, 10, 2)))  # even numbers
print("range(5, 0, -1):", list(range(5, 0, -1)))  # 5 4 3 2 1

# stop is EXCLUSIVE (same idea as string slicing stop)

# ==================================================
# 8. for LOOPS WITH range()
# ==================================================
print("--- for 1 to 5 ---")
for i in range(1, 6):
    print(i)

print("--- even numbers 2 to 10 ---")
for i in range(2, 11, 2):
    print(i)

# ==================================================
# 9. for OVER A STRING (Module 3)
# ==================================================
print("--- characters in Python ---")
word = "Python"
for char in word:
    print(char)

# ==================================================
# 10. for OVER A LIST / TUPLE (PREVIEW — Module 6)
# ==================================================
# You can loop over collections. Deep list study is Module 6.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = (10, 20, 30)
for num in numbers:
    print(num)

# ==================================================
# 11. ACCUMULATORS AND COUNTERS
# ==================================================
# Pattern used everywhere: start at 0, update inside loop.

total = 0
for number in range(1, 11):
    total = total + number   # or total += number
print("Sum 1..10:", total)   # 55

# Trace for smaller range:
# range(1, 4): 1 then 2 then 3 → total becomes 1, 3, 6

even_count = 0
for n in range(1, 11):
    if n % 2 == 0:
        even_count += 1
print("Even count 1..10:", even_count)  # 5

# Factorial of 5
factorial = 1
for n in range(1, 6):
    factorial *= n
print("5! =", factorial)  # 120

# ==================================================
# 12. while LOOPS
# ==================================================
# Repeats WHILE condition is True.
# You must update the condition variable or use break — else infinite loop.

print("--- while 1 to 5 ---")
i = 1
while i <= 5:
    print(i)
    i += 1

print("--- while countdown 5 to 1 ---")
i = 5
while i >= 1:
    print(i)
    i -= 1

# Sentinel-style idea (commented interactive version):
# while True:
#     number = int(input("Enter number (negative to stop): "))
#     if number < 0:
#         break
#     print("You entered:", number)

# Non-interactive demo of the same logic:
demo_inputs = [3, 8, -1]
index = 0
while True:
    number = demo_inputs[index]
    index += 1
    if number < 0:
        print("Stopped on negative.")
        break
    print("You entered:", number)

# ==================================================
# 13. break — EXIT LOOP IMMEDIATELY
# ==================================================
print("--- break when i == 5 ---")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# prints 1 2 3 4

# Password attempt simulation
secret = "admin123"
attempts = ["wrong", "nope", "admin123"]
for attempt in attempts:
    if attempt == secret:
        print("Access granted.")
        break
    print("Incorrect attempt:", attempt)
# ==================================================
# 14. continue — SKIP THIS ITERATION
# ==================================================
print("--- continue skips 5 ---")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("--- skip vowels ---")
for char in "education":
    if char in "aeiou":
        continue
    print(char)

print("--- skip multiples of 3 ---")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# ==================================================
# 15. pass — PLACEHOLDER
# ==================================================
# Does nothing. Keeps syntax valid when a block is required.

for i in range(3):
    pass

age = 15
if age >= 18:
    pass  # TODO: add adult logic later
else:
    print("Under 18 - logic pending elsewhere")

# ==================================================
# 16. NESTED LOOPS (BRIEF)
# ==================================================
print("--- 3x3 grid of coordinates ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

print("--- small star triangle ---")
for i in range(1, 5):
    print("*" * i)

# ==================================================
# 17. MULTIPLICATION TABLE
# ==================================================
table_n = 5
for i in range(1, 11):
    print(f"{table_n} x {i} = {table_n * i}")

# ==================================================
# 18. COMBINED EXAMPLE — NUMBER ANALYZER
# ==================================================
sample = 12
if sample > 0:
    print("Positive")
elif sample < 0:
    print("Negative")
else:
    print("Zero")

if sample % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Factors preview (1..sample):")
for i in range(1, sample + 1):
    if sample % i == 0:
        print(i)

# ==================================================
# 19. COMBINED EXAMPLE — VOWEL COUNTER
# ==================================================
text = "Education"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print("Vowels in Education:", vowel_count)

# ==================================================
# 20. COMMON MISTAKES (commented)
# ==================================================
# Mistake 1: missing colon
# if x > 0
#     print("yes")

# Mistake 2: wrong indentation
# if x > 0:
# print("yes")

# Mistake 3: using = instead of ==
# if x = 5:

# Mistake 4: infinite while (forgot i += 1)
# i = 1
# while i <= 5:
#     print(i)

# Mistake 5: off-by-one with range
# range(1, 10) stops at 9, not 10

# Mistake 6: break vs continue confusion
# break exits; continue only skips current iteration

print("\n--- Module 5 control flow reference complete ---")
