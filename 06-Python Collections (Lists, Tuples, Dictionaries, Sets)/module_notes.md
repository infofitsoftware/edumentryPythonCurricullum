# Module 6 — Python Collections (Lists, Tuples, Dictionaries, Sets)

**For students (beginners)**  
**Prerequisites:** Modules 1–5 (I/O, types, strings, operators, control flow)  
**Next:** Module 7 — Functions  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Create and modify **lists** (index, slice, methods)  
2. Loop and aggregate lists (`sum`, `min`, `max`, counters)  
3. Use **tuples** (immutability, unpacking, `(5,)` trap)  
4. Build and query **dictionaries** safely (`.get`, `.items`)  
5. Use **sets** for uniqueness and set operations  
6. Choose the right collection for a task  
7. Spot AI mistakes: `append` vs `extend`, `b = a` aliasing, `KeyError`, indexing a set  

---

## 2. Why collections matter (AI era)

One variable holds one value. Real programs hold **many** values.

| Place | Collection job |
|-------|----------------|
| FastAPI / APIs | JSON body → **dict**; list of records → **list of dicts** |
| Forms / carts | ordered items → **list** |
| Config / profile | labeled fields → **dict** |
| Logs / tags / IDs | unique values → **set** |
| AI / LLM apps | batches of prompts, messages, scores → **lists** |
| Fixed records | coordinates, RGB, `(lat, lon)` → **tuple** |

**Golden rule:**  
If AI writes collection code for you, check **the type chosen**, **mutating the right object**, and **safe key/index access**. Those hide most bugs.

---

## 3. The four tools at a glance

```
list   tuple   dict   set
```

| | list | tuple | dict | set |
|--|------|-------|------|-----|
| Syntax | `[ ]` | `( )` | `{k: v}` | `{ }` |
| Ordered | Yes | Yes | Yes (3.7+) | No |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | Keys unique | No |
| Access | index | index | key | membership |

Quick chooser:

```
Need order + edits          → list
Need fixed record           → tuple
Need label → value lookup   → dict
Need uniqueness / set math  → set
```

---

## 4. Lists — what and create

A **list** is an ordered, changeable collection.

```python
scores = [85, 90, 78]
mixed = [10, "Python", True]
nested = [[1, 2], [3, 4]]
empty = []
```

Think of a grocery list you can rewrite.

---

## 5. List indexing and slicing

Same idea as strings (Module 3):

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])     # 10
print(numbers[-1])    # 50
print(numbers[1:4])   # [20, 30, 40]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # reversed copy
```

Stop is exclusive: `numbers[0:2]` → `[10, 20]`.

---

## 6. Lists are mutable (unlike strings)

```python
fruits = ["apple", "banana"]
fruits[1] = "blueberry"   # OK
print(fruits)

# text = "apple"
# text[0] = "A"           # TypeError
```

This is a major difference from Module 3 strings.

---

## 7. Essential list methods

```python
cart = ["apple", "banana"]
cart.append("milk")              # add one item at end
cart.extend(["eggs", "bread"])   # add each item
cart.insert(0, "butter")         # insert at index
cart.remove("eggs")              # remove by value (first match)
item = cart.pop()                # remove and return last
cart.sort()
cart.reverse()
copy_cart = cart.copy()
```

**Common mix-up (AI does this too):**

- `append([1, 2])` → adds the whole list as **one** element  
- `extend([1, 2])` → adds **each** element  

```python
a = [1]
a.append([2, 3])   # [1, [2, 3]]
b = [1]
b.extend([2, 3])   # [1, 2, 3]
```

---

## 8. Looping lists and built-ins

```python
prices = [10, 25, 15]
total = 0
for price in prices:
    total += price
