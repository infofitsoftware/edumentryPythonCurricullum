# Module 5 — Practice Exercises: Control Flow Statements

**Instructions**

- Attempt each exercise before opening the Instructor Solution Guide.
- Use Modules 1–5 concepts.
- For input-based tasks, test in the terminal.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Sign of a Number

**Difficulty:** Easy  
**Concepts:** if-elif-else  

**Problem:**  
Ask for an integer. Print `Positive`, `Negative`, or `Zero`.

**Example Input:**
```
-3
```

**Expected Output:**
```
Negative
```

**Hint:** Check `> 0`, then `< 0`, else zero.

---

### Exercise 2 — Even or Odd

**Difficulty:** Easy  
**Concepts:** if-else, `%`  

**Problem:**  
Ask for an integer. Print `Even` or `Odd`.

**Example Input:**
```
8
```

**Expected Output:**
```
Even
```

**Hint:** `number % 2 == 0`.

---

### Exercise 3 — Age Category

**Difficulty:** Easy  
**Concepts:** if-elif-else  

**Problem:**  
Ask for age. Print:

- `Child` if age < 12  
- `Teenager` if 12 ≤ age ≤ 18  
- `Adult` if age > 18  

**Example Input:**
```
15
```

**Expected Output:**
```
Teenager
```

**Hint:** Use `elif` carefully so boundaries do not overlap wrongly.

---

### Exercise 4 — for 1 to 10

**Difficulty:** Easy  
**Concepts:** for, range  

**Problem:**  
Print numbers from 1 to 10, each on its own line, using a `for` loop.

**Example Input:** (none)

**Expected Output:**
```
1
2
...
10
```

**Hint:** `range(1, 11)`.

---

### Exercise 5 — while Countdown

**Difficulty:** Easy  
**Concepts:** while  

**Problem:**  
Using `while`, print numbers from 10 down to 1.

**Example Input:** (none)

**Expected Output:**
```
10
9
...
1
```

**Hint:** Start `i = 10`, loop while `i >= 1`, then `i -= 1`.

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Divisible by 3 and 5

**Difficulty:** Easy  
**Concepts:** if, `and`, `%`  

**Problem:**  
Ask for a number. Print `Yes` if divisible by both 3 and 5, else `No`.

**Example Input:**
```
15
```

**Expected Output:**
```
Yes
```

**Hint:** `(n % 3 == 0) and (n % 5 == 0)`.

---

### Exercise 7 — Marks Band

**Difficulty:** Medium  
**Concepts:** if-elif-else  

**Problem:**  
Ask for marks. Print:

- `Fail` if < 40  
- `Pass` if 40–60  
- `Good` if 61–80  
- `Excellent` if > 80  

**Example Input:**
```
75
```

**Expected Output:**
```
Good
```

**Hint:** Order conditions from highest band or use careful ranges.

---

### Exercise 8 — Sum 1 to 10

**Difficulty:** Easy  
**Concepts:** for, accumulator  

**Problem:**  
Using a `for` loop, compute and print the sum of the first 10 natural numbers.

**Example Input:** (none)

**Expected Output:**
```
55
```

**Hint:** `total = 0`, then `total += i`.

---

### Exercise 9 — Evens 1 to 50

**Difficulty:** Easy  
**Concepts:** for, range step or if  

**Problem:**  
Print all even numbers from 1 to 50 (inclusive), one per line.

**Example Input:** (none)

**Expected Output:** (starts with)
```
2
4
6
```
(ends with `50`)

**Hint:** `range(2, 51, 2)` is simplest.

---

### Exercise 10 — Reverse String with for

**Difficulty:** Medium  
**Concepts:** for over string, accumulator string  

**Problem:**  
Ask for a string. Build its reverse using a `for` loop (do not use `[::-1]` for this exercise) and print it.

**Example Input:**
```
hello
```

**Expected Output:**
```
olleh
```

**Hint:** Start `rev = ""`, then `rev = char + rev` each time.

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — break at 6

**Difficulty:** Easy  
**Concepts:** for, break  

**Problem:**  
Print numbers from 1 to 10, but stop completely when the number is 6 (6 should not print).

**Example Input:** (none)

**Expected Output:**
```
1
2
3
4
5
```

**Hint:** `if i == 6: break` before printing, or print then break carefully — match expected output (1–5 only).

---

### Exercise 12 — continue Multiples of 3

**Difficulty:** Easy  
**Concepts:** for, continue  

**Problem:**  
Print 1 to 10 but skip multiples of 3.

**Example Input:** (none)

**Expected Output:**
```
1
2
4
5
7
8
10
```

**Hint:** `if i % 3 == 0: continue`.

---

### Exercise 13 — Sentinel while

**Difficulty:** Medium  
**Concepts:** while, break, input  

