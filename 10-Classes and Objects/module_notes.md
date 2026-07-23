# Module 10 — Classes and Objects (OOP Fundamentals)

**Course:** Utrains Python Fundamentals  
**Prerequisites:** Modules 1–7 (functions & collections essential)  
**Suggested position:** After Functions / Collections; complements Files & Modules  

---

# Slide 1 — Title

## Classes and Objects

**Big idea:** Bundle **data + behavior** into reusable blueprints.

```
Class  = blueprint
Object = real instance built from the blueprint
```

---

# Slide 2 — Learning Objectives

1. Explain class vs object  
2. Define classes with methods and `self`  
3. Use `__init__` to initialize attributes  
4. Create and use multiple independent objects  
5. Distinguish instance vs class attributes  
6. Use `__str__` for readable printing  
7. Apply beginner **inheritance** and `super()`  
8. Recognize composition (“has-a”)  
9. Avoid common OOP beginner mistakes  

---

# Slide 3 — WHY OOP?

Without classes (only variables + functions):

```python
student_name = "Alice"
student_scores = [90, 80]
# easy to mix up data for many students
```

With classes:

```python
alice = Student("Alice", "A")
alice.add_score(90)
```

**Career:** Django models, FastAPI schemas, pandas objects, ML estimators, UI widgets — all object-based.

---

# Slide 4 — WHAT: Class vs Object

**Analogy:**

- Class `Dog` = cookie cutter  
- Objects `dog1`, `dog2` = cookies  

All dogs can `bark()`, but each may have different `name`.

---

# Slide 5 — First Class

```python
class Dog:
    def bark(self):
        print("Woof!")

dog1 = Dog()
dog1.bark()
```

Steps:

1. Define class  
2. Create object with `Dog()`  
3. Call method with `dog1.bark()`  

---

# Slide 6 — Understanding self

`self` means **this object**.

```python
def increment(self):
    self.value += 1
```

When you write `c.increment()`, Python calls `Counter.increment(c)`.

**You never pass self manually** in normal calls.

---

# Slide 7 — __init__ (Initializer)

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

```python
alice = Student("Alice", "A")
print(alice.name)
```

`__init__` runs automatically on object creation.

---

# Slide 8 — Trace Object Creation

```python
alice = Student("Alice", "A")
```

**Trace:**

1. Create empty Student object  
2. Call `__init__(alice, "Alice", "A")`  
3. Set `alice.name`, `alice.grade`  
4. Name `alice` now refers to that object  

---

# Slide 9 — Methods Use Attributes

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores)
```

Objects keep their own `scores` lists.

---

# Slide 10 — Many Objects, Separate Data

```python
a = Student("Alice")
b = Student("Bob")
a.add_score(90)
b.add_score(70)
```

Changing `a` does **not** change `b`.

**Ask:** What if `scores = []` was a class attribute instead of created in `__init__`?

---

# Slide 11 — Instance vs Class Attributes

```python
class BankAccount:
    bank_name = "EduBank"      # shared

    def __init__(self, owner):
        self.owner = owner     # per object
        self.balance = 0
```

| Kind | Belongs to | Example |
|------|------------|---------|
| Instance | one object | `balance` |
| Class | whole class | `bank_name` |

---

# Slide 12 — __str__

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, Rs.{self.price})"

print(Product("Mouse", 499))
```

Makes debugging and logging readable.

---

# Slide 13 — Encapsulation (Beginner)

Keep internal details tidy:

```python
self._celsius = celsius   # "internal" by convention
```

Provide methods like `get_celsius()` / `to_fahrenheit()`.

Python does not strictly privatize; convention guides teamwork.

---

# Slide 14 — Inheritance (IS-A)

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Meow"
```

`Cat` **is an** `Animal` and can override `speak`.

---

# Slide 15 — Trace Polymorphism

```python
animals = [Cat("Misty"), Animal("Generic")]
for a in animals:
    print(a.speak())
```

Same method name, different behavior per object type.

---

# Slide 16 — super()

```python
class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name, "Manager")
        self.team_size = team_size
```

`super()` calls the parent version — avoid duplicating setup code.

---

# Slide 17 — Composition (HAS-A)

```python
class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
```

A car **has an** engine (object inside object).  
Often clearer than deep inheritance.

---

# Slide 18 — isinstance

```python
isinstance(misty, Cat)     # True
isinstance(misty, Animal)  # True
```

Useful for safe type checks (prefer over fragile string checks).

---

# Slide 19 — OOP + Prior Modules

| Earlier skill | Used in classes |
|---------------|-----------------|
| Functions | methods |
| Lists/dicts | attributes |
| if/loops | method logic |
| files/json | save object data later |

---

# Slide 20 — Common Beginner Mistakes

1. Missing `self` in method signature  
2. Forgetting `__init__` assignments  
3. Shared mutable class attributes (`items = []`)  
4. Calling method on class without instance incorrectly  
5. Confusing blueprint with instance  
6. Overusing inheritance where composition fits better  

---

# Slide 21 — Professional Connection

| Domain | Objects |
|--------|---------|
| Backend | User, Order, Serializer |
| Data | DataFrame-like pipelines |
| AI | Model, Dataset, Trainer |
| Automation | Job, Task, Client |
| DevOps | Resource, Deployment configs |

---

# Slide 22 — Concept Recap

- class / object / `self`  
- `__init__`, attributes, methods  
- `__str__`  
- inheritance / `super()` / `isinstance`  
- composition  

---

# Slide 23 — Syntax Cheat Sheet

```python
class Name:
    shared = 1
    def __init__(self, x):
        self.x = x
    def method(self):
        return self.x
    def __str__(self):
        return str(self.x)

class Child(Name):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
```

---

# Slide 24 — Mistakes Checklist

- [ ] Methods include `self`?  
- [ ] Per-object data created in `__init__`?  
- [ ] Avoid shared mutable class lists?  
- [ ] Create instances with `ClassName(...)`?  
- [ ] Inheritance only when IS-A is clear?  

---

# Slide 25 — “Can You Explain This?”

1. Class vs object?  
2. What is `self`?  
3. Why `__init__`?  
4. Instance vs class attribute?  
5. Inheritance vs composition?  

---

# Slide 26 — Mini Challenges

1. `Book(title, author)` with `__str__`  
2. `BankAccount` deposit/withdraw  
3. `Dog(Animal)` override `speak`  
4. List of students; print averages  

---

# Slide 27 — What You Can Do Now

- Model real entities as classes  
- Keep related data/behavior together  
- Extend classes with inheritance  
- Read OOP code in libraries/frameworks  

---

# Slide 28 — Where This Fits in the Curriculum

Recommended order:

```
Functions → Collections → Classes/Objects → Files/Modules projects
```

You can study this module after Module 7 even if you already finished 8–9.

---

# Slide 29 — Lab Directions

1. Run `module.py`  
2. Complete `module_exercises.md`  
3. Take `module_quiz.json`  

---

*End of Module 10 teaching slides*
