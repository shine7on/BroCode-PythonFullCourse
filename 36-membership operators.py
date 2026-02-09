# membership operators
# test whether a value or variable is found in a sequence
# string, list, tuple, set, or dictionary

email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")


word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


grades = {"Sandy":"A",
          "Bob":"B",
          "Cindy":"C",
          "Dex":"D",
          "Eric":"F"}

name = input("Enter your name: ").capitalize()

if name not in grades:
    print("Invalid")
else:
    print(f"Your grade is {grades[name]}")

