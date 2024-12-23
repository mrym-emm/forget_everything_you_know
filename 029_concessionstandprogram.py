# concession stand program

# dictionary {key:value}

menu = {"popcorn": 1.00,
         "hot Dog": 2.00,
         "pretzel": 2.00,
         "candy": 1.00,
         "soda": 1.00,
         "bottled water": 1.00}

cart = []
total = 0

print("-" * 50)

for key,value in menu.items():

    print(f"{key:10}: {value}")

print("-" * 50)


while True:
    food = input("What food would you like? (q to quit) ").lower()

    if food == "q":
        print("bye")
        break
    elif food in menu.keys():
        print("okay")
        cart.append(food)
        price = menu.get(food)
        total += price



    # elif menu.get(food) is not None:
    #     cart.append(food)
    #     # total = total + menu.values

print(cart)
print(total)
print(f"total is ${total}")
