"""
================================================================================
MODULE 3 — STRINGS IN PYTHON (Reference Program)
================================================================================
Run:  python module.py

Prerequisites: Module 1 (print, input, arithmetic), Module 2 (variables, types)
This file is a REFERENCE — not an assignment. Study and re-run sections.
================================================================================
"""

# ==================================================
# 1. WHAT IS A STRING?
# ==================================================
# A string is text: a sequence of characters inside quotes.
# Used for names, messages, file paths, emails, log lines, API responses.

greeting = "Hello"
city = 'Mumbai'
message = """Welcome to
Python strings."""

print(greeting)
print(city)
print(message)
# Expected: Hello / Mumbai / Welcome to (newline) Python strings.

# ==================================================
# 2. CREATING STRINGS — QUOTE STYLES
# ==================================================
single_quote = 'It is a sunny day'
double_quote = "She said hello"
# Prefer the quote style that avoids escaping apostrophes/quotes:
sentence = "It's a great day to learn Python"
quoted = 'He said "Python is fun"'

print(sentence)
print(quoted)

# Empty string — useful as a starting value or "no text yet"
empty_text = ""
print("Empty length:", len(empty_text))  # 0

# ==================================================
# 3. STRINGS ARE IMMUTABLE
# ==================================================
# Immutable means: you cannot change a character inside an existing string.
# Methods like .upper() return a NEW string; the original stays the same.

original_name = "alice"
upper_name = original_name.upper()

print("Original:", original_name)   # alice  (unchanged)
print("New copy:", upper_name)      # ALICE

# This would cause TypeError if uncommented:
# original_name[0] = "A"

# Correct way to "change" text: build a new string
fixed_name = "A" + original_name[1:]
print("Fixed name:", fixed_name)    # Alice

# ==================================================
# 4. INDEXING — POSITIVE AND NEGATIVE
# ==================================================
# Each character has a position (index).
# Forward:  0  1  2  3  4  5
# Char:     P  y  t  h  o  n
# Reverse: -6 -5 -4 -3 -2 -1

language = "Python"
print("First char:", language[0])      # P
print("Second char:", language[1])     # y
print("Last char:", language[-1])      # n
print("Second last:", language[-2])    # o

# IndexError if index is out of range (commented demo):
# print(language[100])

# ==================================================
# 5. SLICING — [start:stop:step]
# ==================================================
# start  = inclusive (included)
# stop   = exclusive (NOT included)
# step   = how many characters to skip (default 1)

course_title = "Programming"

print(course_title[0:5])     # Progr   (indexes 0,1,2,3,4)
print(course_title[:6])      # Progra  (from start to index 5)
print(course_title[3:])      # gramming
print(course_title[:])       # Programming (full copy)
print(course_title[::2])     # Pormig  (every 2nd character)
print(course_title[::-1])    # gnimmargorP (reverse)

# Practical: extract filename extension idea (simple version)
file_name = "report.pdf"
print("Extension-ish slice:", file_name[-3:])  # pdf

# ==================================================
# 6. LENGTH — len()
# ==================================================
product_code = "SKU-4421"
print("Length:", len(product_code))  # 8
print("Last index is:", len(product_code) - 1)

# ==================================================
# 7. CONCATENATION (+) AND REPETITION (*)
# ==================================================
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)  # Ada Lovelace

separator_line = "-" * 20
print(separator_line)
print("Ha" * 3)   # HaHaHa

# Remember Module 2: "5" + "3" concatenates strings → "53"
print("5" + "3")

# ==================================================
# 8. MEMBERSHIP — in / not in
# ==================================================
email_address = "student@example.com"
print("@" in email_address)           # True
print("gmail" in email_address)       # False
print("xyz" not in email_address)     # True

# ==================================================
# 9. CASE METHODS
# ==================================================
raw_title = "pYtHoN pRoGrAmMiNg"

print(raw_title.upper())       # PYTHON PROGRAMMING
print(raw_title.lower())       # python programming
print(raw_title.title())       # Python Programming
print(raw_title.capitalize())  # Python programming
print(raw_title.swapcase())    # PyThOn PrOgRaMmInG

# Immutability reminder: raw_title itself is unchanged
print("Still original:", raw_title)

# ==================================================
# 10. STRIPPING WHITESPACE
# ==================================================
user_input = "   hello   "
print("|" + user_input.strip() + "|")    # |hello|
print("|" + user_input.lstrip() + "|")   # |hello   |
print("|" + user_input.rstrip() + "|")   # |   hello|

# Practical: clean typed username before comparing
typed_username = "  admin  "
clean_username = typed_username.strip().lower()
print("Clean username:", clean_username)  # admin

# ==================================================
# 11. SEARCHING — find, index, count, startswith, endswith
# ==================================================
sentence = "I love to code in Python"

print(sentence.find("code"))      # 10 (starting index)
print(sentence.find("Java"))      # -1 (not found — safe)
print(sentence.count("o"))        # 4
print(sentence.startswith("I "))  # True
print(sentence.endswith("Python"))  # True

