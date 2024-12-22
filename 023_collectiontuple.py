"""
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
"""

fruits = ("apple", "banana", "coconut","apple", "dates", "dates")
print(fruits)

print(len(fruits))

print("dates" in fruits)

# returns first occurence
print(fruits.index("apple"))

print(fruits.count("apple"))

# can iterate, will print out everything
for fruit in fruits:
    print(fruit)