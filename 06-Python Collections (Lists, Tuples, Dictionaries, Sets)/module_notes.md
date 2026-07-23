# Module 6 — Python Collections

**Course:** Utrains Python Fundamentals  
**Topics:** Lists, Tuples, Dictionaries, Sets  
**Prerequisites:** Modules 1–5  
**Next:** Module 7 — Functions

---

# Slide 1 — Title

## Python Collections

**Problem:** one variable → one value.  
**Need:** carts, scores, configs, unique IDs, labeled records.

Today’s tools:

```
list   tuple   dict   set
```

---

# Slide 2 — Learning Objectives

1. Create and modify **lists**  
2. Use list methods and loop/aggregate lists  
3. Use **tuples** (immutability, unpacking)  
4. Build and query **dictionaries** safely  
5. Use **sets** for uniqueness and set operations  
6. Choose the right collection for a task  
7. Combine collections with loops and conditions  

---

# Slide 3 — WHY Collections? (Motivation)

| Scenario | Best fit |
|----------|----------|
| Shopping cart items | list |
| GPS coordinate (x, y) | tuple |
| Student profile fields | dict |
| Unique tags / IDs | set |

**Career links:** JSON APIs → dicts; data rows → lists of dicts; dedupe → sets.

---

# Slide 4 — Comparison Table

| | list | tuple | dict | set |
|--|------|-------|------|-----|
| Syntax | `[ ]` | `( )` | `{k: v}` | `{ }` |
| Ordered | Yes | Yes | Yes (3.7+) | No |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | Keys unique | No |
| Access | index | index | key | membership |

---

# Slide 5 — Lists: WHAT & CREATE

A **list** is an ordered, changeable collection.

```python
scores = [85, 90, 78]
mixed = [10, "Python", True]
nested = [[1, 2], [3, 4]]
empty = []
```

**Analogy:** a grocery list you can rewrite.

---

# Slide 6 — Indexing & Slicing

Same idea as strings (Module 3):

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])     # 10
print(numbers[-1])    # 50
print(numbers[1:4])   # [20, 30, 40]
print(numbers[::2])   # [10, 30, 50]
```

**Ask:** What is `numbers[0:2]`?

---

# Slide 7 — Mutability (List vs String)

```python
fruits = ["apple", "banana"]
fruits[1] = "blueberry"   # OK

# text = "apple"
# text[0] = "A"           # TypeError
```

Lists are **mutable**. Strings are not.

---

# Slide 8 — Essential List Methods

```python
cart.append("milk")       # add one
cart.extend(["eggs", "bread"])
cart.insert(0, "butter")
cart.remove("eggs")       # by value
item = cart.pop()         # by index (default last)
cart.sort()
cart.reverse()
cart.copy()
```

**Common mix-up:**

- `append([1,2])` adds the whole list as **one** element  
- `extend([1,2])` adds **each** element  

---

# Slide 9 — Looping & Aggregates

```python
prices = [10, 25, 15]
total = 0
for price in prices:
    total += price
```

Shortcuts:

```python
sum(prices), min(prices), max(prices), len(prices)
25 in prices
```

---

# Slide 10 — Trace: Assignment vs Copy

```python
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
```

| Name | Value after |
|------|-------------|
| a | [1, 2, 3, 4] |
| b | same object as a |
| c | [1, 2, 3] |

**Rule:** `b = a` aliases; use `.copy()` for a separate list.

---

# Slide 11 — List Comprehension (Intro)

```python
squares = [x ** 2 for x in range(1, 6)]
evens = [n for n in range(1, 11) if n % 2 == 0]
```

Read as: “make a new list from each x in … (optionally if …)”

Useful, not mandatory on day one — still learn the `for` form first.

---

# Slide 12 — Tuples: WHY & WHAT

**Tuple** = ordered, **immutable** sequence.

```python
point = (10, 20)
person = ("Ada", 36, "Engineer")
single = (5,)     # comma required!
```

**Why exist?** Fixed records, safer “don’t change this”, multiple return values later (Module 7).

---

# Slide 13 — Tuple Unpacking & Conversion

```python
name, age, job = ("Ada", 36, "Engineer")
as_list = list(point)
as_tuple = tuple([1, 2, 3])
```

```python
# point[0] = 99  → TypeError
```

**Ask:** Is `(5)` a tuple? (No — it’s int. Need `(5,)`.)

---

# Slide 14 — Dictionaries: WHY

Store **labeled** data:

```python
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
}
```

**Analogy:** a labeled form, not a numbered queue.

Keys must be unique and immutable (strings/numbers/tuples).

---

# Slide 15 — Dict Access & Update

```python
print(student["name"])
print(student.get("email", "N/A"))  # safe

