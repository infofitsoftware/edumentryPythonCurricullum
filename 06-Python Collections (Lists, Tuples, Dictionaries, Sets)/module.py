"""
================================================================================
MODULE 6 — PYTHON COLLECTIONS (Reference Program)
Lists, Tuples, Dictionaries, Sets
================================================================================
Run:  python module.py

Prerequisites: Modules 1-5 (types, strings, operators, control flow)

This file is a REFERENCE — not an assignment.
================================================================================
"""

print("=== Module 6: Collections ===")

# ==================================================
# 1. WHY COLLECTIONS?
# ==================================================
# Variables hold one value. Real programs hold MANY values:
# shopping cart items, student scores, config settings, unique IDs.
#
# | Type   | Ordered? | Mutable? | Duplicates? | Access        |
# |--------|----------|----------|-------------|---------------|
# | list   | Yes      | Yes      | Yes         | index         |
# | tuple  | Yes      | No       | Yes         | index         |
# | dict   | Yes*     | Yes      | keys unique | key           |
# | set    | No       | Yes      | No          | membership    |
# *dict order preserved since Python 3.7+

# ==================================================
# 2. LISTS — CREATE
# ==================================================
empty_list = []
scores = [85, 90, 78, 92]
mixed = [10, "Python", 3.14, True]
nested = [[1, 2], ["a", "b"]]

print(scores)
print(mixed)
print(nested)

# ==================================================
# 3. LISTS — INDEXING & SLICING (like strings)
# ==================================================
numbers = [10, 20, 30, 40, 50]
print(numbers[0])      # 10
print(numbers[-1])     # 50
print(numbers[1:4])    # [20, 30, 40]
print(numbers[:3])     # [10, 20, 30]
print(numbers[::2])    # [10, 30, 50]
print(numbers[::-1])   # [50, 40, 30, 20, 10]

# ==================================================
# 4. LISTS ARE MUTABLE
# ==================================================
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Contrast with strings (Module 3): strings cannot do text[0] = "A"

# ==================================================
# 5. COMMON LIST METHODS
# ==================================================
cart = ["apple", "banana"]
cart.append("cherry")          # add one item at end
print("append:", cart)

cart.extend(["date", "elderberry"])  # add many items
print("extend:", cart)

cart.insert(1, "apricot")      # insert at index
print("insert:", cart)

cart.remove("banana")          # remove first matching value
print("remove:", cart)

last_item = cart.pop()         # remove and return last
print("pop last:", last_item, cart)

second = cart.pop(1)           # remove and return by index
print("pop index:", second, cart)

print("index of apple:", cart.index("apple"))
print("count cherry:", ["a", "b", "a"].count("a"))

scores = [50, 30, 40, 10, 20]
scores.sort()                  # sorts in place
print("sorted:", scores)
scores.reverse()
print("reversed:", scores)

copy_scores = scores.copy()    # shallow copy
print("copy:", copy_scores)

# clear
temp = [1, 2, 3]
temp.clear()
print("cleared:", temp)

# ==================================================
# 6. LOOPING LISTS + BUILT-INS
# ==================================================
prices = [10, 25, 15, 40]
total = 0
for price in prices:
    total += price
print("Total:", total)
print("sum():", sum(prices))
print("min():", min(prices), "max():", max(prices))
print("len():", len(prices))

# membership
print(25 in prices)

# ==================================================
# 7. LIST ASSIGNMENT VS COPY
# ==================================================
a = [1, 2, 3]
b = a            # same object
c = a.copy()     # new list
b.append(4)
print("a after b.append:", a)   # [1, 2, 3, 4]
print("c unchanged:", c)        # [1, 2, 3]

# ==================================================
# 8. LIST COMPREHENSION (INTRO)
# ==================================================
squares = [x ** 2 for x in range(1, 6)]
print("squares:", squares)

evens = [n for n in range(1, 11) if n % 2 == 0]
print("evens:", evens)

