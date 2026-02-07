name = input("Enter your name: ")
result = len(name)

print(result) # this counts space


indexFirst = name.find(" ")
indexLast = name.rfind(" ") # reverse: get last occurerance
print(indexFirst, indexLast)


name = name.capitalize() # first letter
print(name)

name = name.upper()
print(name)
print(name.lower())

phone_num = input("Enter phone number: ")
counter = phone_num.count("-")
print(counter)
print(phone_num.replace("-", ""))


