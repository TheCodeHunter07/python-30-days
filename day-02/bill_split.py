bill = int(input("Total bill :"))
tip_percentage = int(input("Tip percentage :"))
number_of_people = int(input("number of people :"))


tip = bill * tip_percentage / 100
total = bill + tip
share = total / number_of_people

print(tip)
print(total)
print(share)