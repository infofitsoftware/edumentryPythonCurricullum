# Module 7 — Practice Exercises: Functions

**Instructions:** Attempt each exercise before opening the Instructor Solution Guide.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Add Two Numbers

**Difficulty:** Easy  
**Concepts:** parameters, return  

**Problem:** Write `add(a, b)` that returns the sum of two numbers. Print `add(3, 5)`.

**Expected Output:**
```
8
```

**Hint:** Use `return a + b`.

---

### Exercise 2 — String Length Function

**Difficulty:** Easy  
**Concepts:** return, `len`  

**Problem:** Write `string_length(text)` that returns the length of a string. Test with `"Python"`.

**Expected Output:**
```
6
```

**Hint:** `return len(text)`

---

### Exercise 3 — Even or Odd

**Difficulty:** Easy  
**Concepts:** return, `%`, if  

**Problem:** Write `even_or_odd(n)` that returns `"Even"` or `"Odd"`. Test with `7`.

**Expected Output:**
```
Odd
```

**Hint:** Return a string, don’t only print inside.

---

### Exercise 4 — Hello World Function

**Difficulty:** Easy  
**Concepts:** define/call  

**Problem:** Write `say_hello()` that prints `Hello, World!` when called.

**Expected Output:**
```
Hello, World!
```

**Hint:** No parameters needed.

---

### Exercise 5 — Largest in List

**Difficulty:** Easy  
**Concepts:** list, return  

**Problem:** Write `largest(numbers)` that returns the largest element. Test with `[4, 9, 1, 7]`.

**Expected Output:**
```
9
```

**Hint:** `return max(numbers)`

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Factorial Function

**Difficulty:** Medium  
**Concepts:** loop, return  

**Problem:** Write `factorial(n)` returning `n!` (`0! = 1`). Test with `5`.

**Expected Output:**
```
120
```

**Hint:** Accumulate a product from 1 to n.

---

### Exercise 7 — Palindrome Check

**Difficulty:** Medium  
**Concepts:** strings, return bool/string  

**Problem:** Write `is_palindrome(text)` that returns `True` if the text is a palindrome ignoring case and spaces. Test `"Race car"`.

**Expected Output:**
```
True
```

**Hint:** Clean with `.lower().replace(" ", "")`, compare to reverse.

---

### Exercise 8 — Greeting with Default

**Difficulty:** Easy  
**Concepts:** default argument  

**Problem:** Write `greet(name="Guest")` that prints `Hello, <name>!`. Call once with no args and once with `"Ada"`.

**Expected Output:**
```
Hello, Guest!
Hello, Ada!
```

**Hint:** Default parameter value.

---

### Exercise 9 — Square Function

**Difficulty:** Easy  
**Concepts:** return  

**Problem:** Write `square(n)` returning `n * n`. Print `square(6)`.

**Expected Output:**
```
36
```

**Hint:** Prefer `return`, then print the result outside.

---

### Exercise 10 — Concatenate Strings

**Difficulty:** Easy  
**Concepts:** return, strings  

**Problem:** Write `concat(a, b)` returning `a + b`. Test `"Hello, "` and `"World"`.

**Expected Output:**
```
Hello, World
```

**Hint:** Return the joined string.

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — Filter Evens

**Difficulty:** Medium  
**Concepts:** list, loop, return  

**Problem:** Write `even_only(numbers)` returning a new list of even numbers from the input list. Test `[1, 2, 3, 4, 5, 6]`.

**Expected Output:**
```
[2, 4, 6]
```

**Hint:** Build a new list inside the function.

---

### Exercise 12 — Character Frequency

**Difficulty:** Medium  
**Concepts:** dict, function  

**Problem:** Write `char_frequency(text)` returning a dict of character counts. Test `"banana"`.

**Expected Output:**
```
{'b': 1, 'a': 3, 'n': 2}
```

**Hint:** Use `.get(char, 0) + 1`.

---

### Exercise 13 — Fibonacci (Recursive or Loop)

**Difficulty:** Challenging  
**Concepts:** recursion or loop  

**Problem:** Write `fibonacci(n)` returning the nth Fibonacci number where `fib(0)=0`, `fib(1)=1`. Print `fibonacci(6)`.

**Expected Output:**
```
8
```

**Hint:** Recursion with base case, or loop with two variables.

---

### Exercise 14 — Word Count

**Difficulty:** Easy  
**Concepts:** strings, split  

**Problem:** Write `word_count(sentence)` returning the number of words. Test `"Python is fun to learn"`.

**Expected Output:**
```
5
```

**Hint:** `len(sentence.split())`

---

### Exercise 15 — Min and Max Tuple

**Difficulty:** Medium  
**Concepts:** multiple return  

