# Module 6 — Practice Exercises: Python Collections

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use Modules 1–6.

---

## A. Lists

### A1. [E] Sum a list
Create `[2, 4, 6, 8, 10]` and print the sum.

Expected: `30`

### A2. [E] Min and max
Given `nums = [4, 9, 1, 7, 3]`, print the largest then the smallest.

Expected:
```
9
1
```

### A3. [E] Index and slice
Given `numbers = [10, 20, 30, 40, 50]`, print first item, last item, and `numbers[1:4]`.

### A4. [E] Mutate
Start with `fruits = ["apple", "banana", "cherry"]`. Change index 1 to `"blueberry"` and print the list.

### A5. [M] append vs extend
Predict both results, then run:

```python
a = [1]
a.append([2, 3])
print(a)

b = [1]
b.extend([2, 3])
print(b)
```

Write a comment explaining the difference.

### A6. [M] Cart methods
Start `cart = ["apple"]`.  
`append("milk")`, `extend(["eggs", "bread"])`, `insert(0, "butter")`, then `pop()` once.  
Print the final cart.

### A7. [M] Assignment vs copy
```python
a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(a)
print(c)
```
Predict both lines. Write a comment about aliasing.

### A8. [C] Second largest
Given `nums = [4, 9, 1, 7, 3]`, print the second-largest value  
(do not hard-code `7` — compute it).

---

## B. Tuples

### B1. [E] Loop a tuple
Create `("a", "b", "c", "d", "e")` and print each element on its own line.

### B2. [E] Conversion
Start with `data = [1, 2, 3]`. Convert to tuple, print it, convert back to list, print it.

### B3. [E] Unpacking
```python
person = ("Ada", 36, "Engineer")
```
Unpack into `name`, `age`, `job` and print each.

### B4. [M] Single-element trap
Print `type((5))` and `type((5,))`. Write a comment explaining the difference.

### B5. [M] Immutability check
```python
point = (10, 20)
# point[0] = 99
```
Predict what happens if you uncomment the second line. Write the error name in a comment.

---

## C. Dictionaries

### C1. [E] Create and access
Create a student dict with `name`, `age`, `grade`. Print the name.

### C2. [E] Safe get
Using that student dict, print `student.get("email", "N/A")`.

### C3. [E] Add and update
Add `"city": "Mumbai"` and change `grade` to `"A+"`. Print the dict.

### C4. [M] Loop items
Loop with `.items()` and print `key -> value` for each pair.

### C5. [M] Nested dict
```python
company = {
    "emp1": {"name": "John", "role": "Manager"},
    "emp2": {"name": "Alice", "role": "Dev"},
}
```
Print emp1’s role.

### C6. [M] Frequency counter
Count character frequency in `"banana"` using a dict and `.get`. Print the dict.

Expected shape: `{'b': 1, 'a': 3, 'n': 2}` (order may vary by Python version display, values matter).

### C7. [C] AI bug: KeyError
An AI wrote:
```python
user = {"name": "Ada"}
print(user["email"])
```
Show why this fails, then fix it with `.get`.

---

## D. Sets

### D1. [E] Dedupe print
Create `{"python", "java", "python", "c"}` and print it (duplicates gone).

### D2. [E] Membership
Create `{10, 20, 30, 40}`. Ask for a number; print `Found` or `Not found`.

### D3. [M] Set operations
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```
Print union, intersection, and `A - B`.

### D4. [M] Unique from list
From `[1, 2, 2, 3, 3, 3]`, print a unique collection using `set`.

### D5. [M] Ordered unique
From the same list, build an **ordered** unique list with a loop (no relying on set order).

### D6. [C] Clean tags (AI era)
```python
raw_tags = ["ai", "python", "AI", "python", "  Go  "]
```
Produce a set of cleaned lowercase stripped tags and print it.

---

## E. Combined / real-world

### E1. [M] List of pairs → dict
```python
pairs = [("Ada", 36), ("Alan", 41)]
```
Build a dict and print it.

### E2. [M] Unique evens
From `[1, 2, 2, 3, 4, 4, 5, 6]`, print the set of unique even numbers.

### E3. [M] Ready prompts
```python
prompts = ["  summarize  ", "", "  ", "write title"]
```
Build a new list of non-empty stripped prompts and print it.

### E4. [M] Profile + role check
```python
user = {"id": 7, "name": "  Ada  ", "role": "Admin"}
```
Clean name and role. Print whether role equals `"admin"` after cleaning.

### E5. [C] Merge dict values
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
```
Merge into a new dict: shared keys should be summed. Print the result.

Expected: `{'a': 1, 'b': 5, 'c': 4}`

### E6. [C] Mini inventory
Create a list of product dicts:
```python
products = [
    {"name": "pen", "price": 10},
    {"name": "notebook", "price": 40},
    {"name": "pen", "price": 10},
]
```
Print total price of all items, and a set of unique product names.

---

## F. Short written answers (as comments)

### F1. When do you choose a list vs a tuple?
Answer:

### F2. Why is `dict.get` safer than `dict[key]` for optional fields?
Answer:

### F3. Why can’t you reliably use `set` order for a “first seen” unique list?
Answer:

### F4. What collection fits JSON-like API data best, and why?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
