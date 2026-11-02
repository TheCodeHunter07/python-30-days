# ASSIGNMENT
# 3 rank_students.py — use zip to pair names with marks, then sort highest first

names = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [85, 92, 78, 95]

students = list(zip(names, marks))

ranked = sorted(students, key=lambda student:student[1] ,reverse=True)

print(ranked)