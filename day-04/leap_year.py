# Task:  check whether a year is a leap year

# Approach 1:Using individual if, elif, and else conditions


year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Leap year")

elif year % 100 == 0:
    print("Not a leap year")

elif year % 4 == 0:
    print("Leap year")

else:
    print("Not a leap year")


# Approach 2:Using a single if condition

year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
      print("Leap year")
else:
    print("Not a leap year")