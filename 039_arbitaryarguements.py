"""
ARBITARY arguements

*args = allows you to pass multiple non-key arguements
**kwargs = allows you to pass multiple keyword arguements
           * unpacking operator
"""

# to allow multiple arguemetns passed tru
def add(*args):
    # print(type(args)) # is tuple
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4))

def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("Ms", "Maryam", "M")

def print_address(**kwargs):
    # print(type(kwargs)) #dictionary, so can use dicitonary functionaliy

    for value in kwargs.values():
        print(value)

    for key in kwargs.keys():
        print(key)

    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value} ")

print()
print_address(street = "123 Fake Street",
                    city = "Detroit",
                    zip_code = "40120")

# this will surely be handy
# to mix, positonal args then keyword args

def shipping_label(*args, **kwargs):

    for arg in args:
        print(arg, end = " ")

    print()
    print("You live at ", end = " ")
    # for kwarg in kwargs.values():
    #     print(kwarg, end = " ")
    print(f"{kwargs.get('street')}")

    if "state" in kwargs:
        print(f"{kwargs.get('state')} {kwargs.get('zip_code')}")
    else:
        print(f"{kwargs.get('zip_code')}")

shipping_label("Dr.", "Harry", "Potter",
               street = "123 Fake street",
               state = "Detroit",
               zip_code = "40130")
print()

shipping_label("Dr.", "Harry", "Potter",
               street = "123 Fake street",

               zip_code = "40130")