# ==================================================
# 9. TUPLES — ORDERED & IMMUTABLE
# ==================================================
point = (10, 20)
mixed_tuple = (10, "Python", 3.14, True)
single = (5,)          # comma REQUIRED for one-element tuple
not_tuple = (5)        # this is just int 5
print(type(single), type(not_tuple))

print(point[0], point[-1])
# point[0] = 99  # TypeError if uncommented

# packing / unpacking
person = ("Ada", 36, "Engineer")
name, age, job = person
print(name, age, job)

# conversion
as_list = list(point)
as_tuple = tuple([1, 2, 3])
print(as_list, as_tuple)

print((1, 2, 1).count(1))
print((10, 20, 30).index(20))

# ==================================================
# 10. DICTIONARIES — KEY → VALUE
# ==================================================
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics"],
}

print(student["name"])
print(student.get("email", "N/A"))   # safe access with default

student["city"] = "Mumbai"           # add
student["grade"] = "A+"              # update
print(student)

# remove
removed_age = student.pop("age")
print("removed age:", removed_age)

print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))

# loop
for key, value in student.items():
    print(f"{key} -> {value}")

# update merge
student.update({"hobby": "Reading"})
print(student)

# nested dict
company = {
    "emp1": {"name": "John", "role": "Manager"},
    "emp2": {"name": "Alice", "role": "Dev"},
}
print(company["emp1"]["role"])

# dict comprehension
cubes = {n: n ** 3 for n in range(1, 6)}
print("cubes:", cubes)

# ==================================================
# 11. SETS — UNIQUE & UNORDERED
# ==================================================
tags = {"python", "java", "python", "c"}
print(tags)  # duplicates removed

tags.add("go")
tags.update(["rust", "python"])
print(tags)

tags.discard("java")   # no error if missing
# tags.remove("missing")  # KeyError if missing

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("union:", A | B)                 # or A.union(B)
print("intersection:", A & B)          # or A.intersection(B)
print("difference A-B:", A - B)        # or A.difference(B)
print("symmetric diff:", A ^ B)        # or A.symmetric_difference(B)

print({1, 2}.issubset(A))
print(A.issuperset({1, 2}))

# unique values from list
raw = [1, 2, 2, 3, 3, 3]
unique = list(set(raw))  # order not guaranteed
print("unique:", unique)

# ordered unique (common pattern)
ordered_unique = []
for item in raw:
    if item not in ordered_unique:
        ordered_unique.append(item)
print("ordered unique:", ordered_unique)

# set comprehension
even_set = {n for n in range(1, 11) if n % 2 == 0}
print(even_set)

# ==================================================
# 12. WHEN TO USE WHICH?
# ==================================================
# list  → ordered collection you will change (cart, scores)
# tuple → fixed record (x,y), return multiple values, dict keys if needed
# dict  → labeled data / lookups by key (user profile, JSON-like)
# set   → uniqueness, membership tests, set math

# ==================================================
# 13. COMBINED EXAMPLES
# ==================================================
# Character frequency with dict
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("freq:", freq)

# List of tuples → dict
pairs = [("Ada", 36), ("Alan", 41)]
people = {}
for person_name, person_age in pairs:
    people[person_name] = person_age
print("people:", people)

# Filter unique evens
nums = [1, 2, 2, 3, 4, 4, 5, 6]
unique_evens = {n for n in nums if n % 2 == 0}
print("unique evens:", unique_evens)

# Merge dict values by sum for common keys
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1.copy()
for key, value in d2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
print("merged:", merged)

# ==================================================
# 14. COMMON MISTAKES (commented)
# ==================================================
# fruits[10]                 # IndexError
# student["missing"]         # KeyError — use .get()
# (5) is int, (5,) is tuple
# set_item[0]                # TypeError — sets are not indexed
# confusing append vs extend
# a = b on lists shares the same object

print("\n--- Module 6 collections reference complete ---")
