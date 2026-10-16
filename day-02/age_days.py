
#Method 1: Calculate each result independently 
#Calculate months, days, and hours directly from age.

age = int(input("Enter the age: "))

months = age * 12
days = age * 365
hours = age * 8760

print("Months:", months)
print("Days:", days)
print("Hours:", hours)

#Method 2: Reuse previous calculations

age = int(input("Enter the age: "))

months = age * 12
days = age * 365
hours = days * 24

print("Months:", months)
print("Days:", days)
print("Hours:", hours)