# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ").lower()

# convert kg to pounds
if unit == 'k':
    weight *= 2.205
    unit = 'lbs.'
    print(f"Your newly converted weight is {round(weight, 2)} {unit}")

# convert pounds to kg
elif unit =='l':
    weight /= 2.205
    unit = 'kg.'
    print(f"Your newly converted weight is {round(weight, 2)} {unit}")

else:
    print(f"{unit} is invalid. Please try again")

