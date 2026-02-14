class Car:
    # constructor
    # self: means that this object we are creating right now
    def __init__(self, model, year, color, for_sale): # dunder: double underscore
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive {self.model}")

    def stop(self):
        print(f"You stop {self.model}")