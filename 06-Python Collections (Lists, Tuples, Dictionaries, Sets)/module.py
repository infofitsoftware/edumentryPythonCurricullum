"""
================================================================================
MODULE 6 — Python Collections (Lists, Tuples, Dictionaries, Sets)
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 5 (control flow)
Next:     Module 7 (functions)
================================================================================
"""

print("=== Module 6: Python Collections ===")

# --------------------------------------------------
# 1) Lists — create, index, slice
# --------------------------------------------------
empty_list = []
scores = [85, 90, 78, 92]
mixed = [10, "Python", 3.14, True]
nested = [[1, 2], ["a", "b"]]
print(scores)
print(mixed)
print(nested)

numbers = [10, 20, 30, 40, 50]
print(numbers[0])       # 10
print(numbers[-1])      # 50
print(numbers[1:4])     # [20, 30, 40]
print(numbers[:3])      # [10, 20, 30]
print(numbers[::2])     # [10, 30, 50]
print(numbers[::-1])    # reverse copy

# --------------------------------------------------
# 2) Lists are mutable
# --------------------------------------------------
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)           # ['apple', 'blueberry', 'cherry']

# --------------------------------------------------
# 3) List methods — append vs extend is an AI trap
# --------------------------------------------------
cart = ["apple", "banana"]
cart.append("cherry")
print("append:", cart)

cart.extend(["date", "elderberry"])
print("extend:", cart)

# Contrast append(list) vs extend(list)
demo_a = [1]
demo_a.append([2, 3])
print("append list:", demo_a)   # [1, [2, 3]]

demo_b = [1]
demo_b.extend([2, 3])
print("extend list:", demo_b)   # [1, 2, 3]

cart.insert(1, "apricot")
print("insert:", cart)

cart.remove("banana")
print("remove:", cart)

last_item = cart.pop()
print("pop last:", last_item, cart)

second = cart.pop(1)
print("pop index:", second, cart)

print("index of apple:", cart.index("apple"))
print("count a:", ["a", "b", "a"].count("a"))

scores = [50, 30, 40, 10, 20]
scores.sort()
print("sorted:", scores)
scores.reverse()
print("reversed:", scores)

copy_scores = scores.copy()
print("copy:", copy_scores)

temp = [1, 2, 3]
temp.clear()
print("cleared:", temp)

# --------------------------------------------------
# 4) Looping + built-ins
# --------------------------------------------------
prices = [10, 25, 15, 40]
total = 0
for price in prices:
    total += price
print("Total:", total)
print("sum():", sum(prices))
print("min/max:", min(prices), max(prices))
print("len():", len(prices))
print(25 in prices)

# --------------------------------------------------
# 5) Assignment vs copy (aliasing)
# --------------------------------------------------
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print("a after b.append:", a)   # [1, 2, 3, 4]
print("c unchanged:", c)        # [1, 2, 3]
print("a is b:", a is b)
print("a is c:", a is c)

# --------------------------------------------------
# 6) List comprehension (intro)
# --------------------------------------------------
squares = [x ** 2 for x in range(1, 6)]
print("squares:", squares)
evens = [n for n in range(1, 11) if n % 2 == 0]
print("evens:", evens)

# --------------------------------------------------
# 7) Tuples — immutable + unpacking
# --------------------------------------------------
point = (10, 20)
mixed_tuple = (10, "Python", 3.14, True)
single = (5,)
not_tuple = (5)
print(type(single), type(not_tuple))

print(point[0], point[-1])
# point[0] = 99  # TypeError if uncommented

person = ("Ada", 36, "Engineer")
name, age, job = person
print(name, age, job)

as_list = list(point)
as_tuple = tuple([1, 2, 3])
print(as_list, as_tuple)
print((1, 2, 1).count(1))
print((10, 20, 30).index(20))

# --------------------------------------------------
# 8) Dictionaries — key → value
# --------------------------------------------------
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics"],
}

print(student["name"])
print(student.get("email", "N/A"))

student["city"] = "Mumbai"
student["grade"] = "A+"
print(student)

removed_age = student.pop("age")
print("removed age:", removed_age)

print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))

for key, value in student.items():
    print(f"{key} -> {value}")

student.update({"hobby": "Reading"})
print(student)

company = {
    "emp1": {"name": "John", "role": "Manager"},
    "emp2": {"name": "Alice", "role": "Dev"},
}
print(company["emp1"]["role"])

cubes = {n: n ** 3 for n in range(1, 6)}
print("cubes:", cubes)

# --------------------------------------------------
# 9) Sets — unique + operations
# --------------------------------------------------
tags = {"python", "java", "python", "c"}
print(tags)

tags.add("go")
tags.update(["rust", "python"])
print(tags)

tags.discard("java")
# tags.remove("missing")  # KeyError if missing

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("union:", A | B)
print("intersection:", A & B)
print("difference A-B:", A - B)
print("symmetric diff:", A ^ B)
print({1, 2}.issubset(A))
print(A.issuperset({1, 2}))

raw = [1, 2, 2, 3, 3, 3]
unique = list(set(raw))
print("unique:", unique)

ordered_unique = []
for item in raw:
    if item not in ordered_unique:
        ordered_unique.append(item)
print("ordered unique:", ordered_unique)

even_set = {n for n in range(1, 11) if n % 2 == 0}
print(even_set)

# --------------------------------------------------
# 10) Combined patterns
# --------------------------------------------------
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("freq:", freq)

pairs = [("Ada", 36), ("Alan", 41)]
people = {}
for person_name, person_age in pairs:
    people[person_name] = person_age
print("people:", people)

nums = [1, 2, 2, 3, 4, 4, 5, 6]
unique_evens = {n for n in nums if n % 2 == 0}
print("unique evens:", unique_evens)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1.copy()
for key, value in d2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
print("merged:", merged)

# --------------------------------------------------
# 11) AI-era preview
# --------------------------------------------------
user = {"id": 7, "name": "Ada", "role": "admin"}
print("email:", user.get("email", "missing"))

raw_tags = ["ai", "python", "AI", "python"]
clean_tags = {t.strip().lower() for t in raw_tags}
print("clean tags:", clean_tags)

prompts = ["  summarize  ", "", "  write title  "]
ready = []
for p in prompts:
    clean = p.strip()
    if clean != "":
        ready.append(clean)
print("ready prompts:", ready)

# --------------------------------------------------
# 12) Common mistakes (commented)
# --------------------------------------------------
# fruits[10]              # IndexError
# student["missing"]      # KeyError — use .get()
# (5) is int; (5,) is tuple
# tags[0]                 # TypeError — sets not indexed
# append vs extend
# a = b on lists shares the same object

print("\n--- Module 6 complete. Open module_exercises.md and practice. ---")
