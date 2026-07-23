# Module 10 — Practice Exercises: Classes and Objects

**Instructions:** Attempt before opening the Instructor Solution Guide.

---

# LEVEL 1 — FUNDAMENTALS

### Exercise 1 — Empty Class Instance

**Difficulty:** Easy  
**Concepts:** class, object  

**Problem:** Create a class `Empty` with no methods. Create an object and print its type name (`type(obj).__name__`).

**Expected Output:**
```
Empty
```

---

### Exercise 2 — Hello Method

**Difficulty:** Easy  
**Concepts:** method, self  

**Problem:** Class `Greeter` with method `hello` that prints `Hello!`. Create an object and call it.

**Expected Output:**
```
Hello!
```

---

### Exercise 3 — Student Init

**Difficulty:** Easy  
**Concepts:** `__init__`, attributes  

**Problem:** Class `Student` with `__init__(self, name)` storing `self.name`. Create `Student("Ada")` and print `.name`.

**Expected Output:**
```
Ada
```

---

### Exercise 4 — Two Independent Objects

**Difficulty:** Easy  
**Concepts:** separate instance data  

**Problem:** Class `Box` with `__init__(self, label)`. Create two boxes `"A"` and `"B"`. Print both labels on one line separated by space.

**Expected Output:**
```
A B
```

---

### Exercise 5 — Counter Class

**Difficulty:** Easy  
**Concepts:** methods updating attributes  

**Problem:** `Counter` starts at 0, `increment()` adds 1, `get()` returns value. Increment twice and print `get()`.

**Expected Output:**
```
2
```

---

# LEVEL 2 — APPLY THE CONCEPT

### Exercise 6 — Rectangle Area

**Difficulty:** Easy  
**Concepts:** methods  

**Problem:** `Rectangle(width, height)` with `area()` returning product. Print area of `Rectangle(4, 5)`.

**Expected Output:**
```
20
```

---

### Exercise 7 — Bank Deposit

**Difficulty:** Medium  
**Concepts:** validation in methods  

**Problem:** `BankAccount(owner, balance=0)` with `deposit(amount)` (ignore non-positive). Deposit `50` into account starting at `100`, print balance.

**Expected Output:**
```
150
```

---

### Exercise 8 — __str__ Product

**Difficulty:** Easy  
**Concepts:** `__str__`  

**Problem:** `Product(name, price)` such that `print(product)` shows `Product(Pen, 10)`.

**Expected Output:**
```
Product(Pen, 10)
```

---

### Exercise 9 — Average Scores

**Difficulty:** Medium  
**Concepts:** list attribute, methods  

**Problem:** `Student(name)` with `add_score` and `average`. Add 80 and 100 for `"Bob"`, print average as int.

**Expected Output:**
```
90
```

---

### Exercise 10 — Class Attribute

**Difficulty:** Easy  
**Concepts:** class attribute  

**Problem:** Class `Vehicle` with class attribute `wheels = 4`. Print `Vehicle.wheels` and `Vehicle().wheels`.

**Expected Output:**
```
4
4
```

---

# LEVEL 3 — COMBINE CONCEPTS

### Exercise 11 — Withdraw

**Difficulty:** Medium  
**Concepts:** methods return bool  

**Problem:** Add `withdraw(amount)` to `BankAccount` returning `True` if success else `False`. Start 100, withdraw 40, print balance and result of withdrawing 1000.

**Expected Output:**
```
60
False
```

---

### Exercise 12 — Inheritance Speak

**Difficulty:** Medium  
**Concepts:** inheritance  

**Problem:** `Animal` with `speak()` returning `"..."`. `Dog(Animal)` overrides to `"Woof"`. Print `Dog("Rex").speak()`.

**Expected Output:**
```
Woof
```

---

### Exercise 13 — isinstance Check

**Difficulty:** Easy  
**Concepts:** isinstance  

**Problem:** Using Exercise 12 classes, print whether a `Dog` instance is an instance of `Animal`.

**Expected Output:**
```
True
```

---

### Exercise 14 — super() Manager

**Difficulty:** Medium  
**Concepts:** super  

**Problem:** `Employee(name, role)` with `describe()`. `Manager(name, team_size)` calls `super().__init__(name, "Manager")` and extends describe to include team size. Print describe for `Manager("Sam", 3)`.

**Expected Output:**
```
Sam (Manager), team_size=3
```

---

### Exercise 15 — List of Objects

**Difficulty:** Medium  
**Concepts:** lists + objects  

**Problem:** Create a list of 3 `Student` objects with scores. Print names of students whose average >= 80.

**Hint:** Loop the list; call `.average()`.

---

### Exercise 16 — Composition

