#
# name = input("Enter your full name: ")
#
# result = len(name)
#
# # first occurence
# result = name.find("M")
#
# # last occurence Maryam M
# result = name.rfind("M")
#
# # not found will return -1
# result = name.rfind("d")
#
# print(result)
#
# name = name.capitalize()
# print(name)
#
# name = name.upper()
# print(name)
#
# name = name.lower()
# print(name)
#
# # only returns True when name has DIGITS only not a combo
# result = name.isdigit()
# print(result)
#
# result = name.isalpha()
# print(result)


phone_number = input("Enter ur phone number: ")
result = phone_number.count("-")

result = phone_number.replace("-" , "")

print(result)