# index() is like find() but raises ValueError if missing (safer to use find
# when you are not sure the substring exists):
print(sentence.index("love"))     # 2

# File-type checks (automation / DevOps style)
script_name = "backup.py"
print(script_name.endswith(".py"))   # True
print(script_name.startswith("back"))  # True

# ==================================================
# 12. REPLACE, SPLIT, JOIN
# ==================================================
review = "This is a bad day"
print(review.replace("bad", "good"))  # This is a good day

phrase = "Python is fun to learn"
word_list = phrase.split()            # split on whitespace
print(word_list)                      # ['Python', 'is', 'fun', 'to', 'learn']

csv_line = "Alice,25,Engineer"
fields = csv_line.split(",")
print(fields)                         # ['Alice', '25', 'Engineer']

parts = ["I", "love", "Python"]
joined = "-".join(parts)
print(joined)                         # I-love-Python

# Note: join works on an iterable of STRINGS
print(" ".join(["Hello", "World"]))

# ==================================================
# 13. CONTENT CHECKS — isdigit, isalpha, isalnum, isspace
# ==================================================
print("12345".isdigit())     # True
print("Python".isalpha())    # True
print("Hello123".isalnum())  # True  (letters and/or digits, no spaces/symbols)
print("Hello 123".isalnum()) # False (space is not alphanumeric)
print("   ".isspace())       # True
print("".isdigit())          # False (empty string)

# Practical validation preview (backend / forms)
phone_digits = "9876543210"
print("Looks like digits only:", phone_digits.isdigit())

# ==================================================
# 14. STRING FORMATTING — format() AND f-STRINGS
# ==================================================
student_name = "John"
student_age = 30
book_price = 49.99

print("My name is {} and I am {} years old.".format(student_name, student_age))
print(f"My name is {student_name} and I am {student_age} years old.")
print(f"The price of the book is ${book_price}")
print(f"Price rounded: ${book_price:.2f}")

# Expressions inside f-strings (uses Module 1 arithmetic + Module 2 types)
quantity = 3
unit_price = 12.5
print(f"Line total: {quantity * unit_price}")

# ==================================================
# 15. ESCAPE SEQUENCES
# ==================================================
print("Hello\nWorld")      # newline between Hello and World
print("Name:\tAlice")      # tab space
print("Path tip: C:\\Users\\Student")  # escaped backslashes
print("She said \"Hi\"")   # quotes inside string

# ==================================================
# 16. RAW STRINGS
# ==================================================
# Raw strings (r"...") treat backslashes as normal characters.
# Useful for Windows paths and later for regex patterns.

print(r"C:\newfolder\test")
print(r"Line1\nLine2")     # prints \n literally — does NOT make a newline

# ==================================================
# 17. COMBINED EXAMPLE — PROFILE LINE (Modules 1–3)
# ==================================================
# Concepts used: variables, casting preview, f-strings, strip, title, upper

first = "  sara  "
last = "KHAN"
role = "data analyst"

clean_first = first.strip().title()
clean_last = last.strip().title()
clean_role = role.strip().title()

profile_line = f"{clean_first} {clean_last} | Role: {clean_role}"
print(profile_line)
# Expected: Sara Khan | Role: Data Analyst

# ==================================================
# 18. COMBINED EXAMPLE — SIMPLE INPUT CLEANING
# ==================================================
# Uncomment to try interactively:
# raw_email = input("Enter email: ")
# email = raw_email.strip().lower()
# print(f"Stored email: {email}")
# print("Has @ symbol:", "@" in email)

# Non-interactive demo of the same logic:
raw_email = "  Student@Example.COM  "
email = raw_email.strip().lower()
print("Stored email:", email)
print("Has @ symbol:", "@" in email)

# ==================================================
# 19. COMBINED EXAMPLE — FILENAME CHECKER
# ==================================================
uploaded_file = "  Invoice_March.PDF  "
normalized = uploaded_file.strip().lower()

print("Normalized:", normalized)
print("Is PDF?:", normalized.endswith(".pdf"))
print("Is Python file?:", normalized.endswith(".py"))

# ==================================================
# 20. COMMON MISTAKES (commented — do not uncomment blindly)
# ==================================================
# Mistake 1: trying to change a character in place
# text = "cat"
# text[0] = "b"          # TypeError — strings are immutable

# Mistake 2: confusing find() result -1 with a real index
# position = "abc".find("z")   # -1 means NOT FOUND

# Mistake 3: forgetting that slicing stop is exclusive
# "Python"[0:3] is "Pyt", not "Pyth"

# Mistake 4: joining non-strings
# "-".join([1, 2, 3])    # TypeError — convert to str first

# Mistake 5: expecting upper() to change the original variable
# name = "bob"
# name.upper()
# print(name)            # still "bob" unless you assign: name = name.upper()

print("\n--- Module 3 string reference complete ---")
