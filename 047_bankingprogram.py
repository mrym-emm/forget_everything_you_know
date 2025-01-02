# Python banking program

def show_balance(balance):
    print(f"Your Balance is: RM{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited"))

    if amount < 0:
        print("Thats not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn"))


    if amount > balance:
        print("Please withdraw within your balance")
        return 0
    elif amount < 0:
        print("Withdrawal must be more than RM 0")
        return 0
    else:
        print(f"Your withdrawal of {amount:.2f} is succesful")
        return amount

def main():
    # initialse balance
    balance = 0
    is_running = True # if False will exit program

    while is_running:
        print("*"*30)
        print("Banking program")
        print("""
        1. Show Balance
        2. Make Deposit
        3. Withdraw
        4. Exit
        """)
        print("*" * 30)
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            balance += deposit()

        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Thank you for using our program")
            is_running = False
        else:
            print("Please only choose between 1-4!")
            # no need continue as well

if __name__ == '__main__':
    main()
