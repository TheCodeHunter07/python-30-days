# ASSIGNMENT
# 2 people.py — Person base class with Student and Teacher using super().__init__()

class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age

def introduce(self):
    print(f"Hello, I am {self.name} and I am {self.age} years old.")

class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

student1 = Student("Rahul", 21, "Computer Science")
teacher1 = Teacher("Priya", 35, "Python")

student1.introduce()
student1.study()

teacher1.introduce()
teacher1.teach()