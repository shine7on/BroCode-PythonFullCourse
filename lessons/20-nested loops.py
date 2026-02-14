# outer loop:
#   inner loop:

rows = int(input("Enter # of rows: "))
columns = int(input("Enter # of columns: "))
symbol = input("Enter a symbol: ")

for  x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()