print(total)
```

Shortcuts:

```python
print(sum(prices), min(prices), max(prices), len(prices))
print(25 in prices)
```

---

## 9. Trace: assignment vs copy

```python
a = [1, 2, 3]
b = a          # same object (alias)
c = a.copy()   # separate list
b.append(4)
```

| Name | After |
|------|-------|
| `a` | `[1, 2, 3, 4]` |
| `b` | same object as `a` |
| `c` | `[1, 2, 3]` |

**Rule:** `b = a` shares the list. Use `.copy()` when you need a separate list.  
Module 4’s `is` vs `==` idea returns here.

---

## 10. List comprehension (intro only)

```python
squares = [x ** 2 for x in range(1, 6)]
evens = [n for n in range(1, 11) if n % 2 == 0]
```

Read as: “make a new list from each x in … (optionally if …)”

Useful, not mandatory on day one. Master the normal `for` form first.

---

## 11. Tuples — ordered and immutable

```python
point = (10, 20)
person = ("Ada", 36, "Engineer")
single = (5,)     # comma required!
not_tuple = (5)   # this is just int 5
```

**Why tuples exist:**

- fixed records (coordinates, RGB)  
- safer “don’t change this”  
- multiple return values later (Module 7)  

```python
# point[0] = 99  → TypeError
```

### Unpacking and conversion

```python
name, age, job = ("Ada", 36, "Engineer")
as_list = list(point)
as_tuple = tuple([1, 2, 3])
```

---

## 12. Dictionaries — labeled data

A **dict** stores key → value pairs.

```python
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
}
```

Analogy: a labeled form, not a numbered queue.

Keys must be unique and immutable (usually strings/numbers).

### Access and update

```python
print(student["name"])
print(student.get("email", "N/A"))  # safe

student["city"] = "Mumbai"   # add
student["grade"] = "A+"      # update
student.pop("age")           # remove key
```

**Mistake:** `student["missing"]` → `KeyError`  
**Fix:** `.get("missing", default)`

### Loop and nested dicts

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

JSON from APIs often looks like nested dicts and lists of dicts.

### Frequency counter (classic pattern)

```python
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
# {'b': 1, 'a': 3, 'n': 2}
```

Trace for `'a'`: first time `0 + 1 → 1`; later visits increment.

---

## 13. Sets — unique membership

A **set** is an unordered collection of **unique** items.

```python
tags = {"python", "java", "python"}
print(tags)  # duplicates gone
```

Great for: dedupe, “is X allowed?”, math-like operations.

**Cannot** index: no `tags[0]`.

```python
tags.add("go")
tags.discard("java")  # safe if missing
```

### Set operations

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference
print(A ^ B)   # symmetric difference
```

Dedupe a list (order not guaranteed):

```python
raw = [1, 2, 2, 3, 3]
unique = list(set(raw))
```

If you need **order kept**, build a new list carefully:

```python
ordered_unique = []
for item in raw:
    if item not in ordered_unique:
        ordered_unique.append(item)
```

---

## 14. Real-world preview (still beginner level)

### Shopping cart (list)

```python
cart = []
cart.append("milk")
cart.extend(["eggs", "bread"])
print(len(cart), "items")
```

### API-style user profile (dict)

```python
user = {"id": 7, "name": "Ada", "role": "admin"}
print(user.get("email", "missing"))
```

### Unique tags from messy input (set)

```python
raw_tags = ["ai", "python", "AI", "python"]
clean = {t.strip().lower() for t in raw_tags}
print(clean)
```

### Batch of AI prompts (list + cleaning)

```python
prompts = ["  summarize  ", "", "  write title  "]
ready = []
for p in prompts:
    clean = p.strip()
    if clean != "":
        ready.append(clean)
print(ready)
```

You are not building FastAPI today.  
You are learning the exact collection skills those systems need.

---

## 15. Common mistakes checklist

1. `IndexError` on lists / `KeyError` on dicts  
2. `(5)` vs `(5,)` for single-element tuples  
3. `append` vs `extend`  
4. `b = a` shared list reference (forgot `.copy()`)  
5. Trying to index a set  
6. Assuming set order  
7. Mutating a tuple  
8. Shipping AI dict code without `.get()` for optional keys  

---

## 16. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask which collection type fits and **why**  
- Re-type the fix yourself  
- Run and verify  

---

## 17. Mini self-check (before the quiz)

Can you answer these out loud?

1. list vs tuple?  
2. `append` vs `extend`?  
3. Why use `dict.get`?  
4. Why do sets remove duplicates?  
5. `b = a` vs `b = a.copy()`?  
6. Is `(5)` a tuple?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 18. What “confident” means after Module 6

You can:

- store and process multiple values with the right collection  
- model records with dicts  
- deduplicate with sets  
- unpack tuples  
- combine collections with loops and conditions  
- spot AI mistakes around mutation, keys, and type choice  

Next lesson (Module 7) covers **functions** — packaging collection logic into reusable blocks with `def`, returning tuples/dicts, and passing lists as arguments.
