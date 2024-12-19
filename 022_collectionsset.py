"""
collection = single "variable" used to store multiple values
List = [] ordered and changeable, DUPLICATES OK
Set = {} unordered and immutable, but ADD/REMOVE OK, NO DUPLICATES
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
"""

fruits = {"apple", "banana", "coconut", "dates"}
print(fruits)

print(len(fruits))

# # SETS cannot be indexed bcs theyre unordered
# print(fruits[0])

# add
fruits.add("orange")
print(fruits)

# remove
fruits.remove("apple")
print(fruits)

# pop removes a random item from the set
fruits.pop()
print(fruits)

# clear set
fruits.clear()
print(fruits)

fruits = {"apple", "banana", "coconut", "dates"}
print(fruits)