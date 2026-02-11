# static methods
#  method that belongs to a class rather than any object from that class
# used for general utility funcs

# instance methods: best for operation on instances of the class (objects)
# static methods: best for utility funcs that do not need access to class data


class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Casher", "Cook", "Janitor"]
        return position in valid_position
    

employee1 = Employee("Engine", "Manager")
employee2 = Employee("Bob", "Casher")
employee3 = Employee("Max", "Cook")


print(employee1.get_info())
print(employee1.is_valid_position("Manager"))
print(Employee.is_valid_position("Manager"))