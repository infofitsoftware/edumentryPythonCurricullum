"""
================================================================================
MODULE 10 — CLASSES AND OBJECTS (OOP FUNDAMENTALS)
================================================================================
Run:  python module.py

Prerequisites:
  Modules 1-7 strongly (especially functions & collections)
  Modules 8-9 helpful but not required for core OOP ideas

This file is a REFERENCE — not an assignment.
================================================================================
"""

print("=== Module 10: Classes and Objects ===")

# ==================================================
# 1. WHY CLASSES AND OBJECTS?
# ==================================================
# Functions organize behavior. Classes organize RELATED data + behavior.
# Example: a Student has name, scores, and can compute average.
# Real world: User, Order, FileHandler, Model, Request objects in frameworks.

# ==================================================
# 2. CLASS = BLUEPRINT, OBJECT = INSTANCE
# ==================================================
# Class  -> design / template
# Object -> concrete thing created from the class


class Dog:
    """A simple Dog blueprint."""

    def bark(self):
        print("Woof!")


dog1 = Dog()
dog2 = Dog()
dog1.bark()
dog2.bark()
print("dog1 type:", type(dog1))
print("same class?", type(dog1) is Dog)

# ==================================================
# 3. self — THE CURRENT OBJECT
# ==================================================
# Methods always receive the instance as the first parameter (by convention: self).
# You do NOT pass self manually when calling: dog1.bark()


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def show(self):
        print("value:", self.value)


c = Counter()
c.increment()
c.increment()
c.show()

# ==================================================
# 4. __init__ — CONSTRUCTOR / INITIALIZER
# ==================================================
# Runs automatically when you create an object.


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = []

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

# Each object has its OWN data:
print("alice scores:", alice.scores)
print("bob scores:", bob.scores)

# ==================================================
# 5. ATTRIBUTES
# ==================================================
# Instance attributes: belong to one object (self.name)
# Class attributes: shared by all objects of the class


class BankAccount:
    bank_name = "EduBank"  # class attribute (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner          # instance attribute
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
print("bank:", BankAccount.bank_name, a1.bank_name)

# ==================================================
# 6. __str__ — READABLE STRING FOR print()
# ==================================================


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, Rs.{self.price})"


p = Product("Mouse", 499)
print(p)  # uses __str__

# ==================================================
# 7. METHODS CALLING OTHER METHODS
# ==================================================


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


rect = Rectangle(4, 5)
print(rect.describe())

# ==================================================
# 8. ENCAPSULATION (BEGINNER LEVEL)
# ==================================================
# Convention: _name means "internal use" (not enforced strictly).


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    def get_celsius(self):
        return self._celsius


t = Temperature(25)
print("C:", t.get_celsius(), "F:", t.to_fahrenheit())

# ==================================================
# 9. INHERITANCE — REUSE AND EXTEND
# ==================================================
# Child class gets features from parent class.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"


class Cow(Animal):
    def speak(self):
        return "Moo"


animals = [Cat("Misty"), Cow("Daisy"), Animal("Generic")]
for animal in animals:
    print(animal.name, "->", animal.speak())

# isinstance checks
print("Misty is Cat?", isinstance(animals[0], Cat))
print("Misty is Animal?", isinstance(animals[0], Animal))

# ==================================================
# 10. super() — CALL PARENT VERSION
# ==================================================


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
        base = super().describe()
        return f"{base}, team_size={self.team_size}"


mgr = Manager("Sam", 5)
print(mgr.describe())

# ==================================================
# 11. COMPOSITION — OBJECTS CONTAINING OBJECTS
# ==================================================


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

# ==================================================
# 12. DATACLASS-STYLE PATTERN WITHOUT decorator complexity
# ==================================================
# Many apps use classes as structured records (like enhanced dicts).


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


pt = Point(2, 3)
pt.move(1, -1)
print("point:", pt.x, pt.y)

# ==================================================
# 13. COMMON MISTAKES (commented)
# ==================================================
# 1. Forgetting self in method definitions
# 2. Writing Student.average() instead of alice.average() without instance
# 3. Forgetting to call __init__ fields (AttributeError later)
# 4. Using class attribute mutable list shared across instances:
#      class Bad:
#          items = []   # shared! usually wrong for per-object data
# 5. Confusing class (blueprint) with object (instance)

print("\n--- Module 10 classes and objects reference complete ---")
