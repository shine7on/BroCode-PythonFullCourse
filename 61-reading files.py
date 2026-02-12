# Python reading files (.txt, .json, .csv)

file_path = "output"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


# JSON file
import json

file_path = "output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["age"])
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


# csv file
import csv
file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



