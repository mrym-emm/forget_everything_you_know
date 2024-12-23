"""
default arguements = A default value for certain parameters
                     default is used when the arguements is omitted
                     make your functions more flexible, reduces # of argeuments
                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitary
"""

import time
# put default values,especially if its constant
def net_price(list_price, discount = 0.0, tax = 0.05):
    return list_price * (1 - discount) * (1+ tax)

print(net_price(500))
print(net_price(500, 0.012))


def count(start, end = 0):
    for x in reversed(range(end, start+1)):
        print(x)
        time.sleep(0.07)
    print("Done")

count(30,15)