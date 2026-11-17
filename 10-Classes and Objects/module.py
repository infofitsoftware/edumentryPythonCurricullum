"""
================================================================================
MODULE 10 — Classes and Objects
Student lesson file (beginner fundamentals, stepwise)
================================================================================
How to use this file:
  1. Read one section comment
  2. Run:  python module.py
  3. Change values and rerun
  4. Then open module_exercises.md

Previous: Module 9 (important modules)
Next:     Module 11 (exception handling)

Stay focused on fundamentals. Inheritance is only a light preview.
================================================================================
"""

print("=== Module 10: Classes and Objects ===")

# --------------------------------------------------
# 1) Class = blueprint, object = instance
# --------------------------------------------------


class Dog:
    def bark(self):
        print("Woof!")


dog1 = Dog()
dog2 = Dog()
dog1.bark()
dog2.bark()
print("type:", type(dog1).__name__)

# --------------------------------------------------
# 2) self + __init__ — this object's data
# --------------------------------------------------


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def get(self):
        return self.value


c = Counter()
c.increment()
c.increment()
print("counter:", c.get())  # 2

# --------------------------------------------------
# 3) Student — data + methods together
# --------------------------------------------------


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = []   # per-object list (created in __init__)

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def info(self):
        return f"{self.name} ({self.grade}) avg={self.average():.1f}"


alice = Student("Alice", "A")
alice.add_score(90)
alice.add_score(80)
print(alice.info())

bob = Student("Bob", "B")
bob.add_score(70)
print(bob.name, bob.average())

# Separate objects → separate data
print("alice scores:", alice.scores)
print("bob scores:", bob.scores)

# --------------------------------------------------
# 4) Instance vs class attributes
# --------------------------------------------------


class BankAccount:
    bank_name = "EduBank"  # shared class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


a1 = BankAccount("Ada", 100)
a2 = BankAccount("Alan", 50)
a1.deposit(40)
print(a1.owner, a1.balance)
print(a2.owner, a2.balance)
print("bank:", BankAccount.bank_name)

# --------------------------------------------------
# 5) BAD vs GOOD: shared mutable class attribute
# --------------------------------------------------


class BadBag:
    items = []  # shared by ALL BadBag objects — usually wrong


b1 = BadBag()
b2 = BadBag()
b1.items.append("apple")
print("BadBag b2 sees:", b2.items)  # ['apple'] surprise!


class GoodBag:
    def __init__(self):
        self.items = []  # each object gets its own list


g1 = GoodBag()
g2 = GoodBag()
g1.items.append("apple")
print("GoodBag g2 sees:", g2.items)  # []

# --------------------------------------------------
# 6) __str__ and methods calling methods
# --------------------------------------------------


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, Rs.{self.price})"


print(Product("Mouse", 499))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"area={self.area()}, perimeter={self.perimeter()}"


print(Rectangle(4, 5).describe())

# --------------------------------------------------
# 7) Light encapsulation style (underscore convention)
# --------------------------------------------------


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print("C:", t.get_celsius(), "F:", t.to_fahrenheit())

# --------------------------------------------------
# 8) Inheritance preview only (IS-A)
# --------------------------------------------------


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"


misty = Cat("Misty")
print(misty.name, "->", misty.speak())
print("isinstance Cat?", isinstance(misty, Cat))
print("isinstance Animal?", isinstance(misty, Animal))


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} ({self.role})"


class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name, "Manager")
        self.team_size = team_size

    def describe(self):
        return f"{super().describe()}, team_size={self.team_size}"


print(Manager("Sam", 5).describe())

# --------------------------------------------------
# 9) Composition preview only (HAS-A)
# --------------------------------------------------


class Engine:
    def start(self):
        return "engine started"


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()

    def start(self):
        return f"{self.model}: {self.engine.start()}"


print(Car("Sedan").start())

# --------------------------------------------------
# 10) Beginner real-world style objects
# --------------------------------------------------


class User:
    def __init__(self, name, role):
        self.name = name.strip().title()
        self.role = role.strip().lower()

    def is_admin(self):
        return self.role == "admin"

    def __str__(self):
        return f"User({self.name}, {self.role})"


class Prompt:
    def __init__(self, text):
        self.text = text.strip()

    def length(self):
        return len(self.text)

    def __str__(self):
        return f"Prompt({self.text!r})"


print(User("  ada  ", "Admin"))
print(User("ada", "Admin").is_admin())
print(Prompt("  Summarize this article.  "))
print("prompt length:", Prompt("  hi  ").length())

# --------------------------------------------------
# 11) Common mistakes (commented)
# --------------------------------------------------
# 1. Missing self in method definitions
# 2. Forgetting self.name = name in __init__
# 3. Shared class list: items = []
# 4. Calling Student.average() instead of alice.average()
# 5. Jumping to inheritance before basic classes are solid

print("\n--- Module 10 complete. Open module_exercises.md and practice. ---")
