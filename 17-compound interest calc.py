principal = 0
interest = 0
time = 0

while True:
    principal = int(input("Enter your balance: "))
    if principal < 0:
        print("principal can not less than 0")
    else: 
        break

while interest <= 0:
    interest = float(input("Enter the interest rate: "))
    if interest < 0:
        print("interest can not be less than 0")

while time <= 0:
    time = int(input("Enter the years: "))

print(principal*(1+interest/100)**time)
