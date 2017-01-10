##### 01-control_flow.py
##### Code example for control flow, conditionals, and boolean logic

### Control Flow

## if statement
bool_example = True
if bool_example:
    print("bool example is True")
# if works just like English. If the stuff after it is true, it does the stuff in the following code block
#       code block denoted by tabbing

## else statement
if bool_example:
    print("bool example is True")
else:
    print("it was false")
# just like in English, the else statement denotes the block of code to be executed if the if statement is not true
# in this case, bool_example is True, so the else would not be executed
# 'else' can only follow if or elif

## elif statement
another_bool = False
if another_bool:
    print("another bool is True")
elif bool_example:
    print("bool example is True")
else:
    print("nothing was true")
# elif is short for "else if"
# if the first if evaluates to false, it tries the first elif, then the second, and so on until it reaches an else or something is true
# it's like a ladder. You keep going up the rungs until a rung breaks or you reach the roof

### Conditionals

## Equality ==
x = 9
y = 8
if y == x:
    print("Equality")
else:
    print("Diversity")
# the double equal sign '==' is a comparison rather than assignment
# if the values on each side are the same, it evaluates to True; if they are different, False
# this statement prints "Diversity" because x is not equal to y
# unlike the '=' operator, nothing is changed by '=='

## Not Equals !=
if x != y:
    print("One of these things is not like the other")
# '!=' is the opposite of '=='
# If the two items have different values, '!=' evaluates to True

## Greater Than > an Less Than <
if x > y:
    print("x wins")
if y < x:
    print("y loses")
# '>' and '<' work just like math
# Notice that these if statements are unrelated. Because they are both 'if' (not else or elif), they are not extensions of each other so both can be executed
#       Where only one can be executed out of an if...elif...else... sequence

## Greater Than or Equal To >= and Less than or Equal To <=
x = 4
y = 4
if x >= y:
    print("x wins")
if y <= x:
    print("y loses")
# '>=' and '<=' work like math (although they look different from the math versions)
# Again, both if statements can be evaluated to true in this example because equal is included in both statements

## Multiple Conditions
if 2 < x <= 9:
    print("x is in (2,9]")
# Python allows multiple comparisons in a row, like you would see in math
#       But don't get too comfy - other languages (Java) aren't so generous

### Boolean Logic

## and
if x == 4 and bool_example:
    print("Both true")
# 'and' works like English - if the first is true AND the second is true, it is true

## or
if x > 4 or y <= 4:
    print("Something about 4")
# 'or' also works like English - if the first is true OR the second is true, it is true

## not
if not x > 9:
    print("x is not unlike something less than or equal to 9")
# once again, 'not' works like English
#       If it's NOT true, it's false
#       If it's NOT false, it's true
# 'not' just switches between true and false

### Collection Logic

## in
if 5 in [4, 5, 6, 7]:
    print("In the list")
# lastly, 'in' works like English - it is true if the value is IN the collection
#       Not only lists, but also tuples, strings, and dicts (for dicts, it uses the keys)
