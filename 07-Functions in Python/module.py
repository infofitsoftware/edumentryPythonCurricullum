"""
================================================================================
MODULE 7 — Functions in Python
Student lesson file (beginner-friendly, AI-era examples)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 6 (collections)
Next:     Module 8 (file handling)
================================================================================
"""

print("=== Module 7: Functions in Python ===")

# --------------------------------------------------
# 1) Define and call
# --------------------------------------------------


def greet():
    """Print a simple welcome message."""
    print("Hello! Welcome to Python.")


greet()
greet()

# --------------------------------------------------
# 2) Parameters vs arguments
# --------------------------------------------------


def greet_person(name):  # parameter
    print(f"Hello, {name}!")


greet_person("Alice")  # argument
greet_person("Bob")

# --------------------------------------------------
# 3) return vs print
# --------------------------------------------------


def square(num):
    return num * num


result = square(4)
print("Square:", result)
print("Double square:", square(5) * 2)


def demo_return():
    return "first"
    print("never runs")


print(demo_return())


def do_nothing():
    pass


print("No return →", do_nothing())  # None

# AI bug pattern: print instead of return


def square_print_only(n):
    print(n * n)


value = square_print_only(4)
print("Stored value was:", value)  # None

# --------------------------------------------------
# 4) Multiple return values (tuple unpacking)
# --------------------------------------------------


def min_max(values):
    return min(values), max(values)


lo, hi = min_max([3, 9, 1, 7])
print("min:", lo, "max:", hi)

# --------------------------------------------------
# 5) Positional, default, keyword
# --------------------------------------------------


def add(a, b):
    return a + b


print(add(3, 5))
# print(add(3))  # TypeError: missing argument


def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")


greet_with_default()
greet_with_default("Alice")


def power(base, exponent=2):
    return base ** exponent


print(power(5))       # 25
print(power(5, 3))    # 125


def describe_pet(animal, name):
    print(f"{name} is a {animal}.")


describe_pet(animal="dog", name="Buddy")
describe_pet(name="Kitty", animal="cat")
describe_pet("fish", name="Nemo")

# --------------------------------------------------
# 6) *args and **kwargs
# --------------------------------------------------


def add_numbers(*args):
    return sum(args)


print(add_numbers(1, 2, 3, 4))
print(add_numbers(10, 20))


def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describe_person(name="Alice", age=25, city="New York")


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

# --------------------------------------------------
# 7) Local vs global (brief)
# --------------------------------------------------
counter = 0


def increment_local():
    counter = 10  # local — does NOT change global
    print("local counter:", counter)


def read_global():
    print("global counter:", counter)


increment_local()
read_global()  # still 0

# --------------------------------------------------
# 8) Functions + collections / control flow
# --------------------------------------------------


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

# --------------------------------------------------
# 9) Docstrings
# --------------------------------------------------


def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit.__doc__)

# --------------------------------------------------
# 10) Lambda (intro)
# --------------------------------------------------
cube = lambda x: x ** 3
print(cube(3))

add_two = lambda a, b: a + b
print(add_two(2, 3))

pairs = [("Ada", 90), ("Bob", 75)]
print(sorted(pairs, key=lambda item: item[1]))

# Prefer def for anything non-trivial.

# --------------------------------------------------
# 11) Recursion preview
# --------------------------------------------------


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("fib(6) =", fibonacci(6))  # 8

# --------------------------------------------------
# 12) Mutable default trap
# --------------------------------------------------


def add_item_bad(item, bag=[]):
    bag.append(item)
    return bag


print("bad 1:", add_item_bad("a"))
print("bad 2:", add_item_bad("b"))  # surprise: ['a', 'b']


def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag


print("good 1:", add_item("a"))
print("good 2:", add_item("b"))  # ['b'] only

# --------------------------------------------------
# 13) AI-era preview helpers
# --------------------------------------------------


def clean_email(raw):
    return raw.strip().lower()


def build_prompt(task, text):
    clean = text.strip()
    return f"Task: {task}\nText: {clean}"


def is_admin(role):
    return role.strip().lower() == "admin"


print(clean_email("  Student@Example.COM  "))
print(build_prompt("summarize", "  Hello world  "))
print(is_admin("  Admin  "))

# --------------------------------------------------
# 14) Common mistakes (commented)
# --------------------------------------------------
# greet          # does not call
# greet()        # calls
# print instead of return
# def bad(a=1, b):  # SyntaxError
# mutable default: bag=[]

print("\n--- Module 7 complete. Open module_exercises.md and practice. ---")
