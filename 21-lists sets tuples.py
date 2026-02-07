# collection

## LIST
fruits = ["apple", "orange", "grape", "coconut"]

print(fruits[0:3])

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))

print(len(fruits))

print("apple" in fruits)

fruits[0] = "pineapple"
fruits.insert(0, "banana")

fruits.sort()
 
print(fruits)


## SET
fruits = {"apple", "orange", "grape", "coconut", "coconut"}

#print(dir(fruits))
#print(help(fruits))

print(len(fruits))

print("pineapple" in fruits)

fruits.remove("apple")
fruits.pop()
 
print(fruits)

fruits.clear()



## TUPLE
# tuple >>>>>> list for speed
fruits = ("apple", "orange", "grape", "coconut", "coconut")

print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))





