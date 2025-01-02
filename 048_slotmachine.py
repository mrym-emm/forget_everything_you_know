# Python Slot machin
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*" * 13)
    print(" | ".join(row))
    print("*" * 13)



def get_payout(row,bet):

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0



def main():
    balance = 100

    print("*"*25)
    print("Welcome to slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐  ")  # windows and ;
    print("*" * 25)

    while balance > 0:
        print("*" * 25)
        print(f"Current balance is  ${balance}")

        bet = input("Place you bet amount: ")

        if not bet.isdigit():
            print("Enter numbers only")
            continue # this will skip the current iteration of the loop and restart

        bet = int(bet)

        if bet > balance:
            print("Insufficent funds")
            # continue

        if bet <= 0:
            print("Bet must be greater than 0")
            # continue

        balance -= bet


        row = spin_row()
        # print(row)
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again (y/n)").lower()

        if play_again != 'y':
            print("*" * 40)
            print("Thank you!")
            print(f"Game over your final balance is  {balance}")
            print("*" * 40)
            break






if __name__ == "__main__":
    main()