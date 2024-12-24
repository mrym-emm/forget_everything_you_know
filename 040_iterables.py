"""
Iterables = An object/collection that can return its elements one at a time,
            allowing it to be iterated over in a loop
"""
# lists are iterable
numbers = [1,2,3,4,5]

for num in reversed(numbers):
    print(num, end = "-")

print()
# tuples are also iterable
numbers = (1,2,3,4,5)

for num in numbers:
    print(num, end = "-")

print()
fruits = {"apple", "banana", "kiwi"}
print(fruits)

# sets are non reversible so cannot use reversed()
for fruit in fruits:
    print(fruit)

name = "maryam"

for char in name:
    print(char, end= "")

print()
my_dict = {"A": 1, "B": 2, "C": 3 }

for key in my_dict: # this will return only the key
    print(key)

for value in my_dict.values(): # this will return only the key
    print(value)

for key,value in my_dict.items():
    print(f"{key} = {value}")
