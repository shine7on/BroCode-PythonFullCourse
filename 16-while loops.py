name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

print(f"Your name is {name}")


food = input("Enter a food you like (q to quit): ")


while food != "q":
    food = input("Enter a food you like (q to quit): ")

print("bye")


num = int(input("Enter between 1 - 10: "))

while num < 1 or num > 10:
    num = int(input("Enter between 1 - 10: "))

print(num)
          


