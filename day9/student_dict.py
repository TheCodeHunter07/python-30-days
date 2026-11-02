# ASSIGNMENT
# 3 student_dict.py — store 3 students as nested dictionaries; print each student's average

students = {
    "Rahul": {"math": 80, "science": 90, "english": 70},
    "Priya": {"math": 85, "science": 95, "english": 90},
    "Amit": {"math": 70, "science": 75, "english": 80}
}

for name, marks in students.items():
    total = sum(marks.values())
    average = total/len(marks.values())
    print(f"{name}: Average = {average}")
