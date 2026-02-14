fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# or
# groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"]...]


print(groceries[0][0])

for collection in groceries:
    for item in collection:
        print(item)


one = ["1", "2", "3"]
two = ["4", "5", "6"]
three = ["7", "8", "9"]
four = ["*", "0", "#"]

dials = [one, two, three, four]
# or
# groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"]...]

for collection in dials:
    print()
    for item in collection:
        print(item, end = " ")


# tuple is faster than list
one = (1, 2, 3)
two = (4, 5, 6)
three = (7, 8, 9)
four = ("*", 0, "#")

dials = (one, two, three, four)

for collection in dials:
    print()
    for item in collection:
        print(item, end = " ")




