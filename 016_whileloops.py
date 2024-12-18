"""
while loop = execute some code WHILE some condition remains True

"""

name = input("Enter your name: ")

# this will end the code once the if statements run, but we want the user to give name
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")


while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter age: "))

while age <0:
    print("Age cant be negative")
    age = int(input("Enter age: "))
print(f"You are {age} years old")

food = input("Enter a food you like (q to quit): ")

# can also be written as while not food == 'q':
while food != "q":
    print(f'You like {food}')
    food = input("Enter a food you like (q to quit): ")
print('bye')

num = int(input("Enter a # between 1 - 10:"))

while not 1<= num <= 10:
    print(f"{num} is not valid. Try again")
    num = int(input("Enter a # between 1 - 10:"))
print(f"You choose {num}")
