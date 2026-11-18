# ASSIGNMENT
# 1 student_class.py — a Student class with average() and grade() methods
    

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        
        if not self.marks:
           return 0

        avg = sum(self.marks) / len(self.marks)

        return avg

    def grade(self):

        if not self.marks:
            return "No marks available"

        avg = self.average()

        if avg >= 90:
            return "Grade: A"
        elif avg >= 80:
            return "Grade: B"
        elif avg >= 70:
            return "Grade: C"
        elif avg >= 60:
            return "Grade: D"
        else:
            return "Grade: F"

student1 = Student("sumit",[80, 75, 90])

student2 = Student("Priya",[85, 90, 95])


print(student1.name, student1.average(), student1.grade())
print(student2.name, student2.average(), student2.grade())

student3 = Student("Rahul", [])
print(student3.average())