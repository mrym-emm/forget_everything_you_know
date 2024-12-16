# Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

"""
This whole section is to understand and re-enforce type casting
I may know this already, but I actually learnt new things here.
Especially how empty strings, None values, 0 are False when typecasted to Booleans

"""

name = "Maryam M"
age = 25
gpa = 3.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
age= float(age)

print(gpa)
print(age)

age = str(age)
print(age)
print(type(age))

name = bool(name)
print(name)

# will return False if empty string
name = ""
print(bool(name))


