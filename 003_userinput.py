# input() = A function that prompts the user to enter data
#           Returns the entered data as string


name = input("What is your name?:")

# better to typecast to integer to do any future arithmetic operation
age = int(input("How old are you?: "))

age = age +1

print(f"Hello, {name}")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area of your rectangle is {area} cm²")

## Exercise 2 Shopping Cart Program

item = input("What item woud you like to buy: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")












