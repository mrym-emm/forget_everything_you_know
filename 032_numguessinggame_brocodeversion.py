import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0

is_running = True

print("Python num guessing game")
print(f"Select a number between {lowest_num} and  {highest_num}")

while is_running:

    guess = input("Enter your guess!: ")

    # check user input
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please Select a number between {lowest_num} and  {highest_num}")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        # if correct flags it to False
        else:
            print(f"Correct! The answer was {answer}. It took you {guesses} guesses")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please Select a number between {lowest_num} and  {highest_num}")
