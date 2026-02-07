weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if weight <= 0:
    print("You are fake")
elif unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 1)} {unit}.")
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
    print(f"Your weight is {round(weight, 1)} {unit}.")
else:
    print("Unit is not valid")

