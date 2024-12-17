"""
conditional expression = A one line shorcut for the if else statements
                       = Print or assign one of 2 values based on a conditons
                       X if condition else Y
"""

num = -6


print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"

print(result)

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a< b else b

print(max_num)
print(min_num)

age  = 17

status = "Adult" if age >= 18 else "Child"
print(status)

temp = 28
weather = "HOT" if temp > 20 else "COLD"
print(weather)

user_role = "guest"

access_level = "Full Access" if user_role == "admin" else "limited access"

print(user_role)