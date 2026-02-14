# *arg = allow you to pass multi non-key args
# **kwargs = allow you to pass multi key-args

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Spongebob", "Haroad", "Squarepant")


def print_address(**kwargs):
    for key in kwargs.keys():
        print(key)
    for value in kwargs.values():
        print(value)

print_address(street="123 Fake St.",
              city="detroit",
              state="MI",
              zip="54321")



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value)

shipping_label("Spongebob", "Haroad", "Squarepant", 
               street="123 Fake St.",
               city="detroit",
               state="MI",
               zip="54321")


