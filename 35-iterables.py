# Iterables
# An object/collections that can return its elements one at a time

numbers = [1,2,3,4,5]

for number in numbers:
    print(number, end=" ")

print()

numbers = (1,2,3,4,5)

for number in reversed(numbers):
    print(number, end=" ")

print()

numbers = {1,2,3,4,5} # set

for number in numbers:
    print(number, end=" ")

print()

name = "Sponge Bob"

for char in name:
    print(char, end=" ")

print()

my_dictionary = {"A":1, "B":2, "C":3}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)
    