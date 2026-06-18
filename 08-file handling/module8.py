"08-file handling: File Handling in Python"

"""Introduction to File Handling
File handling in Python allows reading and writing data to files. Python provides built-in functions to work with files efficiently.

Modes of File Handling
"r" → Read mode (default)
"w" → Write mode (overwrites file)
"a" → Append mode (adds data without overwriting)
"x" → Exclusive creation mode (fails if file exists)
"rb", "wb", "ab" → Binary modes
"""

"""Opening and Closing Files (open() and close())
Python’s open() function is used to open a file for reading or writing."""

file = open("example.txt", "r")  # Open file in read mode
file.close()  # Always close the file after use


#Opening and Closing a File

file = open("sample.txt", "w")
file.write("Hello, this is a test file.")
file.close()


"""Reading from Files (read(), readline(), readlines())"""

"Reading the Entire File (read())"
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


"Reading Line by Line (readline())"
file = open("sample.txt", "r")
lines = file.readlines()  # Returns a list of all lines
print(lines)
file.close()

"Reading All Lines (readlines())"
file = open("sample.txt", "r")
lines = file.readlines()  # Returns a list of all lines
print(lines)
file.close()


"Writing to Files (write(), writelines())"
"Writing to a File (write())"

file = open("output.txt", "w")
file.write("This is a new line.\n")
file.close()

"""Writing Multiple Lines (writelines())"""

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("output.txt", "w")
file.writelines(lines)
file.close()


"""Appending Data (a mode)"""
"Appending mode ("a") allows adding content without overwriting the file."

file = open("output.txt", "a")
file.write("This line will be appended.\n")
file.close()

"""Using with Statement for File Handling
Using with automatically closes the file after execution."""

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
# No need to call file.close()



"""Working with Binary Files
For handling non-text files (images, videos, etc.), use binary mode (rb, wb)."""

"Reading a Binary File"

with open("image.jpg", "rb") as file:
    data = file.read()
    print("Binary content:", data[:20])  # Display first 20 bytes


"Writing a Binary File"

with open("copy.jpg", "wb") as new_file:
    new_file.write(data)


"Checking if a File Exists (os.path.exists())"

import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")


"""Deleting a File (os.remove())"""
os.remove("sample.txt")  # Deletes the file

