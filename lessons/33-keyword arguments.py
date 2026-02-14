# keyword arguments
# helps with readability

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("hello", title="Mr.", first="Spongebob", last="Squarepants")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1, area=123,first=456,last=789)

print(phone_num)