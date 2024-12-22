# simple shopping cart program

foods = []

prices = []

total = 0

while True:

    food = input("What would you like? (q to quit): ").lower()

    if food == 'q':
        break

    else:
        price = float(input("What is the price of it: "))
        foods.append(food)
        prices.append(price)

print("Your shopping cart is:")

for food in foods:
    print(food)
for price in prices:
    total += price

print(f"Your final total is: {total}")



