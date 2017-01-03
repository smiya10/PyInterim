# This is the most important part: this # signifies a comment
# It applies only until the end of the line

##### Import #####

import math   # This is an import. 
# Imports say to use a library of someone else's code.
# That way you don't have to reinvent the wheel. 

##### Variables and assignment #####

dogs = 8
# This statement assigns the value 8 to the variable beans
# 'dogs' is a variable. It stores some piece of information
#       In this case, it stores the integer 8
# '=' means that the value on the right side is stored into the variable on the left side
#       Unlike in math, the left side must always be a variable
# '8' is a number value to be stored in the variable 'dogs'

cats = 32
# Like the above statement, this statement stores the value 32 in a variable called cats

dogs = 19
# Because these are "variables," they can change.
# The variable dogs now contains 19, replacing the previous value 8

##### Displaying variables #####

print("Hello World") # displays "Hello World"
# print() is a function which prints the literal phrase "Hello World" to the screen
# Note that a newline is added to the end of each print statement.
#       (You can change this, but it's complicated so don't worry about it)

print(dogs) # displays "19"
# Because this statement does not have quotation marks around dogs
#       it treats dogs as a variable instead of literally printing "dogs"
# The variable dogs contains 19 so the number 19 is displayed on the screen

##### Tabbed Lived Matter #####

    # It is important to note that unlike in other languages, spaces matter
    # If a statement is tabbed over like this, it will cause an error
    # You will learn the appropriate times for tabbing code later in this course
    #       (For the curious, it is to signify blocks of code inside loops and conditionals)

##### Data Types #####

int_example = 5
# This variable stores 5, an integer (appreviated "int"), meaning it is a whole number

float_example = 4.9
# This variable stores 4.9, a floating-point number (abbreviated "float"), meaning it is not a whole number
# This difference is necessary because ints and floats are stored differently in memory
# Unlike other languages, Python makes the conversion beween numeric types simple
#       If a number contains a decimal, it automatically becomes a float in Python
#       (This was not the case in Python 2 where division between ints produced an integer answer; i.e. 4 / 3 => 1)

string_example = "five"
# Strings are collections of characters and are not numeric.
# Strings behave similarly to lists and other collections you will learn later


