"""
Decorator = A function that extends the behaviour of another function
            w/o modifying the base function
            Pass the base function as an arguement to the decorator

            @addsprinkles
            get_icecream("Vanilla)
"""

def add_sprinkles(func):
    def wrapper(*args, **kwargs): # this is necessary as a format, otherwise itll run the function
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream!🍦")



get_ice_cream('choc')
#
# ###This is what happen if you dont have the wrapper
# def add_sprinkles(func):
#     print("You add sprinkles")
#
# @add_sprinkles
# def get_ice_cream():
#     print("Here is your icecream!🍦")
#
# # even when you dont call the function the decorator will run it
# #####################################

