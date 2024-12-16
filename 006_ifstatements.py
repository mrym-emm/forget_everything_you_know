# if = Do some code only IF some condition is True
# else= Do something else
# MUST PAY ATTENTION TO ORDER OF STATEMENTS

# EX 1: Checking age for redit card

age = int(input("Enter age: "))
if age>= 100:
    print("You are too old to sign up!")

elif age >= 18:
    print("You are now signed up")

elif age <0:
    print("You havent been born yet!")



else:
    print("You must be 18+ to sign up for a credit card")

# EX 2: ask if they want food and set up response
response = input("Would you like food? (Y/N): ").lower()

if response == 'y':
    print("Here is some food!")
elif response == 'n':
    print("Okay, feel free to come here if youd like some tho!")
else:
    print("Invalid response")

# Ex 3: Ask for name

name = input("Enter your name:")

if name == "":
    print("You did not enter your name!")

else:
    print(f"Hello, {name}")

## Ex 4: Booleans if else

for_sale = True

if for_sale:
    print("This item is for sale!")

else:
    print("This item is NOT for sale")

is_online = False

if is_online:
    print("This user is ONLINE")

else:
    print("This user is NOT online")
