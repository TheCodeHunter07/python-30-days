#Method 1: Step-by-Step Calculation


total_bill = float(input("Enter the total bill: "))
tip_percentage = float(input("Enter the tip percentage: "))
number_of_people = int(input("Enter the number of people: "))

tip_amount = total_bill * tip_percentage / 100

final_bill = total_bill + tip_amount

share = final_bill / number_of_people

print(f"Original bill: ₹{total_bill:.2f}")
print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Total bill including tip: ₹{final_bill:.2f}")
print(f"Share per person: ₹{share:.2f}")


#Method 2: Calculate the Share Directly

total_bill = float(input("Enter the total bill: "))
tip_percentage = float(input("Enter the tip percentage: "))
number_of_people = int(input("Enter the number of people: "))

tip_amount = total_bill * tip_percentage / 100

share = (total_bill + tip_amount) / number_of_people

print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Share per person: ₹{share:.2f}")
