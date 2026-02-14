menu = {"POPCORN":1.00,
          "HOT DOG":2.00,
          "PRETZEL":2.00,
          "ASST CANDY":1.00,
          "SODA":1.00,
          "BOTTLED WATER":1.00}

cart = []
total = 0

print("-------MENU-------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")


print("-------ORDER-------")
while True:
    item = input("What do u want to get (q to quit): ").upper()
    if item == "Q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total += menu.get(item)

print(cart)
print(f"Total: ${total}")

        


