"""
collection = single "variable" used to store multiple values
List = [] ordered and changeable, DUPLICATES OK
Set = {} unordered and immutable, but ADD/REMOVE OK, NO DUPLICATES
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
"""

fruits = ["apple","banana", "coconut", "dates"]

# print(dir(fruits))
# print(help(fruits))
# print(fruits[::2])
#
# for fruit in fruits:
#     print(fruit)

# counts the length of item in collection
print(len(fruits))
# check item in lists
print("apple" in fruits)

# can replace item in list, and tht list will change
fruits[0] = "epal"

for fruit in fruits:
    print(fruit)

print(fruits)

# append at the end of the list
fruits.append("eggplant")
print(fruits)

# remove element from list
fruits.remove("banana")
print(fruits)

# insert vaLUE at a certain index, DOES NOT REPLACE
fruits.insert(2, "kiwi")
print(fruits)

# sort list
fruits.sort()
print(fruits)

# by default, will reverse the order, for alphabetical then need to sort first
fruits.reverse()
print(fruits)

# # clear list
fruits.clear()
print(fruits)

fruits = ["apple","banana", "coconut", "dates"]

# returns the index of a value in list
print(fruits)
print(fruits.index("banana"))

# counts how many a specified item in list
print(fruits.count("dates"))

