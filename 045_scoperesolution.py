"""
variable scope = where a variable is visible and accessible
scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
"""
################################################
## LOCAL
def func1():
    a = 1
    print(a)


def func2():
    b = 2
    print(b)

# Here in their respective functions, variable a is LOCAL
# to func1() and variable b is LOCAL to func2
# below is wrong
# def func1():
#     a = 1
#     print(b) -----> like this
#
#
# def func2():
#     b = 2
#     print(a) -----> like this
## functions cant see inside of other functions but they can see inside
## of their own
func1()
func2()

################################################

################################################
## ENCLOSED ie function inside fucntion
def func1():
    x = 1
    def func2():
        x = 2
        print(x)
    func2()

func1()
################################################

# GLOBAL -> meaning outside of function

def func1():
    print(x)

def func2():
    print(x)

x = 11

func1()
func2()

################################################

from math import e

def func1():
    # e = 2
    print(e)

# e = 3

func1()

