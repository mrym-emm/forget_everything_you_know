"""
keyword aguements = an arguement preceded by an identifier
                    helps with readability
                    order of arguements doesnt matter
                    1. positional 2.2default 3.KEyWORD 4. arbitary

"""

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello(title = "Ms", greeting = "Hello",first =  "Maryam" , last = "M")

# if you want to mix make sure positonal then keywords

for i in range(1,11):
    print(i, end = " ")

print()

# to seperate with symbol
print("1","2", "3", "4", "5", sep = "*")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 60, area = 123, first = 456, last =789)

print(phone_num)

# keyword arguements --> arguements preceeded by identifier, helps with
#                        readability
