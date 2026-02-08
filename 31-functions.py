def happybirthday():
    print("Yey")
    print("Happy Birthday")


def happybirthday2(name):
    print("Yey")
    print(f"Happy Birthday, {name}")


happybirthday()
happybirthday2("james")


def display_invoice (username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due: {due_date}")

display_invoice("Max", 2000, "1/1")


# return
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

print(add(1,3), subtract(5,3))


def create_name(first, last):
    name = first.capitalize() + " " + last.capitalize()
    return name


print(create_name("max", "KAHG"))

