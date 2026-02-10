# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):

    amount = float(input("Enter an amount to be deposited: $"))

    if (amount < 0):
        print("That is not valid amount")
    else:
        balance += amount
        print(f"Your balance is ${balance:.2f}")
    
    return balance

def withdraw(balance):

    amount = float(input("Enter an amount to be withdrawn: $"))

    if (amount < 0 or balance < amount):
        print("That is not valid amount")
    else:
        balance -= amount
        print(f"Your balance is ${balance:.2f}")

    return balance



def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("Banking Program")
        print("*******************")
        print("1: show balance")
        print("2: deposit")
        print("3: withdraw")
        print("4: exit")

        choice = int(input("Enter your choice (1 - 4): "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance = deposit(balance)
            case 3:
                balance = withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("Invalid")
        
        print("****************")
        

    print("Thank you. Have a nice day.")

if __name__ == "__main__":
    main()
