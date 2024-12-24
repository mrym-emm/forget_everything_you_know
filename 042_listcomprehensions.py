"""
List comprehension = A concise way to create lists in Python
                    Compact and easier to read thn traditional loops
                    [expression for value in iterable if condition]
"""

doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)


doubles_comp = [x*2 for x in range(1,11)]

print(doubles_comp)

triples = [x*3 for x in range(1,11)]
print(triples)

squares = [x **2 for x in range (1,11)]

print(squares)

fruits = ["apple", "banana", "kiwi"]

uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)

first_letter = [fruit[0] for fruit in fruits]
print(first_letter)

numbers = [1,-2,3,-4,5,-6, 8, -7]

positive = [num for num in numbers if num > 0]

print(positive)

negative = [num for num in numbers if num < 0]

print(negative)

even = [num for num in numbers if num % 2 == 0]

print(even)

odd = [num for num in numbers if num % 2 != 0]

print(odd)

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grade = [grade for grade in grades if grade >= 60]

print(passing_grade)