"""
1. Defining and Calling Functions
A function is defined using the def keyword, followed by a function name, parentheses ( ), and a colon :.

Syntax of a Function

def function_name():
    # Function body (code)

"""

def greet():
    print("Hello! Welcome to Python.")

# Calling the function
greet()

"""
A function must be defined before calling it.
Indentation is crucial in Python (inside the function block).

"""

"""
2. Function Parameters and Return Values
2.1 Parameters vs. Arguments
Parameters → Variables inside the function definition.
Arguments → Actual values passed when calling the function.
"""

def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")


"""
2.2 Returning a Value
A function can return a result using the return statement.
"""

#Example: Function with Return Value
def square(num):
    return num * num

result = square(4)
print("Square:", result)


"""
Use return to send back values from a function.
A function stops execution when return is encountered.
"""

"""
3. Types of Function Arguments
Python supports four types of function arguments:

Argument Type	                                           Example
Positional Arguments	                                 func(1, 2)
Default Arguments	                                     func(a=5, b=10)
Keyword Arguments	                                     func(b=10, a=5)
Variable-Length Arguments (*args, **kwargs)	             func(1, 2, 3, key="value")

"""


"""
3.1 Positional Arguments
These are passed in the correct order and must match the function definition.
"""

#Example: Positional Arguments

def add(a, b):
    return a + b

print(add(3, 5))  # Correct
# print(add(3))   # Error: Missing argument


"""
The number of arguments must match the number of parameters.
"""

"""
3.2 Default Arguments
A default value is assigned if no argument is passed.
"""

#Example: Default Arguments

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Uses default value
greet("Alice") # Overrides default


"""#Default arguments must be at the end of the parameter list."""

"""
3.3 Keyword Arguments
Arguments are passed using parameter names.
"""

#Example: Keyword Arguments

def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet(animal="dog", name="Buddy")  # Order doesn’t matter
describe_pet(name="Kitty", animal="cat")  # Same output

"""The order doesn’t matter as long as parameter names are specified."""

"""
3.4 Variable-Length Arguments (*args, **kwargs)

Using *args (Non-Keyword Arguments)
Allows passing multiple arguments as a tuple.
"""

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10


"""*args is used when unsure of the number of arguments."""


"""
Using **kwargs (Keyword Arguments)
Allows passing multiple named arguments as a dictionary.
"""

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25, city="New York")

"""**kwargs allows passing dynamic keyword arguments."""



"""
4. Lambda Functions (Anonymous Functions)
A lambda function is a small, one-line function without a name.

Syntax of a Lambda Function

lambda arguments: expression
"""

cube = lambda x: x ** 3
print(cube(3))  # Output: 27


"""
Lambda functions don’t use def or return.
Used for short, simple operations.
"""