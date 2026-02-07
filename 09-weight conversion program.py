weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if weight <= 0:
    print("You are fake")
elif unit == "K":
    weight *= 2.205
    unit = "Lbs"
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
else:
    print("Unit is not valid")

print(f"Your weight is {weight} {unit}.")