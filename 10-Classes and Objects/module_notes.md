# Module 10 — Classes and Objects

**For students (beginners)**  
**Prerequisites:** Modules 1–7 strongly (functions + collections). Modules 8–9 help, but are not required for the core ideas.  
**Next:** Module 11 — Exception Handling  

Read this slowly. Run the examples in `module.py`. Then do `module_exercises.md`.

This lesson stays on **fundamentals**.  
We will not rush into advanced OOP. Learn one step at a time.

---

## 1. What you will learn today

By the end of this lesson you should be able to:

1. Explain **class vs object** in plain English  
2. Create a simple class and call a method  
3. Understand **`self`**  
4. Use **`__init__`** to store data on an object  
5. Write methods that use and update attributes  
6. Create **multiple independent objects**  
7. Tell **instance attributes** from **class attributes**  
8. Use a simple **`__str__`**  
9. Read a **beginner inheritance** example (IS-A)  
10. Spot common beginner/AI mistakes (missing `self`, shared `[]`)  

---

## 2. Why classes matter (AI era) — keep it simple

So far you used:

- variables for data  
- functions for behavior  

That works… until related pieces grow:

```python
student_name = "Alice"
student_scores = [90, 80]
# now imagine 50 students — easy to mix up
```

A class lets you keep **related data + behavior** together:

```python
alice = Student("Alice")
alice.add_score(90)
```

| Place | Everyday object idea |
|-------|----------------------|
| Backend | User, Order |
| AI apps | Prompt, Message, ModelConfig |
| Automation | Task, Job |
| Files/data | Report, Record |

**Golden rule:**  
If AI writes a class for you, check **`self`**, **`__init__` assignments**, and whether lists/dicts are created **per object** (not shared on the class).

---

## 3. Class vs object (step 1)

```
Class  = blueprint
Object = real thing built from the blueprint
```

Analogy:

- Class `Dog` = cookie cutter  
- Objects `dog1`, `dog2` = cookies  

All dogs can bark. Each dog can have a different name.

---

## 4. Your first class (step 2)

```python
class Dog:
    def bark(self):
        print("Woof!")

dog1 = Dog()
dog1.bark()
```

Do these three moves every time:

1. **Define** the class  
2. **Create** an object with `Dog()`  
3. **Call** a method with `dog1.bark()`  

Writing `Dog.bark()` without an object is usually the wrong beginner move.

---

## 5. What is `self`? (step 3)

`self` means **this object**.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

When you write:

```python
c = Counter()
c.increment()
```

Python roughly does: “call `increment` on object `c`.”

**You do not pass `self` yourself** in normal calls.  
But you **must** include `self` as the first parameter in the method definition.

---

## 6. `__init__` — set up the object (step 4)

`__init__` runs automatically when you create an object.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

alice = Student("Alice", "A")
print(alice.name)   # Alice
```

### Trace

```python
alice = Student("Alice", "A")
```

1. Create a new Student object  
2. Call `__init__(alice, "Alice", "A")`  
3. Store `alice.name` and `alice.grade`  
4. Name `alice` now refers to that object  

If you forget `self.name = name`, later code will crash with `AttributeError`.

---

## 7. Methods that use attributes (step 5)

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
```

Pattern:

1. Store data in `__init__`  
2. Change/use that data in methods  
3. Return a result when useful (Module 7 habit)

---

## 8. Many objects = separate data (step 6)

```python
a = Student("Alice")
b = Student("Bob")
a.add_score(90)
b.add_score(70)
```

Changing `a` does **not** change `b`.  
Each object has its own `scores` list.

This is one of the biggest reasons classes exist.

---

## 9. Instance attributes vs class attributes (step 7)

```python
class BankAccount:
    bank_name = "EduBank"      # class attribute (shared)

    def __init__(self, owner):
        self.owner = owner     # instance attribute (per object)
        self.balance = 0
```

| Kind | Belongs to | Example |
|------|------------|---------|
| Instance | one object | `balance`, `owner` |
| Class | whole class | `bank_name` |

### Important beginner trap

```python
# BAD idea for per-object data
class BadBag:
    items = []   # shared by ALL bags
```

If every bag should have its own list, create it in `__init__`:

```python
class Bag:
    def __init__(self):
        self.items = []
```

AI code often makes this mistake. Check it every time.

---

## 10. `__str__` — nicer printing (step 8)

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, Rs.{self.price})"

print(Product("Mouse", 499))
```

Useful for debugging and logs. Keep it simple.

---

## 11. Methods calling other methods (step 9)

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"area={self.area()}"
```

Once you can do this, you already know the core of beginner OOP.

---

## 12. Light encapsulation (step 10 — optional style)

Sometimes we mark a value as “internal”:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32
```

The underscore `_celsius` is a **convention** (“please treat as internal”).  
Python does not fully hide it. For beginners, just know the style exists.

---

## 13. Inheritance preview (step 11 — fundamentals only)

Inheritance means: child **is a** parent.

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

```python
misty = Cat("Misty")
print(misty.name)     # from Animal
print(misty.speak())  # overridden in Cat
```

### `super()` in one sentence

Use `super()` when the child needs the parent’s `__init__` setup:

```python
class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name, "Manager")
        self.team_size = team_size
```

**Beginner advice:**  
Master normal classes first. Use inheritance only when the IS-A relationship is obvious.

---

## 14. Composition preview (HAS-A) — recognition only

```python
class Engine:
    def start(self):
        return "engine started"

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
```

A car **has an** engine.  
You do not need deep composition design yet — just recognize the pattern.

---

## 15. Real-world preview (still beginner)

### Simple user profile

```python
class User:
    def __init__(self, name, role):
        self.name = name.strip().title()
        self.role = role.strip().lower()

    def is_admin(self):
        return self.role == "admin"
```

### Prompt record (AI-era idea)

```python
class Prompt:
    def __init__(self, text):
        self.text = text.strip()

    def length(self):
        return len(self.text)
```

You are not building Django/FastAPI today.  
You are learning the object fundamentals those tools are built from.

---

## 16. Common mistakes checklist

1. Missing `self` in the method definition  
2. Forgetting `self.name = name` inside `__init__`  
3. Shared mutable class attribute (`items = []`)  
4. Calling a method on the class instead of an instance  
5. Confusing the blueprint (class) with the instance (object)  
6. Jumping to inheritance before basic classes are solid  
7. Shipping AI class code without testing two separate objects  

---

## 17. How to study this lesson

1. Read one section  
2. Run the matching part in `module.py`  
3. Predict output before looking  
4. Do `module_exercises.md` in order (do not skip ahead)  
5. Take `module_quiz.xml`  

If you use AI for help:

- Ask it to explain `self` and `__init__`  
- Create **two objects** and prove their data is separate  
- Re-type the class yourself  

---

## 18. Mini self-check (before the quiz)

Can you answer these out loud?

1. Class vs object?  
2. What is `self`?  
3. Why do we use `__init__`?  
4. Instance attribute vs class attribute?  
5. Why is `items = []` on the class usually dangerous?  
6. What does inheritance mean in one sentence?  

If any answer is unclear, re-read that section and rerun `module.py`.

---

## 19. What “confident” means after Module 10

You can:

- model a simple real entity as a class  
- store per-object data correctly  
- write methods that update/return values  
- create multiple independent objects  
- read basic inheritance code without panic  
- spot beginner/AI OOP mistakes  

Next lesson (Module 11) covers **exception handling** — failing safely when bad input, missing files, or bad object use happens.
