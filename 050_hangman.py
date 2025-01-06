# hangman in python
import random

words = ("apple", "banana", "orange", "coconut" )

# dictionary of key: ()
hangman_art = {
               0: ("   ",
                   "   ",
                   "   "),

               1: (" o ",
                   "   ",
                   "   "),

               2: (" o ",
                   " |  ",
                   "   "),

               3: (" o ",
                   "/| ",
                   "   "),

               4: (" o ",
                   "/|\\",
                   "   "),

               5: (" o ",
                   "/|\\ ",
                   "/  "),

               6: (" o ",
                   "/|\\",
                   "/ \\")
            }

# print(hangman_art[0])
#
# for line in hangman_art[1]:
#     print(line)

# for i in hangman_art:
#     for line in hangman_art[i]:
#         print(line)


def display_man(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("".join(answer))

def main():
    answer = random.choice(words)
    # print(answer)

    hint = ["_"] * len(answer)
    # print(hint)

    wrong_guesses = 0

    # initialize empty set.
    guessed_letter = set()
    is_running = True


    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        # display_hint(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess.isdigit() == True :
            print("Invalid input")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        guessed_letter.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            print("Word is wrong!")
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >=len(hangman_art) - 1:
            print("You lose!")
            display_answer(answer)
            is_running = False
            # play_again = input("Play again?").lower()
            #
            # if play_again == "y":
            #







if __name__ == "__main__":
    main()