student["city"] = "Mumbai"   # add
student["grade"] = "A+"      # update
student.pop("age")           # remove key
```

**Mistake:** `student["missing"]` → `KeyError`  
**Fix:** `.get()`

---

# Slide 16 — Dict Loop & Nested

```python
for key, value in student.items():
    print(key, value)
```

```python
company = {
    "emp1": {"name": "John", "role": "Manager"}
}
print(company["emp1"]["role"])
```

JSON from APIs often looks like nested dicts/lists.

---

# Slide 17 — Dict Trace: Frequency Counter

```python
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
# {'b': 1, 'a': 3, 'n': 2}
```

**Trace ‘a’:** first time 0+1 → 1; later increments.

Classic interview-friendly pattern.

---

# Slide 18 — Sets: WHY & WHAT

**Set** = unordered collection of **unique** items.

```python
tags = {"python", "java", "python"}
print(tags)  # duplicates gone
```

Great for: dedupe, “is X allowed?”, math-like operations.

**Cannot** index: no `tags[0]`.

---

# Slide 19 — Set Operations

```python
A = {1, 2, 3}
B = {3, 4, 5}
A | B   # union
A & B   # intersection
A - B   # difference
A ^ B   # symmetric difference
```

```python
tags.add("go")
tags.discard("java")  # safe if missing
```

---

# Slide 20 — Choosing the Right Tool

```
Need order + edits          → list
Need fixed record           → tuple
Need label → value lookup   → dict
Need uniqueness / set math  → set
```

**Mini challenge:** shopping cart? user settings? unique IPs in a log?

---

# Slide 21 — Combined Patterns

1. `list` of scores → `sum` / `max`  
2. `dict` frequency of characters  
3. `set` unique evens from a list  
4. list of `(name, age)` tuples → dict  

These patterns appear in data cleaning and backend payloads.

---

# Slide 22 — Common Mistakes

1. `IndexError` / `KeyError`  
2. `(5)` vs `(5,)`  
3. `append` vs `extend`  
4. `b = a` shared list reference  
5. Indexing a set  
6. Assuming set order  
7. Mutating a tuple  

---

# Slide 23 — Professional Connection

| Domain | Collection use |
|--------|----------------|
| Backend | request JSON → dict |
| Data | columns/rows as lists/dicts |
| Automation | set of processed file names |
| DevOps | inventory lists, tag sets |
| AI | batches of samples in lists |

---

# Slide 24 — Concept Recap

- list: ordered, mutable  
- tuple: ordered, immutable  
- dict: key → value  
- set: unique membership  
- methods + loops + comprehensions (intro)  

---

# Slide 25 — Syntax Cheat Sheet

```python
L = [1, 2]; L.append(3); L[0]
T = (1, 2); a, b = T
D = {"a": 1}; D.get("a"); D["b"] = 2
S = {1, 2}; S.add(3); S & {2, 4}
[x*2 for x in L]
```

---

# Slide 26 — Mistakes Checklist

- [ ] Right collection type chosen?  
- [ ] Used `.get()` for uncertain keys?  
- [ ] Copied list when needed?  
- [ ] Tuple single-element comma?  
- [ ] No indexing on sets?  

---

# Slide 27 — “Can You Explain This?”

1. list vs tuple?  
2. `append` vs `extend`?  
3. Why `dict.get`?  
4. Why sets remove duplicates?  
5. `b = a` vs `b = a.copy()`?  

---

# Slide 28 — Mini Challenges

1. Second-largest in a list  
2. Char frequency dict  
3. Intersection of two sets  
4. Convert list of pairs to dict  

---

# Slide 29 — What You Can Do Now

- Store and process multiple values  
- Model records with dicts  
- Deduplicate with sets  
- Unpack tuples  
- Combine collections with loops  

---

# Slide 30 — Next Module

**Module 7 — Functions**  
Package collection logic into reusable blocks (`def`), return tuples/dicts, and pass lists as arguments.

---

# Slide 31 — Lab Directions

1. Run `module.py`  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 6 teaching slides*
