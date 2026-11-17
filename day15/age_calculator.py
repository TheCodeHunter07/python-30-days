# ASSIGNMENT
# 2 age_calculator.py — use datetime to print exact age and days until the next birthday


import datetime


today = datetime.date.today()

dob = datetime.date(2003, 8, 18)


# Calculate age in years
age_years = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age_years -= 1


# Calculate remaining months and days
age_months = today.month - dob.month
age_days = today.day - dob.day


# Adjust days
if age_days < 0:
    age_months -= 1

    previous_month = today.month - 1

    if previous_month == 0:
        previous_month = 12

    days_in_previous_month = (
        datetime.date(today.year, today.month, 1)
        - datetime.timedelta(days=1)
    ).day

    age_days += days_in_previous_month


# Adjust months
if age_months < 0:
    age_months += 12
    age_years -= 1


# Calculate next birthday
next_birthday = datetime.date(today.year, dob.month, dob.day)

if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, dob.month, dob.day)


# Calculate remaining days
days_remaining = (next_birthday - today).days


# Display results
print("Today's date:", today)
print("Date of birth:", dob)

print(f"\nYour exact age: {age_years} years, {age_months} months, {age_days} days")

print("\nNext birthday:", next_birthday)
print("Days until next birthday:", days_remaining)





