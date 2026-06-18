"""Module 6: Lists in Python (Ordered & Mutable)"""

"""
Introduction to Lists
A list in Python is an ordered, mutable collection that can hold multiple data types. 
Lists allow modification of their elements and support various operations to manipulate and organize data efficiently.
"""

"""
Creating a List
A list is created using square brackets [] and can contain integers, strings, floats, or even other lists.
"""

# Creating an empty list
empty_list = []

# List with different data types
mixed_list = [10, "Python", 3.14, True]

# Nested list
nested_list = [[1, 2, 3], ["a", "b", "c"]]

print(mixed_list)
print(nested_list)


"""
Accessing Elements (Indexing & Slicing)
Indexing: Access elements using their index (0 for the first, -1 for the last).
Slicing: Extract multiple elements using start:end:step.
"""

numbers = [10, 20, 30, 40, 50]

# Accessing first and last elements
print(numbers[0])   # 10
print(numbers[-1])  # 50

# Slicing a sublist
print(numbers[1:4])    # [20, 30, 40]
print(numbers[:3])     # [10, 20, 30]
print(numbers[::2])    # [10, 30, 50] (Every second element)


"""
Modifying and Updating Lists
Lists are mutable, meaning we can update their elements directly.
"""

#Example: Modifying Lists

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Changing "banana" to "blueberry"

print(fruits)

"""
Common List Methods
"""
"""append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()"""




"""append() – Add an Element at the End"""

fruits = ["apple", "banana"]
fruits.append("cherry")

print(fruits)

"""extend() – Extend a List with Another List"""

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])

print(numbers)

"""insert() – Insert an Element at a Specific Position"""

colors = ["red", "blue", "green"]
colors.insert(1, "yellow")  # Insert "yellow" at index 1

print(colors)

"""remove() – Remove a Specific Element"""

animals = ["cat", "dog", "rabbit"]
animals.remove("dog")

print(animals)

"""pop() – Remove and Return an Element (Default Last Element)"""

numbers = [10, 20, 30, 40]
removed_element = numbers.pop(2)  # Removes element at index 2

print(numbers)
print("Removed:", removed_element)

"""sort() – Sort Elements in Ascending Order"""

scores = [50, 30, 40, 10, 20]
scores.sort()

print(scores)

"""reverse() – Reverse the Order of Elements"""

nums = [1, 2, 3, 4, 5]
nums.reverse()

print(nums)

"""count() – Count Occurrences of an Element"""

numbers = [1, 2, 3, 1, 4, 1, 5]
print(numbers.count(1))

"""index() – Find the First Index of an Element"""
names = ["Alice", "Bob", "Charlie", "Alice"]
print(names.index("Alice"))

"""copy() – Copy a List (Shallow Copy)"""

original_list = [1, 2, 3]
copied_list = original_list.copy()

print(copied_list)


"""List Comprehension"""

"""List comprehension provides a concise way to create lists.
Example: Creating a List of Squares"""

squares = [x**2 for x in range(1, 6)]
print(squares)


"""Example: Filtering Even Numbers"""

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]

print(evens)




"""
Introduction to Tuples
A tuple is an ordered, immutable collection in Python. Unlike lists, tuples cannot be modified once created. 
They are used when data should not change throughout the program.
"""

"""
Creating a Tuple
Tuples are created using parentheses () and can contain multiple data types.
"""

# Empty tuple
empty_tuple = ()

# Tuple with different data types
mixed_tuple = (10, "Python", 3.14, True)

# Tuple with a single element (comma is necessary)
single_element_tuple = (5,)

# Nested tuple
nested_tuple = ((1, 2, 3), ("a", "b", "c"))

print(mixed_tuple)
print(nested_tuple)
print(single_element_tuple)


"""
Accessing Elements (Indexing & Slicing)
Indexing: Access elements using their position (0 for the first, -1 for the last).
Slicing: Extract multiple elements using start:end:step.
"""

#Example: Accessing Tuple Elements

numbers = (10, 20, 30, 40, 50)

# Accessing first and last elements
print(numbers[0])   # 10
print(numbers[-1])  # 50

# Slicing a tuple
print(numbers[1:4])    # (20, 30, 40)
print(numbers[:3])     # (10, 20, 30)
print(numbers[::2])    # (10, 30, 50) (Every second element)

"""
Tuple Immutability
Tuples cannot be changed once created. Trying to modify elements will raise an error.
"""

# Example: Attempting to Modify a Tuple

fruits = ("apple", "banana", "cherry")

# Trying to change an element (will cause an error)
#fruits[1] = "blueberry"



"""
Common Tuple methods
"""

#count() – Count Occurrences of an Element
numbers = (1, 2, 3, 1, 4, 1, 5)
print(numbers.count(1))


#index() – Find the First Index of an Element

names = ("Alice", "Bob", "Charlie", "Alice")
print(names.index("Alice"))

#len() – Get the Number of Elements in a Tuple

colors = ("red", "green", "blue", "yellow")
print(len(colors))


"""
Tuple Packing and Unpacking

Packing a Tuple
Tuple packing means storing multiple values in a single tuple.
"""

person = ("John", 25, "Engineer")
print(person)

"""
Unpacking a Tuple
Tuple unpacking extracts values into separate variables.
"""

name, age, profession = person

print(name)        # John
print(age)         # 25
print(profession)  # Engineer


"""
Converting Between Lists and Tuples
Convert List to Tuple
"""

