### 01-functions.py
# This code example shows the declaration and use of functions

def knockoff_hypot(x, y):
    return sqrt(x**2 + y**2)
# This is a simple function (it does the exact same as math.hypot() )
# To declare a function, you use the 'def' keyword in the format above
# The colon indicates that the following block of code will be the contents of the function
#       The code block is denoted by the tab
# The return value of the function is denoted by the 'return' keyword followed by the value to be returned

def show_square(n):
    squared_value = n**2
    print(squared_value)
# This function does not have a return value, like the print() function
# Instead, it does something to change the state of the computer (in this case by printing)
#       This type of function is not common in a functional language but is possible

def weird_function(a, b, c):
    """
    Calculates the sum of squares divided by three
    :param a: The first parameter
    :param b: The second parameter
    :param c: The third parameter
    :return: Returns the sum of a squared, b squared, and c squared
    """
    ret = a**2 + b**2 + c**2
    return ret
# This function is like others in theory, but it shows the proper documention
# Documenation is represented by a multiline comment (in this setting it is a "docstring") immediately after function declaration in format:
"""
Desciption of function goal
:param variable: Parameters descriptions
...
:return: Specific return value description
"""
# parameters are denoted by ":param" and return value is denoted by ":return" as shown above

import math
def sine_plus_cosine(theta):
    """
    Calculates the sum of sin(theta) and cos(theta)
    :param theta: Angle measure (radians)
    :return: Returns sum of sine and cosine
    """
    return math.sin(theta) + math.cos(theta)
# Functions can use imported modules too
# They can be imported inside the function, but it's better to not

def multireturn_example(a, b):
    """
    Returns a and b concatenated and the lengths of both strings
    :param a: First string to concatenate
    :param b: Second string to concatenate
    :return: Returns a concatenated with b
    """
    a_str = str(a)
    b_str = str(b)
    return (a_str + b_str, len(a_str), len(b_str))
# Returns multiple values as a tuple (we'll discuss it very shortly)
#       Denoted by putting multiple values in parentheses and comma separated

multireturn_tuple = multireturn_example("Guten " + "Tag")
# multireturn_tuple contains ("Guten Tag", 6, 3)
# access individual values in tuple by "indexing" with square brackets
#       Indexes start with 0 (you'll see soon)
print(multireturn_tuple[0]) # prints "Guten Tag"
print(multireturn_tuple[1]) # prints "6"
print(multireturn_tuple[2]) # prints "3"
