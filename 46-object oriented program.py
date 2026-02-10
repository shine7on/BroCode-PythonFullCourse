# object
# a bundle of related attributes (variable) and methods (functions)

# class: design the structure and layout
from car import Car

car1 = Car("BMW", 2026, "pink", False)
car2 = Car("Tesla", 2026, "red", True)
car3 = Car("Toyota", 2026, "yellow", True)

print(car1.model)
print(car2.for_sale)
print(car3.color)

car1.drive()
car2.stop()
print(car3.color)