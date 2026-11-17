"""
================================================================================
MODULE 5 — Control Flow Statements
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 4 (operators)
Next:     Module 6 (collections)

Interactive input() demos are avoided so this file runs without blocking.
================================================================================
"""

print("=== Module 5: Control Flow Statements ===")

# --------------------------------------------------
# 1) if — run a block only when condition is True
# --------------------------------------------------
temperature = 36
if temperature > 30:
    print("It is hot today.")

temperature = 20
if temperature > 30:
    print("This will NOT print.")
print("This always prints (outside the if).")

age = 20
if age >= 18:
    print("Eligible")
print("Done")

# --------------------------------------------------
# 2) if-else — exactly one path
# --------------------------------------------------
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# --------------------------------------------------
# 3) if-elif-else — first True branch wins
# --------------------------------------------------
score = 0
if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Zero")

marks = 82
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Average")
else:
    print("Fail")

# Wrong order demo (commented): putting >= 50 first would mis-label 82 as Average
# if marks >= 50:
#     print("Average")   # would catch 82 too early
# elif marks >= 75:
#     print("Good")

# --------------------------------------------------
# 4) Indentation — multiple lines in one block
# --------------------------------------------------
age = 20
if age >= 18:
    print("Eligible")
    print("You may vote")

# --------------------------------------------------
# 5) Compound conditions + nested if (Module 4)
# --------------------------------------------------
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")

value = 30
if value % 3 == 0 and value % 5 == 0:
    print("Divisible by both 3 and 5")

account_active = True
balance = 500
if account_active:
    if balance >= 100:
        print("Withdrawal allowed")
    else:
        print("Insufficient balance")
else:
    print("Account inactive")

# --------------------------------------------------
# 6) range() — stop is EXCLUSIVE
# --------------------------------------------------
print("range(5):", list(range(5)))                 # [0, 1, 2, 3, 4]
print("range(1, 6):", list(range(1, 6)))           # [1, 2, 3, 4, 5]
print("range(0, 10, 2):", list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print("range(5, 0, -1):", list(range(5, 0, -1)))   # [5, 4, 3, 2, 1]

# --------------------------------------------------
# 7) for with range
# --------------------------------------------------
print("--- for 1 to 5 ---")
for i in range(1, 6):
    print(i)

print("--- even numbers 2 to 10 ---")
for i in range(2, 11, 2):
    print(i)

# --------------------------------------------------
# 8) for over string / simple list
# --------------------------------------------------
print("--- characters in Python ---")
for char in "Python":
    print(char)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# --------------------------------------------------
# 9) Accumulators and counters
# --------------------------------------------------
total = 0
for number in range(1, 11):
    total += number
print("Sum 1..10:", total)   # 55

# Small trace target: range(1, 4) → total becomes 1, then 3, then 6
demo_total = 0
for number in range(1, 4):
    demo_total += number
print("Sum 1..3:", demo_total)  # 6

even_count = 0
for n in range(1, 11):
    if n % 2 == 0:
        even_count += 1
print("Even count 1..10:", even_count)  # 5

factorial = 1
for n in range(1, 6):
    factorial *= n
print("5! =", factorial)  # 120

# Sum of even numbers 1..5 (notes full-trace example)
even_sum = 0
for n in range(1, 6):
    if n % 2 == 0:
        even_sum += n
print("Even sum 1..5:", even_sum)  # 6

# --------------------------------------------------
# 10) while loops — remember to update
# --------------------------------------------------
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

# Sentinel-style loop (non-interactive demo)
demo_inputs = [3, 8, -1]
index = 0
while True:
    number = demo_inputs[index]
    index += 1
    if number < 0:
        print("Stopped on negative.")
        break
    print("You entered:", number)

# Infinite loop bug (DO NOT uncomment):
# i = 1
# while i <= 5:
#     print(i)
#     # missing i += 1

# --------------------------------------------------
# 11) break — exit loop immediately
# --------------------------------------------------
print("--- break when i == 5 ---")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# prints 1 2 3 4

secret = "admin123"
attempts = ["wrong", "nope", "admin123"]
for attempt in attempts:
    if attempt == secret:
        print("Access granted.")
        break
    print("Incorrect attempt:", attempt)

# --------------------------------------------------
# 12) continue — skip this iteration
# --------------------------------------------------
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

# --------------------------------------------------
# 13) pass — placeholder
# --------------------------------------------------
for i in range(3):
    pass

age = 15
if age >= 18:
    pass  # TODO: adult logic later
else:
    print("Under 18 - logic pending elsewhere")

# --------------------------------------------------
# 14) Nested loops (intro)
# --------------------------------------------------
print("--- small star triangle ---")
for i in range(1, 5):
    print("*" * i)

print("--- 3x3 grid ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

# --------------------------------------------------
# 15) Multiplication table
# --------------------------------------------------
table_n = 5
for i in range(1, 11):
    print(f"{table_n} x {i} = {table_n * i}")

# --------------------------------------------------
# 16) Combined: number analyzer
# --------------------------------------------------
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

print("Factors of 12:")
for i in range(1, sample + 1):
    if sample % i == 0:
        print(i)

# --------------------------------------------------
# 17) Combined: vowel counter
# --------------------------------------------------
text = "Education"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print("Vowels in Education:", vowel_count)

# --------------------------------------------------
# 18) AI-era preview: skip empty prompts
# --------------------------------------------------
prompts = ["  summarize this  ", "", "  ", "write a title"]
for raw in prompts:
    clean = raw.strip()
    if clean == "":
        continue
    print(f"Ready prompt: {clean}")

# Threshold alert style
cpu_percent = 92
if cpu_percent > 90:
    print("CPU alert")
else:
    print("CPU normal")

# --------------------------------------------------
# 19) Common mistakes (commented)
# --------------------------------------------------
# Mistake 1: missing colon
# if x > 0
#     print("yes")

# Mistake 2: wrong indentation
# if x > 0:
# print("yes")

# Mistake 3: = instead of ==
# if x = 5:

# Mistake 4: infinite while (forgot update)

# Mistake 5: range stop exclusive
# range(1, 10) stops at 9, not 10

# Mistake 6: break vs continue confusion

print("\n--- Module 5 complete. Open module_exercises.md and practice. ---")
