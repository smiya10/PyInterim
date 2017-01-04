# This example shows how to use the basic numeric operations of Python
#       Math in Python is similar to real math so this shouldn't take too long

# Simple assignment example
var1 = 8
# variable var1 is assigned to contain literal integer 8 (same as before)
# 'var1' is a valid variable name because it contains a number but does not start with the number

var2 = 2
# This variable is included just for future use

# Addition example
addition_example = 1 + 1
# addition_example is set equal to 1 + 1 or 2

# Subtraction example
subtraction_example = var1 - var2
# subtraction_example is set equal to var1 minus var2
#       We know what var1 and var2 are so we can calculate that subtraction_example now contains 6
#       But this is not always the case. Variables are called variables because they can change
#       This assignment takes the current value in var1 and var2 to calculate the value
#       It is not a function, so if var1 or var2 changes after the assignment, subtraction_example is not affected

# Multiplication example
multiplication_example = var1 * 6
# multiplication_example is set to var1 multiplied by 6 (48 in this case), nothing special here

# Division evample
division_example = 9 / 3
# As expected, this variable assignment sets division_example to contain the integer 3

# Another Division Example
division_example_2 = 9 / 4
# This example is interesting: 
#       In many languages (including Python 2), dividing an integer by an integer would yield an integer
#       Because 9 / 4 is 2.25, yielding an integer would require truncating (not rounding) the decimal to integer 2
#       Python is nice and makes the value a float so the value is 2.25 as expected (just beware of Java)

# Parentheses Example
parenthesis_example = (5 * var1) / (8 - 9 * var2)
# Parentheses work the same in Python as in math
# Parentheses put their contents first in order of operations
#       Yes, order of operations still applies here
# With var1=8 and var2=2 as stated above, this statement would store -4 into parenthesis_example


