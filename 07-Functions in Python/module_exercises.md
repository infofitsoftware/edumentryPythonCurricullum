# Module 7 — Practice Exercises: Functions in Python

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises below in order  
4. Predict output before running  
5. If you use AI, explain every line yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Use Modules 1–7. For each function: **define it**, then **call it** and print the result.

---

## A. Define, call, return

### A1. [E] say_hello
Write `say_hello()` that prints `Hello, World!`.

### A2. [E] add
Write `add(a, b)` that **returns** the sum. Print `add(3, 5)`.

Expected: `8`

### A3. [E] string_length
Write `string_length(text)` that returns `len(text)`. Test with `"Python"`.

Expected: `6`

### A4. [E] even_or_odd
Write `even_or_odd(n)` that returns `"Even"` or `"Odd"`. Test with `7`.

Expected: `Odd`

### A5. [M] print vs return bug
```python
def square(n):
    print(n * n)

value = square(4)
print(value)
```
Predict both lines. Then rewrite `square` so `value` becomes `16`.

### A6. [M] min_max
Write `min_max(values)` that returns both min and max. Unpack and print for `[4, 9, 1, 7]`.

---

## B. Arguments: positional, default, keyword

### B1. [E] greet with default
Write `greet(name="Guest")` that prints `Hello, <name>!`.  
Call it once with no argument and once with `"Ada"`.

### B2. [E] power
Write `power(base, exponent=2)` that returns `base ** exponent`.  
Print `power(5)` and `power(5, 3)`.

Expected:
```
25
125
```

### B3. [M] describe_pet
Write `describe_pet(animal, name)` that prints `<name> is a <animal>.`  
Call it with keywords in both orders.

### B4. [M] keyword mix
Call `describe_pet("fish", name="Nemo")`. Write a comment: why positional must come before keywords.

### B5. [C] AI bug: default before required
An AI wrote:
```python
def bad(a=1, b):
    return a + b
```
What error occurs? Rewrite it correctly.

---

## C. *args, **kwargs, scope

### C1. [E] add_numbers
Write `add_numbers(*args)` that returns the sum of all arguments.  
Test with `1, 2, 3, 4`.

### C2. [M] describe_person
Write `describe_person(**kwargs)` that prints each `key: value`.  
Call with `name="Alice", age=25`.

### C3. [M] make_profile
Write a function that accepts `name`, `age`, optional hobbies via `*args`,  
default `city="Unknown"`, and extra fields via `**kwargs`. Return a dict and print it.

### C4. [M] local vs global
```python
counter = 0

def bump():
    counter = 10
    print(counter)

bump()
print(counter)
```
Predict both lines. Write a comment explaining why the global stayed `0`.

---

## D. Functions + prior modules

### D1. [E] largest
Write `largest(numbers)` that returns the largest element. Test with `[4, 9, 1, 7]`.

### D2. [E] is_even
Write `is_even(n)` returning `True`/`False`. Test with `8` and `7`.

### D3. [M] even_only
Write `even_only(numbers)` that returns a new list of even numbers only.  
Test with `[1, 2, 3, 4, 5, 6]`.

### D4. [M] factorial
Write `factorial(n)` returning `n!` (`0! = 1`). Test with `5`.

Expected: `120`

### D5. [M] char_frequency
Write `char_frequency(text)` returning a frequency dict. Test with `"banana"`.

### D6. [M] is_palindrome
Write `is_palindrome(text)` that ignores case and spaces.  
Test with `"Race car"` → `True`.

### D7. [C] average
Write `average(numbers)` that returns the mean as a float.  
If the list is empty, return `None`. Test with `[2, 4, 6]`.

---

## E. Real-world / AI-era helpers

### E1. [M] clean_email
Write `clean_email(raw)` that returns stripped lowercase email.  
Test with `"  Student@Example.COM  "`.

### E2. [M] is_admin
Write `is_admin(role)` that returns whether cleaned role equals `"admin"`.

### E3. [M] build_prompt
Write `build_prompt(task, text)` that returns:
```
Task: <task>
Text: <stripped text>
```

### E4. [M] celsius_to_fahrenheit
Write the conversion function with a docstring. Test with `25`.

### E5. [C] mutable default fix
Show the bug:
```python
def add_item(item, bag=[]):
    bag.append(item)
    return bag
```
Call it twice with `"a"` then `"b"`. Then rewrite the safe `bag=None` version.

### E6. [C] ready_prompts
Write `ready_prompts(prompts)` that takes a list of strings,  
strips each, skips empties, and returns the cleaned list.

---

## F. Lambda / recursion (optional stretch)

### F1. [M] lambda cube
Create `cube = lambda x: x ** 3` and print `cube(3)`.

### F2. [M] sorted by score
Given `pairs = [("Ada", 90), ("Bob", 75)]`, print them sorted by score ascending using `lambda`.

### F3. [C] fibonacci
Write recursive `fibonacci(n)` and print `fibonacci(6)`.

Expected: `8`

---

## G. Short written answers (as comments)

### G1. Parameter vs argument?
Answer:

### G2. Why prefer return over print inside helper functions?
Answer:

### G3. Why is a mutable default dangerous?
Answer:

### G4. When is a lambda a good idea vs a bad idea?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.
