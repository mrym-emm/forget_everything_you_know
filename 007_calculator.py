# python calculator

operator = input("Enter an operator ( + - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == '+':
    print(f"Result is {num1 + num2}")

elif operator == '-':
    print(f"Result is {num1 - num2}")

elif operator == '*':
    print(f"Result is {num1 * num2}")

elif operator == '/':
    print(f"Result is {round(num1 / num2, 3)}")

else:
    print(f"Invalid operator, please try again!")
