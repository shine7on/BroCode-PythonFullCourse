# class methods
# allow operation related to the class itself
# take class as 1st parameter


class Student:

    count = 0
    gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.gpa += gpa


    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    

    @classmethod
    def get_count(cls):
        return f"Total # of student: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.gpa == 0:
            return 0
        else:
            avg = cls.gpa / cls.count
        return f"Total # of student: {avg}"
    

student1 = Student("Bob", 4.0)
student2 = Student("Max", 3.0)
student3 = Student("Cindy", 3.5)

print(Student.get_count())
print(Student.get_avg_gpa())
