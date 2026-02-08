import random

number = random.randint(1,20)
number2 = random.random()

print(number)
print(number2)

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6"]

option = random.choice(options)
card = random.choice(cards)
random.shuffle(cards)

print(option)
print(card)
print(cards)