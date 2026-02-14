# class variable
# shared among all instances of a class
# defined outside the constructor


class Student:
    class_year = 2026
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("Bob", 30)
student2 = Student("Chris", 35)
student3 = Student("Chris", 35)


print(Student.class_year) # use this to show its class variable
print(student1.class_year)

print(Student.num_student)
print(student1.num_student)