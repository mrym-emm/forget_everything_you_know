import math

friends = 5

friends = friends + 1
# the above can also be rewritten as. the '+=' is aka 'augmented assignement operators'
friends += 1

friends -=2

friends *= 3

friends /= 2

# exponential
friends **=2

# remainder
remainder = friends % 3

print(f"You have {friends} friends!")
print(f"You have {remainder} remainder friends")

x =3.14
y = -4
z =5

result = round(x)
result = abs(y)
result = pow(-4, 3)

result = max(x,y,z)
result = min(x,y,z)

print(result)

print(math.pi)
print(math.e)

x = 9.12
result = math.sqrt(x)
result = math.ceil(x)

x = 9.99999
result = math.floor(x)

print(result)

# # Exercise 1: Calculating the circumference of a circle. 2 * pi * radius of circle
#
# formula_constant = 2
# pi = math.pi
# radius = float(input("Insert radius of circle (Its half of the diameter)"))
#
# circumference = formula_constant * pi * radius
#
# print(f"The circumference of the circle is {round(circumference,2)} cm")

## Exercise 2: Calculating the area of a circle. pi*radius^2
# radius = float(input("Insert radius of circle (Its half of the diameter)"))
# pi = math.pi
# area = pi * pow(radius,2)
#
# print(f"The area of the circle is {round(area,2)} cm²")

## Exerise 3: Finding the hypotenuse of a right side triangle

print("""
  |\\
  | \\
a |  \\
  |   \\  c
  |    \\
  |_____\\
     b
""")
print("Find c using the formula --> c = sqrt(a² + b²")

a = float(input("Input a:"))
b = float(input("Input b:"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"c is {c} cm")