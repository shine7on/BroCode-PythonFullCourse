# Conditional Expression:
# one line shortcut for if-else statement (ternary operator)
# X if CONDITION else Y

num = 6

print("Positive" if num > 0 else "Negative")
result = "Even" if num%2 == 0 else "Odd"
print(result)


a = 5
b = 9
max_num = a if a > b else b
min_num = b if a > b else a
print(max_num, min_num)