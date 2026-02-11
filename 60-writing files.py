# python writing files (.txt, .json, .csv)

txt_data = "I like Dogs"
file_path = "output.txt"

try:
    with open(file=file_path, mode="x") as file:
        file.write(txt_data)
        print(f"text file '{file_path}' is created.")
except FileExistsError:
    print("That file already exists!")

# with: open/close file accordingly
# "w" = writing
with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"text file '{file_path}' is created.")

with open(file=file_path, mode="a") as file:
    file.write("\n" + txt_data)
    print(f"text file '{file_path}' is created.")


employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output1.txt"

try:
    with open(file_path, "w") as file:
        for employ in employees:
            file.write(employ + " ")
        print(f"txt file '{file_path}' was created!")
except FileExistsError:
    print("That file already exists!")


# JSON FILE
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook",
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent = 4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


# csv file
# comma separate values

import csv

employees = [["Name", "Age", "Job"],
             ["Bob", 24, "Cook"],
             ["Alex", 45, "Unemployed"],
             ["Max", 67, "Scientist"]]

file_path = "output.cvs"

try:
    with open(file_path, "w", newline ="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists!")




        