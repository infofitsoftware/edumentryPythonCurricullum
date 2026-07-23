"""
================================================================================
MODULE 7 — FUNCTIONS IN PYTHON (Reference Program)
================================================================================
Run:  python module.py

Prerequisites: Modules 1-6 (types, strings, operators, control flow, collections)

This file is a REFERENCE — not an assignment.
================================================================================
"""

print("=== Module 7: Functions ===")

# ==================================================
# 1. WHY FUNCTIONS?
# ==================================================
# Functions package reusable logic.
# Benefits: avoid copy-paste, clearer structure, easier testing.
# Real world: validate_email(), calculate_total(), load_config()

# ==================================================
# 2. DEFINE AND CALL
# ==================================================


def greet():
    """Print a simple welcome message."""
    print("Hello! Welcome to Python.")


greet()
greet()  # reusable — call as many times as needed

# ==================================================
# 3. PARAMETERS VS ARGUMENTS
# ==================================================
# Parameter = name in the definition
# Argument  = value you pass when calling


def greet_person(name):  # name is a parameter
    print(f"Hello, {name}!")


greet_person("Alice")  # "Alice" is an argument
greet_person("Bob")

# ==================================================
# 4. RETURN VALUES
# ==================================================
# print shows something; return sends a value back to the caller.


def square(num):
    return num * num


result = square(4)
print("Square:", result)
print("Double square:", square(5) * 2)

# Code after return in the same function does not run:


def demo_return():
    return "first"
    print("never runs")


print(demo_return())

# Returning nothing explicitly → None


def do_nothing():
    pass


print(do_nothing())  # None

# ==================================================
# 5. MULTIPLE RETURN VALUES (tuple unpacking)
# ==================================================


def min_max(values):
    return min(values), max(values)


lo, hi = min_max([3, 9, 1, 7])
print("min:", lo, "max:", hi)

# ==================================================
# 6. POSITIONAL ARGUMENTS
# ==================================================


def add(a, b):
    return a + b


print(add(3, 5))
# print(add(3))  # TypeError: missing argument

# ==================================================
# 7. DEFAULT ARGUMENTS
# ==================================================


def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")


greet_with_default()
greet_with_default("Alice")

# Defaults must come AFTER non-defaults:
# def bad(a=1, b):  # SyntaxError


def power(base, exponent=2):
    return base ** exponent


print(power(5))       # 25
print(power(5, 3))    # 125

# ==================================================
# 8. KEYWORD ARGUMENTS
# ==================================================


def describe_pet(animal, name):
    print(f"{name} is a {animal}.")


describe_pet(animal="dog", name="Buddy")
describe_pet(name="Kitty", animal="cat")  # order can change with keywords

# Mix: positional first, then keyword
describe_pet("fish", name="Nemo")

# ==================================================
# 9. *args — VARIABLE POSITIONAL
# ==================================================


def add_numbers(*args):
    # args is a tuple of all extra positional arguments
    return sum(args)


print(add_numbers(1, 2, 3, 4))
print(add_numbers(10, 20))

# ==================================================
# 10. **kwargs — VARIABLE KEYWORD
# ==================================================


def describe_person(**kwargs):
    # kwargs is a dict of named arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describe_person(name="Alice", age=25, city="New York")

# ==================================================
# 11. COMBINING PARAMETER STYLES (ORDER)
# ==================================================
# Typical order: positional, *args, keyword-only/defaults carefully, **kwargs
# Beginner-friendly pattern:


def make_profile(name, age, *hobbies, city="Unknown", **extra):
    profile = {
        "name": name,
        "age": age,
        "hobbies": list(hobbies),
        "city": city,
    }
    profile.update(extra)
    return profile


print(make_profile("Sam", 20, "chess", "coding", city="Delhi", role="student"))

# ==================================================
# 12. LOCAL VS GLOBAL SCOPE (BRIEF)
# ==================================================
counter = 0  # global


def increment_local():
    counter = 10  # local — does NOT change global
    print("local counter:", counter)


def read_global():
    print("global counter:", counter)


increment_local()
read_global()  # still 0

# Prefer passing values in/out over changing globals.

# ==================================================
# 13. FUNCTIONS + COLLECTIONS / CONTROL FLOW
# ==================================================


def is_even(n):
    return n % 2 == 0


def even_only(numbers):
    result = []
    for n in numbers:
        if is_even(n):
            result.append(n)
    return result


print(even_only([1, 2, 3, 4, 5, 6]))


def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


print(char_frequency("banana"))


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("5! =", factorial(5))


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("Race car"))

# ==================================================
# 14. LAMBDA (ANONYMOUS) FUNCTIONS
# ==================================================
# Short one-expression functions.


cube = lambda x: x ** 3
print(cube(3))

add_two = lambda a, b: a + b
print(add_two(2, 3))

# Often used later with sorted/map/filter — keep simple for now:
pairs = [("Ada", 90), ("Bob", 75)]
print(sorted(pairs, key=lambda item: item[1]))

# Prefer def for anything non-trivial or multi-line.

# ==================================================
# 15. RECURSION PREVIEW (OPTIONAL PATTERN)
# ==================================================
# A function calling itself. Powerful but easy to misuse.
# Always need a base case.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("fib(6) =", fibonacci(6))  # 8

# ==================================================
# 16. DOCSTRINGS & CLEAR NAMES
# ==================================================


def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit.__doc__)

# ==================================================
# 17. COMMON MISTAKES (commented)
# ==================================================
# 1. Calling before defining (in a simple script top-to-bottom)
# 2. Forgetting parentheses: greet  vs greet()
# 3. Confusing print with return
# 4. Mutable default argument trap:
#    def add_item(item, bag=[]):  # BAD — shared list
#    def add_item(item, bag=None):
#        if bag is None:
#            bag = []
# 5. Default before non-default parameters

print("\n--- Module 7 functions reference complete ---")
