import random

# print(help(random))

# random integers betwen range
number = random.randint(1,6)
print(number)

# random flaoting num between 0 n 1
number = random.random()
print(number)

# great for games with random
options = ("rock", "paper", "gunting")

opt = random.choice(options)

print(opt)

# shuffling a sequence
cards = ["2", "3", "4", "J", "K"]

random.shuffle(cards)
print(cards)