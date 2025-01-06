"""
class variables = Shared among all instances of a class
                 Defined outside the constructor
                 Allow you to share data among all objects created from tht class
"""

class Student:

    class_year = 2024  # this shared among all objetcs
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Patrick", 10)
student2 = Student("Plankton", 11)
student3 = Student("Spongebob", 12)
student4 = Student("Sandy", 12)

print(student1.name)
print(student1.age)
# print(student1.class_year)

print(student2.name)
print(student2.age)
# print(student2.class_year)

# altho if its a class variable, its best practice to write it like below
# so we know its a class variable, and its shared among all the objects

print(Student.class_year)

print(Student.num_student)

print(f"My graduation class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)