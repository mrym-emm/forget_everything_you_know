import random

choices = ("rock", "paper", "scissors")







while True:
    computer_choice = random.choice(choices)
    print(computer_choice)
    user_choice = input("Pick between rock/paper/scissors (q to exit): ").lower()

    if user_choice =="q":
        print("Thanks for playing")
        break

    elif user_choice not in choices:
        print("Please only choose between rock/paper/scissors")
        continue

    else:
        print("okay")
        if user_choice == computer_choice:
            print("Draw")
        elif (user_choice == "paper") and (computer_choice == "rock"):
            print("You win!")
        elif (user_choice == "rock") and (computer_choice == "scissors"):
            print("You win!")
        elif (user_choice == "scissors") and (computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
