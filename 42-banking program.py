# Python Banking Program

balance = 0
is_running = True

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    global balance

    amount = float(input("Enter an amount to be deposited: $"))

    if (amount < 0):
        print("That is not valid amount")
    else:
        balance += amount
        print(f"Your balance is ${balance:.2f}")

def withdraw():
    global balance

    amount = float(input("Enter an amount to be withdrawn: $"))

    if (amount < 0 or balance < amount):
        print("That is not valid amount")
    else:
        balance -= amount
        print(f"Your balance is ${balance:.2f}")




while is_running:
    print("Banking Program")
    print("1: show balance")
    print("2: deposit")
    print("3: withdraw")
    print("4: exit")

    choice = int(input("Enter your choice (1 - 4): "))

    match choice:
        case 1:
            show_balance()
        case 2:
            deposit()
        case 3:
            withdraw()
        case 4:
            is_running = False
        case _:
            print("Invalid")
    

print("Thank you. Have a nice day.")

