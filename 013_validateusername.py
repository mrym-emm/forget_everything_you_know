"""
Validating user input exercise
1. no more thn 12 characters
2. no spacecs
3. no digits
"""

user_name = input("Please enter a username: ")


# if len(user_name) > 12:
#     print("Username cant be longer thn 12 characters")
#
# # This checks both the 2nd and thrid but for clarity is better for sperate
# elif user_name.isalpha() == False:
#     print("Username cant have spaces or digits")
#
# else:
#     print(f"Welcome {user_name}")

if len(user_name) > 12:
    print("Username cant be longer thn 12 characters")

# there shouldnt be any spaces, so it should return -1, otherwise it will inform users tht cannot have spaces
elif user_name.find(" ") != -1:
    print("Username cant have spaces")

# checks for digits, esentiallty x.isalpha() == False
elif not user_name.isalpha():
    print("Username cant have digits")

else:
    print(f"Welcome {user_name}")

