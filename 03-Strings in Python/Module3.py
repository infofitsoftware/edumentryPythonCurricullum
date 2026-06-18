
#1. Introduction to Strings
#string in Python is a sequence of characters enclosed within single ('), double ("), or triple (''' or """)

"""Key Properties of Strings
✅ Immutable: Strings cannot be modified once created.
✅ Indexed: Characters can be accessed using positive and negative indices.
✅ Iterable: Strings can be looped through character by character."""


"""2. Creating Strings in Python
Python allows multiple ways to create a string."""

# Using single, double, and triple quotes
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline 
string using triple quotes.'''

print(str1, str2, str3)

"""3. String Indexing and Slicing"""

"""String Indexing
Each character in a string has a position (index)."""

"""
Characters                           P    Y     T       H      O      N
Forward Indexing                     0    1     2       3      4      5
Reverse Indexing                    -6   -5    -4      -3     -2     -1
"""

word = "Python"
print(word[0])   # Output: P (First character)
print(word[-1])  # Output: n (Last character)


"""String Slicing ([start:end:step])"""

word = "Programming"
print(word[0:5])   # Output: Progr (0 to 4)
print(word[:6])    # Output: Progra (0 to 5)
print(word[3:])    # Output: gramming (from index 3 to end)
print(word[::2])   # Output: Pormig (every 2nd character)
print(word[::-1])  # Output: gnimmargorP (Reversed string)

"""4. List of All String Methods"""

"""
Method                                                          Description

capitalize()	                                           Capitalizes first letter
casefold()	                                               Converts to lowercase (stronger than lower())
center(width)	                                           Centers string within width
count(substring)	                                       Counts occurrences of substring
encode()	                                               Converts string to bytes
endswith(suffix)	                                       Checks if string ends with suffix
expandtabs(tabsize)             	                       Expands tabs to spaces
find(substring)	                                           Returns index of first occurrence of substring
index(substring)	                                       Same as find(), but raises error if not found
isalnum()	                                               Returns True if all characters are alphanumeric
isalpha()	                                               Returns True if all characters are letters
isdigit()	                                               Returns True if all characters are digits
islower()	                                               Returns True if all characters are lowercase
isspace()	                                               Returns True if all characters are whitespace
istitle()	                                               Returns True if string is title-cased
isupper()	                                               Returns True if all characters are uppercase
join(iterable)	                                           Joins elements of iterable with string
ljust(width)	                                           Left-aligns string within width
lower()	                                                   Converts to lowercase
lstrip()	                                               Removes leading whitespace
replace(old, new)	                                       Replaces occurrences of old with new
rfind(substring)	                                       Returns last occurrence of substring
rindex(substring)	                                       Same as rfind(), but raises error if not found
rjust(width)	                                           Right-aligns string within width
rstrip()	                                               Removes trailing whitespace
split(sep)	                                               Splits string into a list
splitlines()	                                           Splits string at line breaks
startswith(prefix)	                                       Checks if string starts with prefix
strip()	                                                   Removes leading and trailing whitespace
swapcase()	                                               Swaps uppercase to lowercase and vice versa
title()	                                                   Converts to title case
upper()	                                                   Converts to uppercase
zfill(width)	                                           Pads string with zeros
"""

"""5. String Methods and Functions
Finding String Length"""

text = "Python"
print(len(text))  # Output: 6


"""Changing Case"""

text = "hello world"
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.title())       # Hello World
print(text.capitalize())  # Hello world


"""Checking String Content"""
print("Python".isalpha())  # True (Only letters)
print("1234".isdigit())    # True (Only digits)
print("Hello123".isalnum()) # True (Letters and numbers)
print("   ".isspace())     # True (Only spaces)



"""Searching in Strings"""
text = "Python programming"
print(text.find("prog"))  # Output: 7
print(text.count("o"))    # Output: 2


"""Replacing and Splitting"""
text = "I love Python"
print(text.replace("love", "like"))  # I like Python

words = text.split()  # Splits string into a list
print(words)  # ['I', 'love', 'Python']

joined_text = "-".join(words)
print(joined_text)  # I-love-Python


"Checking Prefix and Suffix"
text = "hello.py"
print(text.startswith("hello"))  # True
print(text.endswith(".py"))      # True


"""Stripping Whitespace"""
text = "  hello  "
print(text.strip())  # "hello"
print(text.lstrip()) # "hello  "
print(text.rstrip()) # "  hello"


"""6. String Formatting
Using format()"""

name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.

"""Using f-strings (Python 3.6+)"""

print(f"My name is {name} and I am {age} years old.")

"""7.Escape Sequences"""
"""Escape sequences allow special formatting inside strings."""

"""7.
Escape Sequence                Meaning

\n	                           Newline
\t	                           Tab
\\                             Backslash"""

print("Hello\nWorld")  # Newline
print("Name:\tAlice")  # Tab


"""8. Raw Strings (r"string")
Raw strings ignore escape sequences.
"""

print(r"C:\newfolder\test")  # Output: C:\newfolder\test