**Difficulty:** Medium  
**Concepts:** composition  

**Problem:** `Battery` with `level` default 100. `Phone` has a `Battery` and method `status()` returning `battery:<level>`. Print status.

**Expected Output:**
```
battery:100
```

---

# LEVEL 4 — PROBLEM SOLVING

### Exercise 17 — Library Book

**Difficulty:** Medium  
**Concepts:** class design  

**Problem:** `Book(title, copies)`. Methods `borrow()` decreases copies if > 0 (return True/False), `return_book()` increases copies. Start with 2 copies; borrow twice; print copies; borrow again print False.

**Expected Output:**
```
0
False
```

---

### Exercise 18 — Playlist

**Difficulty:** Challenging  
**Concepts:** list attribute  

**Problem:** `Playlist(name)` stores songs list. `add(song)`, `count()`, `has(song)`. Add two songs, print count and `has` result for one song.

**Example Output:**
```
2
True
```

---

### Exercise 19 — Shape Hierarchy

**Difficulty:** Challenging  
**Concepts:** inheritance polymorphism  

**Problem:** Base `Shape` with `area()` returning 0. `Circle(r)` area `3.14*r*r`, `Square(side)` area `side*side`. Put both in a list and print areas as ints.

**Example:** Circle 2 → 12, Square 3 → 9

**Expected Output:**
```
12
9
```

---

### Exercise 20 — User Auth Object

**Difficulty:** Challenging  
**Concepts:** methods + strings  

**Problem:** `User(username, password)` with `check_password(pw)` (exact match) and `is_admin` boolean default False. Create admin user `admin`/`secret` with `is_admin=True`. Print check_password result for `"secret"` and `is_admin`.

**Expected Output:**
```
True
True
```

---

# Instructor Solution Guide

```python
# Exercise 1
class Empty:
    pass
print(type(Empty()).__name__)

# Exercise 2
class Greeter:
    def hello(self):
        print("Hello!")
Greeter().hello()

# Exercise 3
class Student:
    def __init__(self, name):
        self.name = name
print(Student("Ada").name)

# Exercise 4
class Box:
    def __init__(self, label):
        self.label = label
print(Box("A").label, Box("B").label)

# Exercise 5
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
print(c.get())

# Exercise 6
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
print(Rectangle(4, 5).area())

# Exercise 7
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
acct = BankAccount("Ada", 100)
acct.deposit(50)
print(acct.balance)

# Exercise 8
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"Product({self.name}, {self.price})"
print(Product("Pen", 10))

# Exercise 9
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def average(self):
        return sum(self.scores) / len(self.scores)
bob = Student("Bob")
bob.add_score(80)
bob.add_score(100)
print(int(bob.average()))

# Exercise 10
class Vehicle:
    wheels = 4
print(Vehicle.wheels)
print(Vehicle().wheels)

# Exercise 11
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
acct = BankAccount("Ada", 100)
acct.withdraw(40)
print(acct.balance)
print(acct.withdraw(1000))

# Exercise 12
class Animal:
    def speak(self):
        return "..."
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Woof"
print(Dog("Rex").speak())

# Exercise 13
print(isinstance(Dog("Rex"), Animal))

# Exercise 14
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
print(Manager("Sam", 3).describe())

# Exercise 15
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def add_score(self, s):
        self.scores.append(s)
    def average(self):
        return sum(self.scores) / len(self.scores)
s1, s2, s3 = Student("A"), Student("B"), Student("C")
s1.add_score(90); s1.add_score(90)
s2.add_score(50); s2.add_score(60)
s3.add_score(80); s3.add_score(85)
for s in [s1, s2, s3]:
    if s.average() >= 80:
        print(s.name)

# Exercise 16
class Battery:
    def __init__(self, level=100):
        self.level = level
class Phone:
    def __init__(self):
        self.battery = Battery()
    def status(self):
        return f"battery:{self.battery.level}"
print(Phone().status())

# Exercise 17
class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies
    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False
    def return_book(self):
        self.copies += 1
book = Book("Python 101", 2)
book.borrow()
book.borrow()
print(book.copies)
print(book.borrow())

# Exercise 18
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add(self, song):
        self.songs.append(song)
    def count(self):
        return len(self.songs)
    def has(self, song):
        return song in self.songs
pl = Playlist("Mix")
pl.add("Song A")
pl.add("Song B")
print(pl.count())
print(pl.has("Song A"))

# Exercise 19
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
for shape in [Circle(2), Square(3)]:
    print(int(shape.area()))

# Exercise 20
class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
    def check_password(self, pw):
        return self.password == pw
admin = User("admin", "secret", is_admin=True)
print(admin.check_password("secret"))
print(admin.is_admin)
```
