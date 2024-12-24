"""
Membership operators = used to test whether a value or variable
                       is found in a sequence
                       (string, list, tuple, set, dictionary)
                       1. in
                       2. not in
"""

word = "apple"

# letter = input("Guess a letter in the secret word").lower()
letter = "a"

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} is not found")

if letter not in word:

    print(f"{letter} is not found")
else:
    print(f"There is a {letter}")

students = {"Pooh", "Tigger", "Owl"}

# student = "Pooh"
student = "Poohdd"


if student not in students:
    print(f"{student} not in database")
else:
    print(f"{student} is found")


grades = {"Pooh": "A",
          "Tigger": "B",
          "Owl": "C"}

student = "Owl"

if student in grades:
    print(f"{student} grade is {grades.get(student)}")
else:
    print("Student is not found")


email = "haha@gmail!com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")