numbers_list = [1, 2, 3, 4]
numbers_tuple = tuple(numbers_list)

print(numbers_tuple)

"""Convert Tuple to List"""

colors_tuple = ("red", "green", "blue")
colors_list = list(colors_tuple)

print(colors_list)


"""
Introduction to Dictionaries
A dictionary in Python is an unordered, mutable collection of key-value pairs.

Keys must be unique and immutable (strings, numbers, tuples).
Values can be any data type (int, list, tuple, another dictionary, etc.).
Dictionaries allow fast lookups based on keys.

Creating a Dictionary
Dictionaries are defined using curly braces {} or the dict() function.
"""

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

# Using dict() function
employee = dict(id=101, name="John Doe", salary=50000)

print(student)
print(employee)




"""
Accessing Dictionary Elements
Use keys to access values with dict[key] or dict.get(key).
"""

#Example: Accessing Dictionary Values

# Accessing values
print(student["name"])   # Alice
print(student.get("age"))  # 22

# Using get() to handle missing keys
print(student.get("email", "Not Available"))  # Not Available

#get() prevents errors if a key doesn’t exist by returning None or a default value.


"""
Modifying a Dictionary
Add a new key-value pair
Update an existing key's value
Delete a key-value pair
"""

#Example: Adding, Updating, and Deleting Data

student["city"] = "New York"  # Adding a new key-value pair
student["grade"] = "A+"  # Updating an existing value
del student["age"]  # Removing a key-value pair

print(student)


"""Common Dictionary Methods"""

"""clear()
copy()
fromkeys(iterable, value)
get(key, default)
items()
keys()
values()
pop(key, default)
popitem()
setdefault(key, default)
update(iterable or dictionary)"""

#keys() – Get All Keys

print(student.keys())

#values() – Get All Values

print(student.values())

#items() – Get All Key-Value Pairs

print(student.items())

#update() – Merge Two Dictionaries

extra_info = {"hobby": "Reading", "age": 22}
student.update(extra_info)

print(student)


#pop() – Remove a Key and Get Its Value

removed_value = student.pop("city")
print(removed_value)  # New York
print(student)


#popitem() – Remove the Last Inserted Key-Value Pair

student.popitem()
print(student)

#Iterating Over a Dictionary

#Use for loops to iterate over keys, values, or key-value pairs.
#Example: Looping Through a Dictionary
# Iterate over keys
for key in student:
    print(key, ":", student[key])

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key} -> {value}")


"""Nested Dictionaries
A nested dictionary contains dictionaries inside dictionaries."""

# Example: Working with Nested Dictionaries

company = {
    "employee1": {"name": "John", "role": "Manager"},
    "employee2": {"name": "Alice", "role": "Developer"}
}

print(company["employee1"]["name"])  # John

"""
Dictionary Comprehension
Similar to list comprehension, dictionary comprehension provides a short way to create dictionaries.
"""

#Example: Creating a Dictionary Using Comprehension

squares = {num: num**2 for num in range(1, 6)}
print(squares)


"""
Introduction to Sets
A set in Python is an unordered, mutable collection of unique elements.

Unordered: Elements are not stored in a particular order.
No Duplicates: A set automatically removes duplicate values.
Mutable: You can add and remove elements.
Heterogeneous: It can contain different data types.
Unindexed: Elements cannot be accessed using an index.


Creating a Set
Sets can be created using curly braces {} or the set() function.
"""

# Creating a set with unique elements
fruits = {"apple", "banana", "cherry", "banana", "apple"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'} (No duplicates)

# Creating an empty set (use set(), NOT {})
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# Creating a set from a list
numbers = set([1, 2, 3, 4, 4, 2])
print(numbers)  # Output: {1, 2, 3, 4}

#Accessing Elements in a Set
#Since sets are unordered, elements cannot be accessed using an index. However, we can iterate through a set.

for fruit in fruits:
    print(fruit)

"""Modifying a Set
Adding Elements (add())"""

fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits.update(["grape", "mango"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange', 'grape', 'mango'}

"""Removing Elements from a Set
remove() – Removes a Specific Element (Throws Error if Not Found)"""

fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange', 'grape', 'mango'}
#If the element does not exist, remove() raises an error.

"""discard() – Removes an Element Without Error"""

fruits.discard("banana")  # No error even if 'banana' is missing

"""pop() – Removes and Returns a Random Element"""

random_element = fruits.pop()
print(random_element)  # Output: A random element from the set


"""clear() – Removes All Elements"""

fruits.clear()
print(fruits)  # Output: set()


"""
Set Operations (Union, Intersection, Difference, Symmetric Difference)
Python sets support mathematical operations like union, intersection, and difference.
"""

#union() – Combines Two Sets

A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))  # Output: {1, 2, 3, 4, 5}

#intersection() – Finds Common Elements
print(A.intersection(B))  # Output: {3}


#difference() – Elements in A but Not in B

print(A.difference(B))  # Output: {1, 2}

#symmetric_difference() – Elements in Either A or B but Not Both

print(A.symmetric_difference(B))  # Output: {1, 2, 4, 5}


# Checking Set Membership
# Example: Checking if an Element Exists in a Set

print(3 in A)  # Output: True
print(10 not in B)  # Output: True

"""Set Comprehension
Set comprehension is similar to list comprehension but results in a set.

Example: Set Comprehension"""

squared_numbers = {x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}


