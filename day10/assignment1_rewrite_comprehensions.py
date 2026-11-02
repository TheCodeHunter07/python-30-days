# ASSIGNMENT
# 1 Rewrite three earlier loop-based solutions using comprehensions


#  Program 1: unique_words.py (Day 8)
words = ["python", "java", "python", "javascript", "java"]

unique_words = {word for word in words}

print(sorted(unique_words))

#  Program 2: char_frequency.py — Day 9

text = "hello"

frequency = {char: text.count(char) for char in set(text)}

print(frequency)

# Program 3: student_dict.py — Day 9

students = {
    "Rahul": {"math": 80, "science": 90},
    "Priya": {"math": 85, "science": 95},
    "Amit": {"math": 70, "science": 75}
}

averages = {
    name: sum(marks.values()) / len(marks)
    for name, marks in students.items()
}
