"""
================================================================================
MODULE 3 — Strings in Python
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 2 (variables, types, casting)
Next:     Module 4 (operators)
================================================================================
"""

print("=== Module 3: Strings in Python ===")

# --------------------------------------------------
# 1) What is a string?
# --------------------------------------------------
greeting = "Hello"
city = "Mumbai"
message = """Welcome to
Python strings."""

print(greeting)
print(city)
print(message)

# Prefer the quote style that avoids escaping
sentence = "It's a great day to learn Python"
quoted = 'He said "Python is fun"'
print(sentence)
print(quoted)

empty_text = ""
space_text = " "
print("Empty length:", len(empty_text))   # 0
print("Space length:", len(space_text))   # 1
print("bool empty:", bool(empty_text))    # False
print("bool space:", bool(space_text))    # True

# --------------------------------------------------
# 2) Immutability — methods return NEW strings
# --------------------------------------------------
original_name = "alice"
upper_name = original_name.upper()
print("Original:", original_name)   # alice
print("New copy:", upper_name)      # ALICE

# Wrong (TypeError) if uncommented:
# original_name[0] = "A"

fixed_name = "A" + original_name[1:]
print("Fixed name:", fixed_name)    # Alice

# AI bug pattern: call replace, forget to assign
msg = "bad"
msg.replace("bad", "good")
print("Forgot assign:", msg)        # still bad
msg = msg.replace("bad", "good")
print("After assign:", msg)         # good

# --------------------------------------------------
# 3) Indexing
# --------------------------------------------------
#  P y t h o n
#  0 1 2 3 4 5
# -6-5-4-3-2-1
language = "Python"
print("First:", language[0])
print("Second:", language[1])
print("Last:", language[-1])
print("Second last:", language[-2])
print("Last index number:", len(language) - 1)

# --------------------------------------------------
# 4) Slicing — [start:stop:step]
# --------------------------------------------------
# start included, stop EXCLUDED
course_title = "Programming"
print(course_title[0:5])     # Progr
print(course_title[:6])      # Progra
print(course_title[3:])      # gramming
print(course_title[:])       # Programming
print(course_title[::2])     # every 2nd char
print(course_title[::-1])    # reverse

file_name = "report.pdf"
print("Extension-ish:", file_name[-3:])  # pdf

# --------------------------------------------------
# 5) len, +, *
# --------------------------------------------------
product_code = "SKU-4421"
print("Length:", len(product_code))

first_name = "Ada"
last_name = "Lovelace"
print(first_name + " " + last_name)
print("-" * 20)
print("Ha" * 3)
print("5" + "3")  # concatenation → 53

# --------------------------------------------------
# 6) Membership — in / not in
# --------------------------------------------------
email_address = "student@example.com"
print("@" in email_address)
print("gmail" in email_address)
print("xyz" not in email_address)
print("py" in "Python")  # False — case sensitive

# --------------------------------------------------
# 7) Case + strip (cleaning pattern)
# --------------------------------------------------
raw_title = "pYtHoN pRoGrAmMiNg"
print(raw_title.upper())
print(raw_title.lower())
print(raw_title.title())
print(raw_title.capitalize())
print("Still original:", raw_title)

user_input = "   hello   "
print("|" + user_input.strip() + "|")
print("|" + user_input.lstrip() + "|")
print("|" + user_input.rstrip() + "|")

typed_username = "  Admin  "
clean_username = typed_username.strip().lower()
print("Clean username:", clean_username)

# --------------------------------------------------
# 8) find, count, startswith, endswith
# --------------------------------------------------
sentence_text = "I love to code in Python"
print("find code:", sentence_text.find("code"))
print("find Java:", sentence_text.find("Java"))  # -1
print("count o:", sentence_text.count("o"))
print(sentence_text.startswith("I "))
print(sentence_text.endswith("Python"))

script_name = "backup.py"
print("Is .py?:", script_name.endswith(".py"))

# Case-sensitive find
print("find python in Python:", "Python".find("python"))  # -1

# --------------------------------------------------
# 9) replace, split, join
# --------------------------------------------------
review = "This is a bad day"
print(review.replace("bad", "good"))

phrase = "Python is fun to learn"
print(phrase.split())

csv_line = "Alice,25,Engineer"
print(csv_line.split(","))

parts = ["I", "love", "Python"]
print("-".join(parts))
print(" ".join(["Hello", "World"]))

# --------------------------------------------------
# 10) Content checks
# --------------------------------------------------
print("12345".isdigit())
print("Python".isalpha())
print("Hello123".isalnum())
print("Hello 123".isalnum())  # False — space
print("   ".isspace())
print("".isdigit())           # False

phone_digits = "9876543210"
print("Looks like digits only:", phone_digits.isdigit())

# --------------------------------------------------
# 11) f-strings
# --------------------------------------------------
student_name = "John"
student_age = 30
book_price = 49.99
print(f"My name is {student_name} and I am {student_age} years old.")
print(f"The price of the book is ${book_price}")
print(f"Price rounded: ${book_price:.2f}")
print(f"Line total: {3 * 12.5}")

# --------------------------------------------------
# 12) Escape sequences + raw strings
# --------------------------------------------------
print("Hello\nWorld")
print("Name:\tAlice")
print("Path tip: C:\\Users\\Student")
print("She said \"Hi\"")

print(r"C:\newfolder\test")
print(r"Line1\nLine2")  # literal \n

# --------------------------------------------------
# 13) Real-world preview: clean profile / email / file / prompt
# --------------------------------------------------
first = "  sara  "
last = "KHAN"
role = "data analyst"
profile_line = f"{first.strip().title()} {last.strip().title()} | Role: {role.strip().title()}"
print(profile_line)

raw_email = "  Student@Example.COM  "
email = raw_email.strip().lower()
print("Stored email:", email)
print("Has @ symbol:", "@" in email)

uploaded_file = "  Invoice_March.PDF  "
normalized = uploaded_file.strip().lower()
print("Normalized:", normalized)
print("Is PDF?:", normalized.endswith(".pdf"))

# AI / LLM style: clean a prompt before measuring length
prompt = "  Summarize this article in 3 bullets.  "
clean_prompt = prompt.strip()
print(f"Prompt: {clean_prompt}")
print(f"Prompt length: {len(clean_prompt)}")

# JSON-like text fields often need cleaning + casting (Module 2 + 3)
row = "  Ada , 25 , true "
name_part, age_part, active_part = [p.strip() for p in row.split(",")]
print("Parsed name:", name_part)
print("Parsed age text:", age_part, "->", int(age_part))
print("Parsed active:", active_part.lower() == "true")

print("\n--- Module 3 complete. Open module_exercises.md and practice. ---")
