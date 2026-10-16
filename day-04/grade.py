# Task:  marks out of 100 -> grade A / B / C / D / F

# Requirements:

# Ask the user to enter marks out of 100.
# If marks are 90 or above, print Grade A.
# If marks are 75–89, print Grade B.
# If marks are 60–74, print Grade C.
# If marks are 35–59, print Grade D.
# If marks are below 35, print Grade F.


marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Grade F")