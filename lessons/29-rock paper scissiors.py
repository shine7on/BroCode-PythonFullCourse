import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    
    again = input("Play again? (y/n): ").lower()
    while again != "y" and again != "n":
        again = input("Do you want to play again? (y/n): ").lower()
    
    if (again == "n"):
        is_running = False



    