"""1. Variables and Constants
What is a Variable?
A variable is a name that refers to a value stored in memory. In Python, variables are dynamically created when a value is assigned to them.

Syntax:
variable_name = value"""

name = "Alice"   # String variable
age = 25         # Integer variable
height = 5.6     # Float variable
is_student = True  # Boolean variable

print(name, age, height, is_student)

"""Variable Naming Rules
✅ Must start with a letter (a-z, A-Z) or an underscore (_)
✅ Can contain letters, digits (0-9), and underscores
✅ Case-sensitive (name and Name are different)
✅ Should not be a Python keyword (e.g., if, while, import)

Valid Examples:"""

my_variable = 10
_myVar = "Python"
age_2024 = 30


"""Invalid Examples:"""
2name = "John"  # ❌ Cannot start with a number
my-variable = 50  # ❌ Hyphens are not allowed
if = 25  # ❌ 'if' is a reserved keyword

"""2.Data Types in Python
Python provides built-in data types for handling different kinds of values.

Data Type                           Description                              Example
int                                 Whole numbers	                         10, -5, 200
float                               Decimal numbers                          3.14, -0.5, 2.0
str                                 Sequence of characters                   "Hello", 'Python'
bool                                Boolean values (True or False)            True, False
NoneType                            Represents an absence of value            None
"""

age = 25  # Integer
price = 19.99  # Float
message = "Hello, World!"  # String
is_python_easy = True  # Boolean
nothing = None  # NoneType

print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(message))   # <class 'str'>
print(type(is_python_easy))  # <class 'bool'>
print(type(nothing))   # <class 'NoneType'>


"""
3. Type Casting (Type Conversion)

Python allows you to convert one data type into another using casting functions.

Function                                                   Converts To
int(x)                                                     Integer
float(x)                                                   Float
str(x)                                                     String
bool(x)                                                    Boolean
"""

num = 10
print(type(num))  # <class 'int'>

num_str = str(num)
print(type(num_str))  # <class 'str'>

pi = "3.14"
pi_float = float(pi)
print(type(pi_float))  # <class 'float'>


"""
Important Notes on Type Casting:
✔️ int(3.9) → 3 (Removes decimal part)
✔️ float("10") → 10.0
✔️ bool(0) → False, bool(1) → True
"""

"""
Why Type Casting is Important for input()?
Python’s input() function always returns user input as a string, even if the user enters a number. This is why we need type conversion when working with numerical values.

Example (Incorrect way without casting):
"""

num1 = input("Enter first number: ")  # User enters 5
num2 = input("Enter second number: ")  # User enters 3
print("Sum:", num1 + num2)  # Output: 53 (Incorrect, since '5' + '3' = '53')


"""⚠️ Here, Python treats both inputs as strings, so concatenation occurs instead of addition."""

"""Correct way using int() casting:"""

num1 = int(input("Enter first number: "))  # Convert input to integer
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)  # Output: 8 (Correct)

"""Similarly, for decimal inputs, we use float():"""

num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))
print("Sum:", num1 + num2)


"""
4. Type Checking
Python provides the type() function to check the type of a variable.

Example:
"""

x = 42
y = "Python"
z = 3.14

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>


print(isinstance(42, int))  # True
print(isinstance("Python", float))  # False
print(isinstance(3.14, (int, float)))  # True (Checks both int and float)
