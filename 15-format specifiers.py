# format specifiers
# {value: flag} format

price1 = 3.14159
price2 = -987.65

print(f"Price 1 is ${price1:.2f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:^10}")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")

price1 = 3000.14159
price2 = -9870.65

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price2:+,.2f}")
