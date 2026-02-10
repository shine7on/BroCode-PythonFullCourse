# multiple inheritance:
# inherit from more than one parent class C(A, B)

# multi-level inheritance
# inherit from a parent which inherits from another parent
# C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"this {self.name} is eating")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit (Prey):
    pass

class Hawk (Predator):
    pass

class Fish (Prey, Predator):
    pass


rabbit = Rabbit("Bob")
hawk = Hawk("Chris")
fish = Fish("Fin")

rabbit.flee()
hawk.hunt()

rabbit.eat()

