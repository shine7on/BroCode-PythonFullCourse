# super()
# used in a child class to call methos from a parent class (super class)
# extend the functionality of the inherited methods

class  Shape:
    def __init__ (self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {"Filled" if self.is_filled else "Not Filled"}")

class Circle (Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is circle")



class Square (Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle (Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle("pink", True, 5)
print(circle.color)
print(circle.is_filled)

circle.describe()
circle.super().describe()





