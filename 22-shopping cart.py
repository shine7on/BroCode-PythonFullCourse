foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter a price for a {food}: $"))
        while float(price) <= 0:
            price = float(input(f"Enter a price for {food}: $"))
        prices.append(price)


print("----- YOUR CART ------")
for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print()
print(f"Total: ${total}")



