##### Strings Example #####

### Concatenation
str1 = "hello "
str2 = "world"
print(str1 + str2) # prints "hello world"
# using + symbol concatenates or puts the two together

### Repeating Strings
str1 = "9"
num = 9
print(str1 * num) # prints "999999999"
# Even if the string looks like a number as in "9", it still behaves as a string
#       Multiplying a string by an integer repeats the string that many times
#       Multiplying by a float causes an error

### Input
usr_input = input()
# Waits until user types something and presses enter, then stores to usr_input
# input() is a function which returns a string (you'll learn those soon)
print(usr_input) # prints exactly what the person typed originally


usr_input_2 = input("Enter a number: ")
# input() can also dispay a string to the user to ask for a value as seen above

### Casting

int_string = "98" # string that looks like a number
int_num = int(int_string) # casts the string "98" to integer 98
# if the string cannot be casted to an integer (i.e. "hello" or "93.4"), it will throw an error
#       Errors may be covered later if time allows

float_string = "98.3"
float_num = float(float_string) # casts string "98.3" to float 98.3

num_example = 34.5
num_string = str(num_example) # casts number (can be int or float) 34.5 to string "34.5"

# Other casts include:
#       complex() - converts a string that looks like a complex number to a complex number
#       chr() - converts an integer to it's ascii equivalent

### Formatting strings

inserted_int = 98
string_with_int = "Integer here: %d." % inserted_int
print(string_with_int) # prints "Integer here: 98"
# Formatting strings are formed by using "argument specifiers"
# To insert an integer, use "%d" (I have no clue why it's %d) and specifying the number afterward using a % (not modulo here)
# If a float is specified, it will be truncated to an integer for the string
# Formatting strings are an alternative to concatenation
#       As is the string method join() which can be found in the API
# This method is left over from older languages like C

inserted_float = 2.2
string_with_float = "Float here: %f" % inserted_float
print(string_with_float) # prints "Float here: 2.200000"
# Does the same as above but using a float and "%f" specifier
# Prints with several decimal points
#       This can be changed, but not in this course because it gets complicated quickly

inserted_string = "James"
string_with_insert = "Hello, %s. How are you?"
print(string_with_insert) # prints "Hello, James. How are you?"
# Does the same but with a string and specifier "%s"
# Can be used with anything that can be converted to a string, including numbers, lists, and some other objects

string_with_nums = "I have %d %s and %f %s" % (10, "fingers", 9.5, "toes")
print(string_with_nums) # prints "I have I have 10 fingers and 9.500000 toes"
# To print multiple items in one string, use what's called a tuple (you will learn this later)
#       It's just a bunch of values separated by commas within parentheses
