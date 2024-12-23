# return =statement used to end a function and send a result back to the caller

def add(x,y):
    return x + y

def minus(x,y):
    return x - y
def times(x,y):
    return x * y
def div(x,y):
    return x / y

z = add(1,2)
print(z)

z = minus(1,2)
print(z)

z = times(1,2)
print(z)

z = div(1,2)
print(z)

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

name = create_name("maryam", "m")
print(name)
