# Module 6 — Practice Exercises: Collections

**Instructions:** Attempt before opening the Instructor Solution Guide. Use Modules 1–6.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Sum a List

**Difficulty:** Easy  
**Concepts:** list, loop or `sum`  

**Problem:** Create a list of five integers. Print the sum of all elements.

**Example Input:** (none — hard-code `[2, 4, 6, 8, 10]`)

**Expected Output:**
```
30
```

**Hint:** `sum(numbers)` or an accumulator loop.

---

### Exercise 2 — Min and Max

**Difficulty:** Easy  
**Concepts:** list, `min`, `max`  

**Problem:** Given `nums = [4, 9, 1, 7, 3]`, print the largest and smallest numbers on two lines.

**Expected Output:**
```
9
1
```

**Hint:** `max(nums)` and `min(nums)`.

---

### Exercise 3 — Loop a Tuple

**Difficulty:** Easy  
**Concepts:** tuple, for  

**Problem:** Create a tuple with five elements and print each element on its own line using a loop.

**Example:** `("a", "b", "c", "d", "e")`

**Expected Output:**
```
a
b
c
d
e
```

**Hint:** `for item in my_tuple:`

---

### Exercise 4 — List ↔ Tuple Conversion

**Difficulty:** Easy  
**Concepts:** `list()`, `tuple()`  

**Problem:** Start with `data = [1, 2, 3]`. Convert to a tuple and print it. Convert that tuple back to a list and print it.

**Expected Output:**
```
(1, 2, 3)
[1, 2, 3]
```

**Hint:** `tuple(data)`, then `list(...)`.

---

### Exercise 5 — Membership in a Set

**Difficulty:** Easy  
**Concepts:** set, `in`  

**Problem:** Create a set `{10, 20, 30, 40}`. Ask the user for a number and print `Found` or `Not found`.

**Example Input:**
```
20
```

**Expected Output:**
```
Found
```

**Hint:** `if value in my_set:`

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Ordered Unique List

**Difficulty:** Medium  
**Concepts:** list, membership  

**Problem:** From `[1, 2, 2, 3, 1, 4, 3]`, remove duplicates **while keeping first-seen order**. Print the result.

**Expected Output:**
```
[1, 2, 3, 4]
```

**Hint:** Build a new list; append only if `item not in new_list`. (`set` alone may change order.)

---

### Exercise 7 — Merge Sets

**Difficulty:** Easy  
**Concepts:** set union  

**Problem:** Merge `{1, 2, 3}` and `{3, 4, 5}` and print the union.

**Expected Output:** (order may vary)
```
{1, 2, 3, 4, 5}
```

**Hint:** `A | B` or `A.union(B)`.

---

### Exercise 8 — Dict Keys and Values

**Difficulty:** Easy  
**Concepts:** dict  

**Problem:** Create a dictionary with three key-value pairs. Print all keys, then all values (each collection on its own line is fine).

**Example dict:** `{"name": "Ada", "age": 36, "job": "Engineer"}`

**Hint:** `.keys()`, `.values()` or loop `.items()`.

---

### Exercise 9 — Character Frequency

**Difficulty:** Medium  
**Concepts:** dict, strings, loop  

**Problem:** Ask for a string. Count occurrences of each character into a dictionary and print it.

**Example Input:**
```
banana
```

**Expected Output:**
```
{'b': 1, 'a': 3, 'n': 2}
```

**Hint:** `freq[char] = freq.get(char, 0) + 1`

---

### Exercise 10 — Safe get()

**Difficulty:** Easy  
**Concepts:** `dict.get`  

**Problem:** For `user = {"name": "Sam", "role": "admin"}`, print the email using `.get()` with default `"missing"`.

**Expected Output:**
```
missing
```

**Hint:** `user.get("email", "missing")`

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — Second Largest

**Difficulty:** Medium  
**Concepts:** list, sorting or logic  

**Problem:** Find the second largest number in `[5, 1, 9, 9, 3, 7]` (treat unique values: second largest is 7).

**Expected Output:**
```
7
```

**Hint:** Convert to unique values, sort, pick second from end.

---

### Exercise 12 — Word Lengths Dict

**Difficulty:** Medium  
**Concepts:** list, dict comprehension or loop  

**Problem:** Given `words = ["python", "is", "fun"]`, create a dict of word → length and print it.

**Expected Output:**
```
{'python': 6, 'is': 2, 'fun': 3}
```

**Hint:** `{w: len(w) for w in words}`

---

### Exercise 13 — Sum Even Tuple Values

**Difficulty:** Medium  
**Concepts:** tuple, for, `%`  

**Problem:** Given `nums = (2, 5, 8, 3, 10)`, print the sum of even numbers.

**Expected Output:**
```
20
```

**Hint:** Accumulate when `n % 2 == 0`.

---

### Exercise 14 — Subset Check

**Difficulty:** Easy  
**Concepts:** set  