**Problem:**  
Keep asking the user for a number. Print each number. Stop when the user enters a negative number (do not print the negative).

**Example Input:**
```
4
9
-1
```

**Expected Output:**
```
4
9
```

**Hint:** `while True:` + `if number < 0: break`.

---

### Exercise 14 — pass Placeholder

**Difficulty:** Easy  
**Concepts:** for, pass  

**Problem:**  
Write a `for` loop that runs 5 times with only `pass` in the body. Then print `Loop finished`.

**Example Input:** (none)

**Expected Output:**
```
Loop finished
```

**Hint:** Body can be only `pass`.

---

### Exercise 15 — Factorial

**Difficulty:** Medium  
**Concepts:** for, accumulator product  

**Problem:**  
Ask for a non-negative integer `n`. Print `n!` (factorial). Assume `0! = 1`.

**Example Input:**
```
5
```

**Expected Output:**
```
120
```

**Hint:** `result = 1`; multiply by each value in `range(1, n + 1)`.

---

### Exercise 16 — Vowel Counter

**Difficulty:** Medium  
**Concepts:** for, if, strings, membership  

**Problem:**  
Ask for a string. Count vowels `a e i o u` (case-insensitive) and print the count.

**Example Input:**
```
Education
```

**Expected Output:**
```
5
```

**Hint:** Loop `text.lower()`; `if char in "aeiou"`.

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Multiplication Table

**Difficulty:** Medium  
**Concepts:** for, f-strings  

**Problem:**  
Ask for an integer `n`. Print its multiplication table from 1 to 10 as `n x i = product`.

**Example Input:**
```
5
```

**Expected Output:**
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

**Hint:** `for i in range(1, 11):`.

---

### Exercise 18 — Prime Check

**Difficulty:** Challenging  
**Concepts:** for, if, break/flag  

**Problem:**  
Ask for an integer `n > 1`. Print `Prime` or `Not prime`.

**Example Input:**
```
7
```

**Expected Output:**
```
Prime
```

**Hint:** Check divisibility from 2 to `n-1` (or to `n//2`). If any divides evenly → not prime.

---

### Exercise 19 — Fibonacci (10 terms)

**Difficulty:** Challenging  
**Concepts:** for, variables swap/update  

**Problem:**  
Print the first 10 Fibonacci numbers starting with 0 and 1, separated-separated on one line:

`0 1 1 2 3 5 8 13 21 34`

**Example Input:** (none)

**Expected Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Hint:** Keep `a, b = 0, 1`; each step print `a`, then `a, b = b, a + b`.

---

### Exercise 20 — Star Pyramid

**Difficulty:** Challenging  
**Concepts:** nested loops or string `*`  

**Problem:**  
Ask for height `h`. Print a left-aligned pyramid of `*` with `h` rows.

**Example Input:**
```
4
```

**Expected Output:**
```
*
**
***
****
```

**Hint:** `print("*" * i)` or nested loops.

---

# Instructor Solution Guide

```python
# Exercise 1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 2
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 3
age = int(input("Age: "))
if age < 12:
    print("Child")
elif age <= 18:
    print("Teenager")
else:
    print("Adult")

# Exercise 4
for i in range(1, 11):
    print(i)

# Exercise 5
i = 10
while i >= 1:
    print(i)
    i -= 1

# Exercise 6
n = int(input("Number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")

# Exercise 7
marks = int(input("Marks: "))
if marks < 40:
    print("Fail")
elif marks <= 60:
    print("Pass")
elif marks <= 80:
    print("Good")
else:
    print("Excellent")

# Exercise 8
total = 0
for i in range(1, 11):
    total += i
print(total)

# Exercise 9
for i in range(2, 51, 2):
    print(i)

# Exercise 10
text = input("Text: ")
rev = ""
for char in text:
    rev = char + rev
print(rev)

# Exercise 11
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Exercise 12
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# Exercise 13
while True:
    number = int(input("Number: "))
    if number < 0:
        break
    print(number)

# Exercise 14
for i in range(5):
    pass
print("Loop finished")

# Exercise 15
n = int(input("n: "))
result = 1
for i in range(1, n + 1):
    result *= i
print(result)

# Exercise 16
text = input("Text: ")
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print(count)

# Exercise 17
n = int(input("n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Exercise 18
n = int(input("n: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not prime")

# Exercise 19
a, b = 0, 1
for i in range(10):
    if i == 9:
        print(a)
    else:
        print(a, end=" ")
    a, b = b, a + b

# Exercise 20
h = int(input("Height: "))
for i in range(1, h + 1):
    print("*" * i)
```

**Note on Exercise 19:** `append` / `join` lightly use list+string tools; an alternate beginner version prints with `end=" "`.
