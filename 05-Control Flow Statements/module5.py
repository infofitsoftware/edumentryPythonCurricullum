# Control Flow Statements

"""1. Conditional Statements in Python
Control flow statements allow programs to make decisions and execute specific code blocks based on conditions.

1.1 The `if` Statement
The `if` statement executes a block of code **only if** the specified condition evaluates to `True`.


Syntax:

if condition:
    # Code to execute if condition is True

"""

#Example: Checking for a Positive Number**

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")




"""1.2 The `if-else` Statement
The `if-else` statement provides two execution paths:
- If the condition is `True`, the `if` block executes.
- Otherwise, the `else` block executes.

**Syntax:**

if condition:
    # Executes if condition is True
else:
    # Executes if condition is False"""


"""Example: Checking Even or Odd Numbers"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")




"""1.3 The `if-elif-else` Ladder
For multiple conditions, the `if-elif-else` structure is used instead of multiple `if-else` statements.

**Syntax:**

if condition1:
    # Executes if condition1 is True
elif condition2:
    # Executes if condition2 is True
else:
    # Executes if none of the conditions are True"""


"""Example: Checking Positive, Negative, or Zero"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")



"""
2. Looping Constructs (`for`, `while`)
Loops allow repeated execution of code until a condition is met.

Understanding the `range()` Function
Before diving into loops, let's understand `range()`, which generates a sequence of numbers.

#### **Syntax:**

range(start, stop, step)

- **start**: (Optional) The starting number (default is `0`).
- **stop**: The ending number (**not included in the range**).
- **step**: (Optional) The increment between numbers (default is `1`)."""


for i in range(1, 6):
    print(i)

"""Output:

1
2
3
4
5"""



"""2.1 The `for` Loop
A `for` loop iterates over a sequence (list, tuple, string, `range()`).

**Example: Printing Numbers from 1 to 5**"""

for i in range(1, 6):
    print(i)


"""🔹 The loop runs **5 times**, from `1` to `5`."""

"""Iterating Over a List
A list is a collection of items enclosed in square brackets []."""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

"""Iterating Over a Tuple
A tuple is similar to a list but immutable (cannot be changed) and enclosed in parentheses ()."""

numbers = (10, 20, 30, 40)

for num in numbers:
    print(num)


"""Iterating Over a String
A string is a sequence of characters, so we can iterate over each character."""

word = "Python"

for char in word:
    print(char)


"""2.2 The `while` Loop
A `while` loop runs as long as a condition is `True`.

Example: Printing Numbers from 1 to 5**"""

i = 1
while i <= 5:
    print(i)
    i += 1  # Increment to avoid an infinite loop


"""The loop stops when `i > 5`."""


"""3. Control Statements (`break`, `continue`, `pass`)
These statements control the flow of loops."""

### 3.1 The `break` Statement
#The `break` statement exits the loop immediately.

#### **Example: Stop Printing at 5**

for i in range(1, 11):
    if i == 5:
        break
    print(i)

"""**Output:**

1
2
3
4"""
#The loop stops when `i == 5`.


### 3.2 The `continue` Statement
"""The continue statement **skips** the current iteration and moves to the next one.

Example: Skip 5 in a Loop"""

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

"""Output:

1
2
3
4
6
7
8
9
10

The loop **skips** printing `5` but continues execution."""


"""3.3 The `pass` Statement
The `pass` statement does nothing; it acts as a placeholder.

**Example:"""

for i in range(5):
    pass  # Placeholder for future code

#Commonly used in empty function definitions or loops to avoid syntax errors.