**Problem:** Check whether `{1, 2}` is a subset of `{1, 2, 3, 4}`. Print `True` or `False`.

**Expected Output:**
```
True
```

**Hint:** `.issubset()` or `<=`.

---

### Exercise 15 — Intersection

**Difficulty:** Easy  
**Concepts:** set  

**Problem:** Print the intersection of `{1, 2, 3, 4}` and `{3, 4, 5, 6}`.

**Expected Output:** (order may vary)
```
{3, 4}
```

**Hint:** `A & B`

---

### Exercise 16 — Merge Dicts Summing Common Keys

**Difficulty:** Challenging  
**Concepts:** dict, loop  

**Problem:** Merge `{"a": 1, "b": 2}` and `{"b": 3, "c": 4}` so common keys sum values.

**Expected Output:**
```
{'a': 1, 'b': 5, 'c': 4}
```

**Hint:** Copy first dict; for each key in second, add or insert.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Cubes Dictionary

**Difficulty:** Medium  
**Concepts:** dict comprehension / loop  

**Problem:** Create a dictionary for numbers 1 to 10 where value is the cube. Print the dict.

**Expected Output:** (keys 1..10, values 1, 8, 27, …, 1000)

**Hint:** `{n: n**3 for n in range(1, 11)}`

---

### Exercise 18 — Unique Even Set

**Difficulty:** Medium  
**Concepts:** list, set, filter  

**Problem:** From `[1, 2, 2, 3, 4, 4, 5, 6, 6]`, create a set of unique even numbers and print it.

**Expected Output:** (order may vary)
```
{2, 4, 6}
```

**Hint:** `{n for n in nums if n % 2 == 0}`

---

### Exercise 19 — Sort Dict by Values Descending

**Difficulty:** Challenging  
**Concepts:** dict, `sorted`  

**Problem:** Given `scores = {"Ada": 90, "Bob": 75, "Cam": 95}`, print a list of `(name, score)` pairs sorted by score descending.

**Expected Output:**
```
[('Cam', 95), ('Ada', 90), ('Bob', 75)]
```

**Hint:** `sorted(scores.items(), key=lambda item: item[1], reverse=True)`  
(If lambda is new: build a list of tuples and sort carefully; instructor may demo `key=`.)

---

### Exercise 20 — Tuples List to Dictionary

**Difficulty:** Medium  
**Concepts:** list of tuples, dict  

**Problem:** Convert `[("Ada", 36), ("Alan", 41), ("Grace", 45)]` into a dictionary name → age and print it.

**Expected Output:**
```
{'Ada': 36, 'Alan': 41, 'Grace': 45}
```

**Hint:** Loop pairs and assign `d[name] = age`, or `dict(pairs)`.

---

# Instructor Solution Guide

```python
# Exercise 1
numbers = [2, 4, 6, 8, 10]
print(sum(numbers))

# Exercise 2
nums = [4, 9, 1, 7, 3]
print(max(nums))
print(min(nums))

# Exercise 3
items = ("a", "b", "c", "d", "e")
for item in items:
    print(item)

# Exercise 4
data = [1, 2, 3]
t = tuple(data)
print(t)
print(list(t))

# Exercise 5
values = {10, 20, 30, 40}
n = int(input("Number: "))
if n in values:
    print("Found")
else:
    print("Not found")

# Exercise 6
raw = [1, 2, 2, 3, 1, 4, 3]
unique = []
for item in raw:
    if item not in unique:
        unique.append(item)
print(unique)

# Exercise 7
print({1, 2, 3} | {3, 4, 5})

# Exercise 8
person = {"name": "Ada", "age": 36, "job": "Engineer"}
print(list(person.keys()))
print(list(person.values()))

# Exercise 9
text = input("Text: ")
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# Exercise 10
user = {"name": "Sam", "role": "admin"}
print(user.get("email", "missing"))

# Exercise 11
nums = [5, 1, 9, 9, 3, 7]
unique_sorted = sorted(set(nums))
print(unique_sorted[-2])

# Exercise 12
words = ["python", "is", "fun"]
print({w: len(w) for w in words})

# Exercise 13
nums = (2, 5, 8, 3, 10)
total = 0
for n in nums:
    if n % 2 == 0:
        total += n
print(total)

# Exercise 14
print({1, 2}.issubset({1, 2, 3, 4}))

# Exercise 15
print({1, 2, 3, 4} & {3, 4, 5, 6})

# Exercise 16
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1.copy()
for key, value in d2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
print(merged)

# Exercise 17
print({n: n ** 3 for n in range(1, 11)})

# Exercise 18
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print({n for n in nums if n % 2 == 0})

# Exercise 19
scores = {"Ada": 90, "Bob": 75, "Cam": 95}
print(sorted(scores.items(), key=lambda item: item[1], reverse=True))

# Exercise 20
pairs = [("Ada", 36), ("Alan", 41), ("Grace", 45)]
print(dict(pairs))
```
