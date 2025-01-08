"""
Class methods = Allow operations related to the class itself
                Take (cls) [opposite to the (self)] as the first parameter, which represents the class itself

 Instance methods = best for operations on instance of the class (object)
 Static methods = best for utility functions that do no need access to class data
 Class methods = Best for class-level data or require access to the class itself
"""

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        # whenever we re creating student, we increment the count by 1
        Student.count +=1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} -> {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of student is {cls.count}"

    @classmethod
    def get_avggpa(cls):
        if cls.count == 0:
            return 0

        return f"Average gpa is {cls.total_gpa/cls.count:.2f}"


student1 = Student("Patrick", 3.4)
student2 = Student("Sandy", 3.9)
student3 = Student("Spongebob", 3.7)

print(Student.get_count())
print(Student.get_avggpa())