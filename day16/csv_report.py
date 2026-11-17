# ASSIGNMENT
# 2 csv_report.py — write 10 students with marks to a CSV; read it back and print averages

import csv 

students = [
    ["Rahul", 85],
    ["Amit", 78],
    ["Priya", 92],
    ["Sneha", 88],
    ["Rohan", 75],
    ["Neha", 95],
    ["Karan", 67],
    ["Pooja", 82],
    ["Akash", 90],
    ["Anjali", 80]
]



with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Marks"])

    writer.writerows(students)


with open("students.csv", "r", newline="") as file:

    reader = csv.reader(file)

    for row in reader:
        print(f"Name: {row[0]}, Marks: {row[1]}")



total_marks = 0 

student_count = 0

with open("students.csv", "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        marks = int(row[1])

        total_marks += marks

        student_count += 1

    average = total_marks / student_count

    print("Total Marks:", total_marks)
    print("Number of Students:", student_count)
    print("Average Marks:", average)


