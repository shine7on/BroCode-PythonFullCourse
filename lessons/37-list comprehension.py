# List comprehension
# create lists concisely

# integer
doubles = []

for x in range(1,11):
    doubles.append(x*2)

print(doubles)


doubles2 = [x*2 for x in range(1,11)]
print(doubles2)

triples = [y*3 for y in range(1,11)]
print(triples)


squares = [z**2 for z in range(1,11)]
print(squares)


# strings
fruits = ["apple", "orange", "banana"]
fruits = [ fruit.upper() for fruit in fruits ]
letter = [ fruit[0] for fruit in fruits ]

print(fruits)
print(letter)


# integer
numbers = [1, -2, 3, -4, -6, 3, -9, 13]
positive = [ number for number in numbers if number >= 0]

print(positive)


grades = [85, 42, 79, 90, 56, 61, 30]
grade = [ grade for grade in grades if grade >= 60]

print(grade)