**Problem:** Write `bounds(numbers)` returning `(smallest, largest)`. Unpack and print both for `[5, 1, 9, 3]`.

**Expected Output:**
```
1
9
```

**Hint:** `return min(numbers), max(numbers)`

---

### Exercise 16 — Sort Keys by Values

**Difficulty:** Challenging  
**Concepts:** dict, sorted, function  

**Problem:** Write `keys_sorted_by_value(d)` returning a list of keys sorted by their values ascending. Test `{"a": 3, "b": 1, "c": 2}`.

**Expected Output:**
```
['b', 'c', 'a']
```

**Hint:** `sorted(d, key=d.get)` or sort items then take keys.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Factors List

**Difficulty:** Medium  
**Concepts:** loop, list return  

**Problem:** Write `factors(n)` returning all positive factors of `n`. Test `12`.

**Expected Output:**
```
[1, 2, 3, 4, 6, 12]
```

**Hint:** Check `n % i == 0` for `i` in `1..n`.

---

### Exercise 18 — Temperature Converter

**Difficulty:** Medium  
**Concepts:** keyword args / branching  

**Problem:** Write `convert_temp(value, to_scale)` where `to_scale` is `"C"` or `"F"`.

- If converting to F: `(C * 9/5) + 32`  
- If converting to C: `(F - 32) * 5/9`  

Print `convert_temp(25, "F")` and `convert_temp(77, "C")`.

**Expected Output:**
```
77.0
25.0
```

**Hint:** Use `if to_scale == "F":`.

---

### Exercise 19 — Primes Up to n

**Difficulty:** Challenging  
**Concepts:** nested loops / helper function  

**Problem:** Write `primes_up_to(n)` returning a list of primes `<= n`. Test `20`.

**Expected Output:**
```
[2, 3, 5, 7, 11, 13, 17, 19]
```

**Hint:** Write helper `is_prime(k)`, then collect primes.

---

### Exercise 20 — Second Highest

**Difficulty:** Medium  
**Concepts:** list, set/sort  

**Problem:** Write `second_highest(numbers)` returning the second largest unique value. Test `[5, 1, 9, 9, 3, 7]`.

**Expected Output:**
```
7
```

**Hint:** `sorted(set(numbers))[-2]`

---

### Bonus — *args Sum

**Difficulty:** Medium  
**Concepts:** `*args`  

**Problem:** Write `sum_all(*args)` returning the sum of any number of numeric arguments. Test `sum_all(1, 2, 3, 4)`.

**Expected Output:**
```
10
```

---

# Instructor Solution Guide

```python
# Exercise 1
def add(a, b):
    return a + b
print(add(3, 5))

# Exercise 2
def string_length(text):
    return len(text)
print(string_length("Python"))

# Exercise 3
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(even_or_odd(7))

# Exercise 4
def say_hello():
    print("Hello, World!")
say_hello()

# Exercise 5
def largest(numbers):
    return max(numbers)
print(largest([4, 9, 1, 7]))

# Exercise 6
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# Exercise 7
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
print(is_palindrome("Race car"))

# Exercise 8
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
greet("Ada")

# Exercise 9
def square(n):
    return n * n
print(square(6))

# Exercise 10
def concat(a, b):
    return a + b
print(concat("Hello, ", "World"))

# Exercise 11
def even_only(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
print(even_only([1, 2, 3, 4, 5, 6]))

# Exercise 12
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq
print(char_frequency("banana"))

# Exercise 13
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

# Exercise 14
def word_count(sentence):
    return len(sentence.split())
print(word_count("Python is fun to learn"))

# Exercise 15
def bounds(numbers):
    return min(numbers), max(numbers)
lo, hi = bounds([5, 1, 9, 3])
print(lo)
print(hi)

# Exercise 16
def keys_sorted_by_value(d):
    return sorted(d, key=d.get)
print(keys_sorted_by_value({"a": 3, "b": 1, "c": 2}))

# Exercise 17
def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
print(factors(12))

# Exercise 18
def convert_temp(value, to_scale):
    if to_scale == "F":
        return (value * 9 / 5) + 32
    if to_scale == "C":
        return (value - 32) * 5 / 9
    return None
print(convert_temp(25, "F"))
print(convert_temp(77, "C"))

# Exercise 19
def is_prime(k):
    if k <= 1:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True

def primes_up_to(n):
    result = []
    for k in range(2, n + 1):
        if is_prime(k):
            result.append(k)
    return result
print(primes_up_to(20))

# Exercise 20
def second_highest(numbers):
    unique_sorted = sorted(set(numbers))
    return unique_sorted[-2]
print(second_highest([5, 1, 9, 9, 3, 7]))

# Bonus
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))
```
