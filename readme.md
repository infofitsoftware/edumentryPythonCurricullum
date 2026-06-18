# 📘 edumentry :- Python Fundamentals Course

## 📌 Course Overview
This course covers the fundamentals of Python programming, starting from basic syntax to file handling. Each module includes conceptual understanding, examples, and exercises.

---

## 📚 Course Modules

### 🟢 **Module 1: Introduction to Python**

---

#### 🔹 1. What is Python?

Python is a high-level, interpreted programming language developed by **Guido van Rossum** in 1991. It is widely used in web development, data analysis, AI/ML, automation, and more.

**Key Characteristics:**
- ✔️ Simple and readable syntax
- ✔️ Interpreted language (no need to compile)
- ✔️ Dynamically typed
- ✔️ Cross-platform support
- ✔️ Rich standard libraries

---

#### 🔹 2. Why Python? (Features and Applications)

**Advantages:**
- ✅ Beginner-friendly
- ✅ Works on any operating system
- ✅ Platform-independent
- ✅ Interactive and interpreted
- ✅ Extensive community support
- ✅ Huge collection of libraries and frameworks

**Popular Use Cases:**
- 🌐 Web Development – *Django, Flask*
- 📊 Data Science & ML – *Pandas, NumPy, TensorFlow*
- 🤖 Automation & Scripting
- 🎮 Game Development – *Pygame*
- 🔐 Cybersecurity & Ethical Hacking

---

#### 🔹 3. Installing Python and Setting Up Environment

