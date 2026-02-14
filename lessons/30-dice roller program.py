import random

# ● ┌ ─ ┐ │ └ ┘

"┌---------┐"
"│         │"
"│         │"
"│         │"
"└---------┘"


dice_art = {
    1: ("┌---------┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└---------┘"),
    2: ("┌---------┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└---------┘"),
    3: ("┌---------┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└---------┘"),
    4: ("┌---------┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└---------┘"),
    5: ("┌---------┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└---------┘"),
    6: ("┌---------┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└---------┘")
}



dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

print(dice)

for x in range(num_of_dice):
    num = dice[x]
    for x in range(5):
        print(dice_art[num][x])

for x in range(5):
    for num in dice:
        print(dice_art[num][x], end=" ")
    
    print()

