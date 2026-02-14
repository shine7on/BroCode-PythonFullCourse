# Python Slot Machine
import random

def spin_row():
    symbols = [ "🍒", '🍉', "🍋", "🔔", "⭐️" ]

    results = []

    for _ in range(3):
        results.append(random.choice(symbols))
    
    return results
               

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        else:
            return bet * 20
    
    return 0

    
def main():
    balance = 100
    print("************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒　🍉　🍋　🔔　⭐️")
    print("************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Invalid. Please enter valid number.")
            continue

        bet = float(bet)
        if bet > balance or bet < 0:
            print("Invalid. Please enter valid number.")
            continue
        else:
            balance -= bet

        row = spin_row()

        print("printing")
        
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost...")

        balance += payout

        play_again = input("Play again? (y/n): ").lower()

        if play_again == "n":
            break
    
    print(f"Your current balance: ${balance}")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()