**🔧 Windows:**
- Download Python from [https://www.python.org](https://www.python.org)
- Run the installer and **check the box**: ✅ *Add Python to PATH*
- Open Command Prompt and verify installation:

```bash
python --version
```
🐧 Linux (Ubuntu) or 🖥️ macOS:

Check version:
```bash
python3 --version
```

If not installed:
# For Ubuntu/Debian
```bash
sudo apt install python3
```
# For macOS (using Homebrew)
```bash
brew install python
```
---

#### 🔹 4. Introduction to print() and input() Functions

🖨️ print() – Display Output:
```python
print("Welcome to Python!")
print("My name is John.")
```
🧠 Tip: print() can display multiple items separated by commas, and it will automatically insert a space between them:

```python
print("The sum of 5 and 3 is:", 5 + 3)
```

⌨️ input() – Take User Input:
```python
name = input("Enter your name: ")
print(name)
```

---
#### 🔹 5. Writing and Running Your First Python Script
```python
print("Hello, World!")
```

Save this code in a file called hello.py and run it using:
```python
python hello.py
```
📌note: Use python or python3 depending on your system.
---
#### 🔹 6. Basic Arithmetic Operations in Python

```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)
```
---


#### 7. Simple Interactive Program
```python
first_name = input("please enter your first name: ")
last_name = input("please enter your last name: ")
full_name=first_name+last_name
print("hello,",full_name)
```


### 🟢 **Module 2: Variables, Data Types & Type Casting**

---

#### 🔹 1. Variables and Constants

A **variable** is a name that refers to a value stored in memory. In Python, variables are dynamically created when a value is assigned.

A **constant**, by convention, is a variable written in **all uppercase** to indicate that it should not be changed (though Python does not enforce it like other languages).

```python
PI = 3.14159      # Constant by naming convention
MAX_USERS = 100
```

**🔧 Syntax:**
```python
variable_name = value
```

🧪 Example:

```python
name = "Alice"         # String variable
age = 25               # Integer variable
height = 5.6           # Float variable
is_student = True      # Boolean variable

print(name, age, height, is_student)
```
🧠 **Tip:** You can print multiple values together using commas. Python will separate them with spaces:

🔹 Variable Naming Rules
- ✅ Must start with a letter (a-z, A-Z) or underscore _
- ✅ Can include letters, numbers (0-9), and underscores
- ✅ Case-sensitive (Name and name are different)
- ✅ Cannot use Python reserved keywords (if, while, import, etc.)

- ✅ Valid Examples:
```python
my_variable = 10
_myVar = "Python"
age_2024 = 30
```
❌ Invalid Examples:
```python
2name = "John"      # Cannot start with a number
my-variable = 50    # Hyphens are not allowed
if = 25             # 'if' is a reserved keyword
```
---
#### 🔹 2. Data Types in Python
Python provides built-in types to store different kinds of values.

| Data Type   | Description                         | Example       |
|:------------|:------------------------------------|:--------------|
| `int`       | Whole numbers                       | `10`, `-5`    |
| `float`     | Decimal numbers                     | `3.14`, `2.0` |
| `str`       | Sequence of characters (strings)    | `"Hello"`     |
| `bool`      | Boolean values                      | `True`, `False` |
| `NoneType`  | Represents the absence of a value   | `None`        |

🧪 Examples:
```python
age = 25                 # int
price = 19.99            # float
message = "Hello"        # str
is_python_easy = True    # bool
nothing = None           # NoneType

print(type(age))
print(type(price))
print(type(message))
print(type(is_python_easy))
print(type(nothing))
```

---
#### 🔹 3. Type Checking
Python provides type() to check the variable's type and isinstance() to verify it against a specific type or tuple of types.

🧪 Example:
```python
x = 42
y = "Python"
z = 3.14
```
```python
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>
```
```python
print(isinstance(42, int))             # True
print(isinstance("Python", float))     # False
print(isinstance(3.14, (int, float)))  # True
```
---
#### 🔄 4. Type Casting (Type Conversion)

Python allows converting between data types using casting functions.

| Function     | Description             | Example                  |
|--------------|-------------------------|--------------------------|
| `int(x)`     | Converts to Integer     | `int(3.9)` → `3`         |
| `float(x)`   | Converts to Float       | `float("10")` → `10.0`   |
| `str(x)`     | Converts to String      | `str(123)` → `"123"`     |
| `bool(x)`    | Converts to Boolean     | `bool(0)` → `False`      |


🧪 Example:
```python
num = 10
print(type(num))     # <class 'int'>

num_str = str(num)
print(type(num_str)) # <class 'str'>

pi = "3.14"
pi_float = float(pi)
print(type(pi_float)) # <class 'float'>
```
ℹ️ Notes:

int(3.9) → 3 (decimal removed)

float("10") → 10.0

bool(0) → False, bool(1) → True

🔹 Why Type Casting is Important with input() when doing operation with numbers
The input() function always returns a string, even for numeric inputs. You need type casting to perform arithmetic.

🚫 Incorrect way (no casting):
```python
num1 = input("Enter first number: ")  # User enters 5
num2 = input("Enter second number: ") # User enters 3
print("Sum:", num1 + num2)  # Output: 53 (string concatenation)
```

✅ Correct way using int():
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)  # Output: 8
```

✅ For decimal inputs using float():
```python
num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))
print("Sum:", num1 + num2)
```




### 🟣 Module 3: Strings in Python

---

#### 1️⃣ Introduction to Strings

A **string** in Python is a sequence of characters enclosed within single (`'`), double (`"`), or triple (`'''` or `"""`) quotes.

**Key Properties of Strings**  
✅ Immutable: Strings cannot be modified once created  
✅ Indexed: Characters can be accessed using positive and negative indices  
✅ Iterable: Strings can be looped through character by character  

---

#### 2️⃣ Creating Strings in Python

Python allows multiple ways to create a string:

```python
# Using single, double, and triple quotes
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline 
string using triple quotes.'''

print(str1, str2, str3)
```
---
#### 3️⃣ String Indexing and Slicing


String Indexing Table:

| Characters         | P  | Y  | T  | H  | O  | N  |
|--------------------|----|----|----|----|----|----|
| Forward Indexing   | 0  | 1  | 2  | 3  | 4  | 5  |
| Reverse Indexing   | -6 | -5 | -4 | -3 | -2 | -1 |

String Indexing:
```python
word = "Python"
print(word[0])    # P (First character)
print(word[-1])   # n (Last character)
```

String Slicing:
```python
word = "Programming"
print(word[0:5])    # Output: Progr (0 to 4)
print(word[:6])     # Output: Progra (0 to 5)
print(word[3:])     # Output: gramming (from index 3 to end)
print(word[::2])    # Output: Pormig (every 2nd character)/(Characters at index 0, 2, 4, 6, ...)
print(word[::-1])   # Output: gnimmargorP (Reversed string)
```
---
#### 4️⃣ Built-in String Methods (Raw Markdown Table)

| Method               | Description                                         |
|----------------------|-----------------------------------------------------|
| `capitalize()`       | Capitalizes first letter                            |
| `casefold()`         | Converts to lowercase (more aggressive)             |
| `center(width)`      | Centers string in a given width                     |
| `count(substring)`   | Counts occurrences of a substring                   |
| `encode()`           | Converts string to bytes                            |
| `endswith(suffix)`   | Checks if string ends with the given suffix         |
| `expandtabs(size)`   | Replaces tabs with spaces                           |
| `find(substring)`    | Returns the index of first occurrence               |
| `index(substring)`   | Same as find but raises error if not found          |
| `isalnum()`          | Checks if all characters are alphanumeric           |
| `isalpha()`          | Checks if all characters are letters                |
| `isdigit()`          | Checks if all characters are digits                 |
| `islower()`          | Checks if all characters are lowercase              |
| `isspace()`          | Checks if all characters are whitespace             |
| `istitle()`          | Checks if string is title-cased                     |
| `isupper()`          | Checks if all characters are uppercase              |
| `join(iterable)`     | Joins elements of an iterable with the string       |
| `ljust(width)`       | Left-aligns string within given width               |
| `lower()`            | Converts to lowercase                               |
| `lstrip()`           | Removes leading whitespace                          |
| `replace(old, new)`  | Replaces old substring with new                     |
| `rfind(substring)`   | Finds last occurrence of substring                  |
| `rindex(substring)`  | Like rfind, but raises error if not found           |
| `rjust(width)`       | Right-aligns string                                 |
| `rstrip()`           | Removes trailing whitespace                         |
| `split(sep)`         | Splits string into list                             |
| `splitlines()`       | Splits string at line breaks                        |
| `startswith(prefix)` | Checks if string starts with given prefix           |
| `strip()`            | Removes leading/trailing whitespace                 |
| `swapcase()`         | Swaps case of all characters                        |
| `title()`            | Converts to title case                              |
| `upper()`            | Converts to uppercase                               |
| `zfill(width)`       | Pads string with zeros                              |

---
#### 5️⃣ String Methods and Functions
```python
# Finding String Length
text = "Python"
print(len(text))  # Output: 6

# Changing Case
text = "hello world"
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.title())       # Hello World
print(text.capitalize())  # Hello world

# Checking String Content
print("Python".isalpha())    # True
print("1234".isdigit())      # True
print("Hello123".isalnum())  # True
print("   ".isspace())       # True

# Searching in Strings
text = "Python programming"
print(text.find("prog"))  # Output: 7
print(text.count("o"))    # Output: 2

# Replacing and Splitting
text = "I love Python"
print(text.replace("love", "like"))  # I like Python

words = text.split()
print(words)  # ['I', 'love', 'Python']

joined = "-".join(words)
print(joined)  # I-love-Python

# Checking Prefix and Suffix
text = "hello.py"
print(text.startswith("hello"))  # True
print(text.endswith(".py"))      # True

# Stripping Whitespace
text = "  hello  "
print(text.strip())   # 'hello'
print(text.lstrip())  # 'hello  '
print(text.rstrip())  # '  hello'
```
---
#### 6️⃣ String Formatting

```python
# Using format()
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```
```python
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
```
---
#### 7️⃣ Escape Sequences

| Escape Sequence | Meaning     |
|------------------|-------------|
| `\n`             | Newline     |
| `\t`             | Tab         |
| `\\`             | Backslash   |

```python
print("Hello\nWorld")  # Newline
print("Name:\tAlice")  # Tab
```
---
#### 8️⃣ Raw Strings

```python
# Raw strings ignore escape sequences
print(r"C:\newfolder\test")  # Output: C:\newfolder\test
```


---

### 🟣 Module 4: Operators and Expressions



Operators are symbols that perform operations on variables and values.  
Expressions are combinations of values, variables, and operators that produce a result.

In this module, we will explore different types of operators in Python and how they work.

---

#### ➕ 1. Arithmetic Operators

These operators perform mathematical operations like addition, subtraction, multiplication, and division.

```python
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

```

| Operator        | Symbol | Example   | Result                            |
|----------------|--------|-----------|-----------------------------------|
| Addition        | +      | 10 + 5    | 15                                |
| Subtraction     | -      | 10 - 5    | 5                                 |
| Multiplication  | *      | 10 * 5    | 50                                |
| Division        | /      | 10 / 3    | 3.3333                            |
| Floor Division  | //     | 10 // 3   | 3 (Removes decimal part)         |
| Modulus         | %      | 10 % 3    | 1 (Remainder)                    |
| Exponentiation  | **     | 2 ** 3    | 8 (2³)                            |

---
#### 🧮 2. Comparison (Relational) Operators
These operators return True or False based on a condition.

```python
x = 10
y = 5

print(x > y)    # True
print(x < y)    # False
print(x == 10)  # True
print(y != 5)   # False
```

| Operator | Meaning                      | Example   | Result |
|----------|------------------------------|-----------|--------|
| ==       | Equal to                     | 5 == 5    | True   |
| !=       | Not equal to                 | 5 != 3    | True   |
| >        | Greater than                 | 10 > 5    | True   |
| <        | Less than                    | 2 < 5     | True   |
| >=       | Greater than or equal to     | 3 >= 3    | True   |
| <=       | Less than or equal to        | 4 <= 2    | False  |

---
#### ⚙️ 3. Logical Operators
Used to combine multiple conditions.

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```


| Operator | Meaning                                     | Example                          | Result |
|----------|---------------------------------------------|----------------------------------|--------|
| and      | Returns True if both conditions are True    | (5 > 2) and (10 > 3)             | True   |
| or       | Returns True if at least one is True        | (5 > 2) or (10 < 3)              | True   |
| not      | Reverses the Boolean result                 | not (5 > 2)                      | False  |




---
#### 📝 4. Assignment Operators
Used to assign or modify values of variables.

```python
x = 10
x += 5  # x = x + 5
print(x)  # 15

x *= 2  # x = x * 2
print(x)  # 30
```

| Operator | Meaning                    | Example   | Equivalent To   |
|----------|----------------------------|-----------|-----------------|
| =        | Assign value               | x = 10    | x = 10          |
| +=       | Add & assign               | x += 5    | x = x + 5       |
| -=       | Subtract & assign          | x -= 3    | x = x - 3       |
| *=       | Multiply & assign          | x *= 2    | x = x * 2       |
| /=       | Divide & assign            | x /= 2    | x = x / 2       |
| //=      | Floor divide & assign      | x //= 2   | x = x // 2      |
| %=       | Modulus & assign           | x %= 3    | x = x % 3       |
| **=      | Exponentiate & assign      | x **= 2   | x = x ** 2      |


---
#### 🧭 5. Identity  Operators
🧠 Identity Operators
Check if two variables reference the same object in memory.

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True
print(a is c)   # False
print(a == c)   # True
```

| Operator | Meaning                          | Example     |
|----------|----------------------------------|-------------|
| is       | True if objects are identical    | x is y      |
| is not   | True if objects are not same     | x is not y  |


#### 📦 Membership Operators
Used to check if a value exists in a collection.

```python
word = "apple"

print("a" in word)      # True — 'a' is in "apple"
print("z" in word)      # False — 'z' is not in "apple"
print("pp" in word)     # True — "pp" is a substring of "apple"
print("app" not in word) # False — "app" *is* in "apple"

```

| Operator | Meaning                                 | Example              |
|----------|-----------------------------------------|----------------------|
| in       | True if value exists in the sequence    | 'a' in 'apple'       |
| not in   | True if value does not exist            | 5 not in [1, 2, 3]   |





### 🧭 Module 5: Control Flow Statements

Control flow statements allow programs to make decisions and repeat code blocks based on conditions.

---

#### ✅ 1. Conditional Statements

 🔹 1.1 The `if` Statement

Executes a block of code **only if** the condition is `True`.

**🔧 Syntax:**
```python
if condition:
    # Code to execute if condition is True
```

📌 Example: Check if a number is positive

num = int(input("Enter a number: "))
```python
if num > 0:
    print("The number is positive.")
```

🔹 1.2 The if-else Statement
Executes one of two blocks depending on the condition.

🔸 if-else Flow

        ┌───────────────┐
        │  Condition ?  │
        └─────┬─────────┘
              │
        ┌─────▼───────┐
     Yes│  Execute     │
        │  if-block    │
        └─────┬────────┘
              │
           ┌──▼──┐
           │ End │
           └─────┘
              │
             No
              │
        ┌─────▼───────┐
        │ Execute     │
        │ else-block  │
        └─────┬────────┘
              │
           ┌──▼──┐
           │ End │
           └─────┘


🔧 Syntax:
```python
if condition:
    # Executes if condition is True
else:
    # Executes if condition is False
```

📌 Example: Even or Odd
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```


🔹 1.3 The if-elif-else Ladder
Used to test multiple conditions.

🔸 if-elif-else Flow

         ┌──────────────┐
         │ Condition 1? │
         └─────┬────────┘
               │Yes
         ┌─────▼───────┐
         │ Execute     │
         │ if-block    │
         └─────┬────────┘
               │
            ┌──▼──┐
            │ End │
            └─────┘
               │
              No
               │
         ┌─────▼───────┐
         │ Condition 2?│
         └─────┬────────┘
               │Yes
         ┌─────▼───────┐
         │ Execute     │
         │ elif-block  │
         └─────┬────────┘
               │
            ┌──▼──┐
            │ End │
            └─────┘
               │
              No
               │
         ┌─────▼───────┐
         │ Execute     │
         │ else-block  │
         └─────┬────────┘
               │
            ┌──▼──┐
            │ End │
            └─────┘


🔧 Syntax:
```python
if condition1:
    # Executes if condition1 is True
elif condition2:
    # Executes if condition2 is True
else:
    # Executes if none are True
```

📌 Example: Positive, Negative, or Zero
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```
---
#### 🔁 2. Looping Constructs
Loops are used to repeat a block of code.

🔸 for Loop Flow

        ┌───────────────┐
        │  Initialize   │
        │  Loop Var     │
        └─────┬─────────┘
              │
        ┌─────▼───────┐
        │ Condition ? │
        └─────┬───────┘
              │Yes
        ┌─────▼────────┐
        │ Execute Loop │
        │   Body       │
        └─────┬────────┘
              │
        ┌─────▼───────┐
        │ Increment   │
        │  Loop Var   │
        └─────┬───────┘
              │
             (Repeat)
              │
             No
              │
        ┌─────▼────┐
        │   End    │
        └──────────┘


🔹 Understanding range() Function
Syntax:

```python
range(start, stop, step)
```

start: Optional, default is 0

stop: Required (excluded)

step: Optional, default is 1

Example:
```python
for i in range(1, 6):
    print(i)
```

Output:
```python
1
2
3
4
5
```

🔹 2.1 for Loop
Used for iterating over sequences like list, tuple, string.

📌 Example: Iterate 1 to 5
```python
for i in range(1, 6):
    print(i)
```

📌 Example: Iterate Over List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

📌 Example: Iterate Over Tuple
```python
numbers = (10, 20, 30, 40)
for num in numbers:
    print(num)
```

📌 Example: Iterate Over String
```python
word = "Python"
for char in word:
    print(char)
```

🔹 2.2 while Loop
Runs while the condition is True.

🔸 while Loop Flow

        ┌───────────────┐
        │ Initialization│
        └─────┬─────────┘
              │
        ┌─────▼───────┐
        │ Condition ? │
        └─────┬───────┘
              │Yes
        ┌─────▼────────┐
        │ Execute Loop │
        │   Body       │
        └─────┬────────┘
              │
        ┌─────▼───────┐
        │ Update      │
        │ Condition   │
        └─────┬───────┘
              │
             (Repeat)
              │
             No
              │
        ┌─────▼────┐
        │   End    │
        └──────────┘


📌 Example: 1 to 5
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
---
#### 🔀 3. Control Statements (break, continue, pass)
⛔ 3.1 break Statement
Stops the loop immediately.

📌 Example: Stop at 5
```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output:
```python
1
2
3
4
```

📌 Example: break — Stop when input is correct:

```python
while True:
    pwd = input("Enter password: ")
    if pwd == "admin123":
        print("Access granted.")
        break
```

➿ 3.2 continue Statement
Skips current iteration and continues.

📌 Example: Skip 5

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

```python
1
2
3
4
6
7
8
9
10
```
📌Example: continue — Skip vowels:

```python
for char in "education":
    if char in "aeiou":
        continue
    print(char)
```

📭 3.3 pass Statement
Does nothing — used as a placeholder.

📌 Example:
```python
for i in range(5):
    pass  # Placeholder for future code
```



### 🧩 Module 6: Lists, Tuples, Dictionaries, and Sets in Python

---

### 1.📌 Lists in Python (Ordered & Mutable)
📖 Introduction to Lists
A list in Python is an ordered, mutable collection that can hold multiple data types.
You can add, update, delete, and rearrange elements easily.

🛠️ Creating a List

```python
# Empty list
empty_list = []

# List with mixed data types
mixed_list = [10, "Python", 3.14, True]

# Nested list
nested_list = [[1, 2, 3], ["a", "b", "c"]]

print(mixed_list)
print(nested_list)
```

🔍 Accessing Elements (Indexing & Slicing)

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])     # First element → 10
print(numbers[-1])    # Last element → 50
print(numbers[1:4])   # Sublist → [20, 30, 40]
print(numbers[:3])    # → [10, 20, 30]
print(numbers[::2])   # Every second element → [10, 30, 50]
```

📝 Modifying and Updating Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Replace banana with blueberry
print(fruits)
```

🔧 Common List Methods

```scss
append(), extend(), insert(), remove(), pop(), clear(), 
index(), count(), sort(), reverse(), copy()
```

📋 Method Reference Table

| Method        | Description                                 |
|---------------|---------------------------------------------|
| append()      | Adds a single element at the end            |
| extend()      | Adds multiple elements from another list    |
| insert()      | Inserts an element at a specific index      |
| remove()      | Removes the first occurrence of a value     |
| pop()         | Removes and returns element by index        |
| clear()       | Removes all elements from the list          |
| index()       | Returns the first index of a value          |
| count()       | Counts how many times a value appears       |
| sort()        | Sorts the list in ascending order           |
| reverse()     | Reverses the list order                     |
| copy()        | Returns a shallow copy of the list          |

Examples:

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)

colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)

🎯 List Comprehension

```python
# Squares of numbers
squares = [x**2 for x in range(1, 6)]
print(squares)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)

```
---
### 2.📦 Tuples in Python (Ordered & Immutable)
📖 Introduction to Tuples
A tuple is similar to a list but immutable (cannot be changed once created).

```python
# Creating Tuples
empty_tuple = ()
mixed_tuple = (10, "Python", 3.14, True)
single_element = (5,)  # Important: Comma needed
nested_tuple = ((1, 2), ("a", "b"))

print(mixed_tuple)
```

🧭 Indexing & Slicing Tuples
```python
numbers = (10, 20, 30, 40, 50)
print(numbers[0])      # First element
print(numbers[-1])     # Last element
print(numbers[1:4])    # Slice → (20, 30, 40)
```

⚠️ Tuple Immutability
```python
fruits = ("apple", "banana", "cherry")
# fruits[1] = "blueberry"  ❌ Error!
```

🔧 Common Tuple Methods
```python
numbers = (1, 2, 1, 4, 1)
print(numbers.count(1))     # → 3
print(numbers.index(4))     # → 3
```

📦 Tuple Packing & Unpacking
```python
person = ("John", 25, "Engineer")
name, age, job = person
print(name, age, job)
```

🔁 Conversion Between List and Tuple
```python
# List → Tuple
lst = [1, 2, 3]
tpl = tuple(lst)

# Tuple → List
tpl2 = ("red", "green")
lst2 = list(tpl2)
```
---
### 3.🗂️ Dictionaries in Python (Key-Value Pairs)
📖 Introduction
A dictionary stores data in key-value format. Keys must be unique.

```python
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics"]
}
```

🔍 Accessing & Modifying Dictionary

```python
print(student["name"])          # Alice
print(student.get("email", "N/A"))  # Safe access


# Modify
student["city"] = "New York"
student["grade"] = "A+"
del student["age"]
```

🔧 Common Dictionary Methods
| Method         | Description                                      |
|----------------|--------------------------------------------------|
| get()          | Gets value of a key safely                       |
| keys()         | Returns all keys                                 |
| values()       | Returns all values                               |
| items()        | Returns all key-value pairs                      |
| update()       | Merges another dictionary                        |
| pop()          | Removes item by key                              |
| popitem()      | Removes the last inserted item                   |
| setdefault()   | Sets a default value if key doesn't exist        |
| clear()        | Clears all entries                               |


```python
student.update({"hobby": "Reading"})
student.pop("city")
student.popitem()
```

🔁 Looping Through Dictionary

```python
for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(f"{key} -> {value}")
```

🧩 Nested Dictionary

```python
company = {
    "emp1": {"name": "John", "role": "Manager"},
    "emp2": {"name": "Alice", "role": "Dev"}
}
print(company["emp1"]["role"])  # Manager
```

🧠 Dictionary Comprehension

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)
```

---
### 4.🔗 Sets in Python (Unordered & Unique)
📖 Introduction
A set is:

Unordered

Mutable

Contains unique elements

```python
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # Duplicates removed
```

🧪 Set Operations

| Operation             | Syntax                    | Description                      |
|-----------------------|---------------------------|----------------------------------|
| Union                 | A.union(B)                | Combines all unique elements     |
| Intersection          | A.intersection(B)         | Common elements only             |
| Difference            | A.difference(B)           | Elements in A not in B           |
| Symmetric Difference  | A.symmetric_difference(B) | Unique in A or B, not both       |


```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))             # → {1, 2, 3, 4, 5}
print(A.intersection(B))      # → {3}
print(A.difference(B))        # → {1, 2}
print(A.symmetric_difference(B))  # → {1, 2, 4, 5}
```


⚙️ Modifying Sets
```python
fruits.add("orange")
fruits.update(["grape", "mango"])

fruits.remove("banana")   # ❌ Error if not found
fruits.discard("banana")  # ✅ No error
random_element = fruits.pop()
fruits.clear()
```

🔁 Iterating Sets
```python
for item in fruits:
    print(item)
```

🧠 Set Comprehension
```python
squared = {x**2 for x in range(1, 6)}
print(squared)  # → {1, 4, 9, 16, 25}
```


### 🧠 Module 7: Python Functions
---
Functions help in organizing code into reusable blocks. In this module, we’ll learn how to define and use functions effectively.

🔹 1. Defining and Calling Functions

A function is defined using the def keyword, followed by a name, parentheses () (with optional parameters), and a colon :

```python
# Function Definition
def greet():
    print("Hello! Welcome to Python.")

# Function Call
greet()
```
✅ A function must be defined before it's called.
📝 Indentation is critical inside function blocks.



🔹 2. Function Parameters and Return Values

📌 2.1 Parameters vs. Arguments

Parameters → Variables in the function definition.

Arguments → Actual values passed when calling the function.

```python
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")
```

📌 2.2 Returning a Value

Use return to send a value back to the caller.

```python
def square(num):
    return num * num

result = square(4)
print("Square:", result)
```
🚫 A function stops execution once return is encountered.




🔹 3. Types of Function Arguments

Python supports four types of function arguments:

| Argument Type            | Description                                | Example                          |
|--------------------------|--------------------------------------------|----------------------------------|
| Positional Arguments     | Passed in the correct order                | `func(1, 2)`                     |
| Default Arguments        | Parameters with default values             | `func(a=5, b=10)`                |
| Keyword Arguments        | Specify argument names during function call| `func(b=10, a=5)`                |
| Variable-Length Arguments| Accepts multiple values using *args/**kwargs| `func(1, 2, 3, key="value")`     |


📌 3.1 Positional Arguments
Arguments passed in the correct order.

```python
def add(a, b):
    return a + b

print(add(3, 5))  # ✅
# print(add(3))   # ❌ Error: missing argument
```

⚙️ 3.2 Default Arguments
Assign default values if no argument is passed.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Uses default → "Guest"
greet("Alice")  # Overrides default
```

📝 Default parameters must be placed after non-defaults.

🧾 3.3 Keyword Arguments
Specify arguments using parameter names (order doesn't matter).

```python
def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet(animal="dog", name="Buddy")
describe_pet(name="Kitty", animal="cat")
```

🌟 3.4 Variable-Length Arguments
➕ *args → Non-keyword variable arguments
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10
```
📦 *args is treated as a tuple of values.

🧩 **kwargs → Keyworded variable arguments
```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25, city="New York")
```

🔑 **kwargs is treated as a dictionary of named arguments.

⚡ 4️⃣ Lambda Functions (Anonymous Functions)
A lambda is a small, single-line function.

📐 Syntax

lambda arguments: expression

Example:
```python
cube = lambda x: x ** 3
print(cube(3))  # Output: 27
```


### 📁 Module 08: File Handling in Python
File handling allows us to read and write data to files. Python provides built-in functions to handle files easily and efficiently.

🗂️ File Modes in Python

| Mode  | Description                            |
|-------|----------------------------------------|
| "r"   | Read (default mode)                    |
| "w"   | Write (overwrites file if it exists)   |
| "a"   | Append (adds content to the file)      |
| "x"   | Exclusive creation (fails if file exists) |
| "rb"  | Read binary                            |
| "wb"  | Write binary                           |
| "ab"  | Append binary                          |


📖 Opening and Closing Files

```python
file = open("example.txt", "r")  # Open in read mode
file.close()                     # Close the file
```

✅ Always close the file after use!

✍️ Writing to a File
```python
file = open("sample.txt", "w")
file.write("Hello, this is a test file.")
file.close()
```

📚 Reading from Files
🔹 Reading the entire content

```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

🔹 Reading line by line

```python
file = open("sample.txt", "r")
line = file.readline()
print(line)
file.close()
```

🔹 Reading all lines into a list

```python
file = open("sample.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

📝 Writing Multiple Lines

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("output.txt", "w")
file.writelines(lines)
file.close()
```

➕ Appending to a File

```python
file = open("output.txt", "a")
file.write("This line will be appended.\n")
file.close()
```

🤝 Using with Statement (Auto-closes File)

```python
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
# No need to explicitly close
```

🖼️ Working with Binary Files
🔹 Reading a binary file


```python
with open("image.jpg", "rb") as file:
    data = file.read()
    print("Binary content:", data[:20])  # First 20 bytes
```

```python
with open("copy.jpg", "wb") as new_file:
    new_file.write(data)
```


🔍 Check if File Exists

```python
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")

```


❌ Deleting a File

```python
import os

os.remove("sample.txt")

```

✅ Tips:

Always close the file or use with to handle it automatically.

Use binary mode for images or non-text files.

File handling is crucial for logging, storing data, and working with external files.










