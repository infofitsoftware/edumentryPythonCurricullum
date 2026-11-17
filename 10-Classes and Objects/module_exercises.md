# Module 10 — Practice Exercises: Classes and Objects

**For students**

1. Read `module_notes.md`  
2. Run `module.py` and understand each print  
3. Solve exercises **in order** (do not skip ahead)  
4. Predict output before running  
5. If you use AI, explain `self` and `__init__` yourself  

**Difficulty:** [E] Easy · [M] Medium · [C] Challenge  

Stay on fundamentals. Inheritance appears only in section E.

---

## A. First steps: class, object, method

### A1. [E] Empty class
Create class `Empty` with no methods. Create an object and print `type(obj).__name__`.

Expected: `Empty`

### A2. [E] Hello method
Class `Greeter` with method `hello` that prints `Hello!`. Create an object and call it.

### A3. [E] Dog bark
Create `Dog` with `bark(self)` printing `Woof!`. Create two dogs and call `bark` on both.

### A4. [M] Missing self bug
An AI wrote:
```python
class Greeter:
    def hello():
        print("Hello!")
```
What is wrong? Fix it and call `hello` on an object.

---

## B. `__init__`, attributes, simple methods

### B1. [E] Student name
Class `Student` with `__init__(self, name)` storing `self.name`.  
Create `Student("Ada")` and print `.name`.

### B2. [E] Two boxes
Class `Box` with `__init__(self, label)`. Create boxes `"A"` and `"B"`. Print both labels.

Expected: `A B`

### B3. [E] Counter
`Counter` starts at 0. `increment()` adds 1. `get()` returns value.  
Increment twice and print `get()`.

Expected: `2`

### B4. [M] Rectangle area
`Rectangle(width, height)` with `area()` returning the product.  
Print area of `Rectangle(4, 5)`.

Expected: `20`

### B5. [M] Product `__str__`
`Product(name, price)` with `__str__` returning `Product(Mouse, Rs.499)` style text.  
Print `Product("Mouse", 499)`.

---

## C. Separate objects and updating data

### C1. [M] Student scores
`Student(name)` with `scores = []` in `__init__`, plus `add_score` and `average`.  
Add 90 and 80 for Alice. Print average.

Expected: `85.0`

### C2. [M] Prove independence
Create two students. Add different scores to each. Print both score lists.  
Write a comment: why the lists are different.

### C3. [M] BankAccount
`BankAccount(owner, balance=0)` with `deposit`.  
Start at 100, deposit 50, print balance.

Expected: `150`

### C4. [M] Withdraw
Add `withdraw(amount)` that only works if enough balance.  
Start at 100, withdraw 30, print balance. Then try withdrawing 1000 and print whether it succeeded.

### C5. [C] Shared list trap
Show the bug:
```python
class BadBag:
    items = []
```
Append to one bag and print the other bag’s items.  
Then write the fixed `GoodBag` version.

---

## D. Methods calling methods + light style

### D1. [M] Rectangle describe
Add `perimeter()` and `describe()` that uses `area()` and `perimeter()`.  
Print describe for `Rectangle(4, 5)`.

### D2. [M] Temperature
`Temperature(celsius)` stores `_celsius`, with `get_celsius()` and `to_fahrenheit()`.  
Print both for 25.

### D3. [M] User
`User(name, role)` cleans name/role in `__init__`.  
`is_admin()` returns whether role is `"admin"`. Test with `"  Ada  ", "Admin"`.

### D4. [M] Prompt (AI era)
`Prompt(text)` strips text. `length()` returns length.  
Test with `"  Summarize this.  "`.

### D5. [C] Mini gradebook
Create a list of 3 `Student` objects, add scores, then loop and print each `info()` line.

---

## E. Inheritance preview only

### E1. [M] Animal / Cat
`Animal(name)` with `speak()` returning `"..."`.  
`Cat(Animal)` overrides `speak` to `"Meow"`.  
Print name and speak for `Cat("Misty")`.

### E2. [M] isinstance
Using the cat from E1, print `isinstance(misty, Cat)` and `isinstance(misty, Animal)`.

### E3. [C] Manager with super
`Employee(name, role)` with `describe()`.  
`Manager(name, team_size)` calls `super().__init__(name, "Manager")` and extends `describe`.  
Print describe for `Manager("Sam", 5)`.

---

## F. Short written answers (as comments)

### F1. Class vs object?
Answer:

### F2. What is `self`?
Answer:

### F3. Why create lists inside `__init__` instead of on the class?
Answer:

### F4. When is inheritance appropriate for a beginner?
Answer:

---

## Done?

Re-read any weak section in `module_notes.md`, rerun `module.py`, then take `module_quiz.xml`.

**This folder should contain only:**
- `module_notes.md`
- `module.py`
- `module_exercises.md`
- `module_quiz.xml`
