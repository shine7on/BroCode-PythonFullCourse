capitals = {"USA":"Washington D.C.",
            "India":"New Deli",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals.get("USA"))
print(capitals.get("New Deli"))

capitals.update({"Japan":"Tokyo"})
capitals.update({"USA":"New York"})
capitals.pop("China")


print(capitals)

keys = capitals.keys()
print(keys)


values = capitals.values()
print(values)


items = capitals.items()
print(items)
