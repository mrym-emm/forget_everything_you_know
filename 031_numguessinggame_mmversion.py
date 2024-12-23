# number guessing game
import random
a= 1
b= 10
actual_num = random.randint(a,b)
print(actual_num)

limit_guesses = 3
guess = 1


while guess <= limit_guesses:

    answer = int(input(f"Guess a number between {a} and {b}"))

    if answer == actual_num:
        print(f"Correct! The number is {actual_num}")
        break
    elif answer < actual_num:
        print(f"Go Higher! You have {limit_guesses - guess} guesses left")
        guess += 1

    elif answer > actual_num:
        print(f"Go Lower! You have {limit_guesses - guess} guesses left")
        guess += 1


print(f"You ran out of guesses. The correct number is {actual_num}")

    # else:
    #     print(f"Try again. You have {limit_guesses - guess} guesses left")
    #     guess += 1








