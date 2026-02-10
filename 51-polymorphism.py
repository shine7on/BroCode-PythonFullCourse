# polymorphism
# greek word "have many forms or faces"

# two ways to achieve polymorphism
# 1: inheritance = object could be treated of the same type as a parent class
# 2: "Duck Typing" = object must have necessary variables/functions

# abstract method:
# Any class inheriting from Parent must implement abstract methods.
from abc import abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius ** 2 * 3.14

class Square(Shape):
    def __init__ (self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__ (self, base, height):
        self.base = base
        self.height = height
    
    def area (self):
        return self.base * self.height / 2

class Pizza (Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pineapple", 10)]

for shape in shapes:
    print(shape.area())

