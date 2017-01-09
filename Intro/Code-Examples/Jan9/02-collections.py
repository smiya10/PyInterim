### 02-collections.py
# This example script shows the basic use of collections

## Types of collections
tuple_example = (2, 9, 49, 2.3, "number")
list_example = [3, 3, 3.3, "3"]
string_example = "hello"
dictionary_example = {"five": 5, "six": 6, "nein", "no"}

print(tuple_example[2]) # prints "49"
# indexes start at 0 so index [2] is the third item

list_example[3] = "three"
# sets the value of index [3] a new value
# strings and tuples are "immutable" meaning it cannot be changed
#       Indexes cannot be set to new values and the length cannot change

print(len(tuple_example)) # prints "5"
# len() prints the length of the collection
# works on any collection

print(tuple_example[0:3]) # prints "(2, 9, 49)"
# separating two indexes by a colon does "slicing"
# returns the a collection (same type as original) containing the indexes from the first index to (but not including) the second index

print(tuple_example[0:4:2]) # prints "(2, 49)"
# a third index in the slice makes it go by that number (in this case, every two)

print(dictionary_example["five"]) # prints "5"
# with dictionaries, keys are used instead of indexes
# keys are the first values in the colon-separated pairs and values are second
#       i.e. "five": 5 -> "five" is key and 5 is value

list_example.append(999)
print(list_example) # prints "[3, 3, 3.3, '3', 999]"
# lists are mutable so its append() function adds a value
# (the python interpreter may use '' instead of "" for strings but it doesn't matter)

print(list_example * 2) # prints [3, 3, 3.3, '3', 999, 3, 3, 3.3, '3', 999]
# like strings, you can multiply all collections by an integer to repeat it

print(list_example + ["additional", "stuff"]) # prints "[3, 3, 3.3, '3', 999, 'additional', 'stuff']"
# also like strings, lists can be concatenated (only with the same type though)

print(list_example.pop()) # prints "999"
# pop() removes last value and returns it
print(list_example) # prints "[3, 3, 3.3, '3']"
# Note that the 999 has been removed from the list

list_example.remove(3.3)
print(list_example) # prints "[3, 3, '3']"
# you can remove elements by popping by index or removing by element
#       If an element is contained twice, it will remove first instance

## More functions for lists and dictionaries can be found in the API
## You will need to use the API
