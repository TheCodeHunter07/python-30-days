# ASSIGNMENT
# 1 Add __str__ and __repr__ to your Student class

# Stretch: Make Student objects sortable by average using __lt__.


class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, {self.marks})"

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def __lt__(self, other):
        return self.average() < other.average()


# Creating Student objects
student1 = Student("Rahul", 21, [80, 90, 85])
student2 = Student("Amit", 22, [60, 70, 65])
student3 = Student("Priya", 20, [90, 95, 85])


# Testing __str__() and __repr__()
print(student1)
print(str(student1))
print(repr(student1))


# Creating a list of students
students = [student1, student2, student3]


# Displaying original student records
print("\nOriginal Student List:")

for student in students:
    print(f"Student Name: {student.name}, Average: {student.average()}")


# Testing average()
print("\nIndividual Averages:")
print(student1.average())
print(student2.average())


# Testing __lt__()
print("\nComparison:")
print(student1 < student2)


# Sorting students using __lt__()
sorted_students = sorted(students)

print("\nStudents Sorted by Average Marks:")

for student in sorted_students:
    print(f"{student.name}: {student.average()}")