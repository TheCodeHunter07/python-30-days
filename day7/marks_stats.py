# Assignment 1: marks_stats.py- marks for 5 subjects -> total, average, highest, lowest

# Objective: Create a Python program that accepts marks for five subjects and displays the total, average, highest mark, and lowest mark.

marks =[]

for i in range(1,6):
    subject = int(input(f"Enter the marks of subject {i} out of 100:"))

    marks.append(subject)



total = sum(marks)

highest = max(marks)
lowest = min(marks)
        
avg = total/len(marks)


print(f"Total marks: {total}")
print(f"Average : {avg}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")



