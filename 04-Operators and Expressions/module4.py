"Module 3: Operators and Expressions"

"""
Operators are symbols that perform operations on variables and values. Expressions are combinations of values, variables, and operators that produce a result.
In this module, we will explore different types of operators in Python and how they work.
"""

"""
1. Arithmetic Operators
These operators perform mathematical operations like addition, subtraction, multiplication, and division.

Operator	                                       Symbol	                              Example	Result
Addition	                                          +	                                    10 + 5	  15
Subtraction	                                          -	                                    10 - 5	   5
Multiplication	                                      *	                                    10 * 5	   50
Division	                                          /	                                    10 / 3	  3.3333
Floor Division	                                     //	                                    10 // 3	   3 (Removes decimal part)
Modulus	                                             %	                                    10 % 3	   1 (Remainder)
Exponentiation	                                     **	                                     2 ** 3	   8 (2³)
"""

a = 10
b = 3

print("Addition:", a + b)  # 13
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)  # 3.3333
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)  # 1
print("Exponentiation:", a ** b)  # 1000


"""
2. Comparison (Relational) Operators
Comparison operators compare values and return a Boolean (True/False) result.

Operator	                               Meaning	                                  Example	                           Result
==	                                        Equal to	                               5 == 5	                            True
!=	                                        Not equal to	                           5 != 3	                            True
>	                                        Greater than	                           10 > 5	                            True
<	                                        Less than	                               2 < 5	                            True
>=	                                        Greater than or equal to	               3 >= 3	                            True
<=	                                        Less than or equal to	                   4 <= 2	                            False

"""

x = 10
y = 5

print(x > y)   # True
print(x < y)   # False
print(x == 10) # True
print(y != 5)  # False


"""
3. Logical Operators
Logical operators are used to combine conditional statements.

Operator	                                 Meaning	                                               Example
and	                             Returns True if both conditions are True	                   (5 > 2) and (10 > 3) → True
or	                             Returns True if at least one condition is True             	(5 > 2) or (10 < 3) → True
not	                             Reverses the Boolean result	                                not (5 > 2) → False
"""

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


"""
4. Assignment Operators
Assignment operators are used to assign values to variables and modify them.

Operator	                                   Meaning	                    Example	                    Equivalent To
=	                                           Assign value	                x = 10	                      x = 10
+=	                                           Add & assign             	x += 5	                      x = x + 5
-=	                                           Subtract & assign	        x -= 3	                      x = x - 3
*=	                                           Multiply & assign	        x *= 2	                      x = x * 2
/=	                                           Divide & assign	            x /= 2	                      x = x / 2
//=	                                           Floor divide & assign	    x //= 2	                      x = x // 2
%=	                                           Modulus & assign	            x %= 3	                      x = x % 3
**=	                                           Exponentiate & assign	    x **= 2	                      x = x ** 2
"""

x = 10
x += 5  # x = x + 5
print(x)  # 15

x *= 2  # x = x * 2
print(x)  # 30

"""
5. Identity and Membership Operators
Identity Operators (is, is not)
Identity operators check if two variables point to the same object in memory.

Operator	           Meaning	                                                 Example
is	                  Returns True if objects are identical	                      x is y
is not	             Returns True if objects are not identical	                x is not y


"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (same memory location)
print(a is c)   # False (different objects)
print(a == c)   # True (same content)


"""
Membership Operators (in, not in)
Membership operators check if a value exists within a sequence (list, tuple, string, etc.).

Operator	                    Meaning	                                     Example
in	                    Returns True if a value is found	              'a' in 'apple'
not in	                  Returns True if a value is not found	         5 not in [1, 2, 3]
"""


fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("grape" not in fruits)  # True

