# Method 1:

units = int(input("Enter electricity units:"))

if units <= 100 :
    total = units*1.50 
    

elif units > 100 and units <= 200:
     total = (100*1.50) + ((units - 100) *2.50)
     

else:
     total = (100*1.50) +  ( 100 *2.50) + ((units - 200) *4.00)


print(f"Total electricity bill: ₹{total:.2f}")

# method 2:

# Task: calculate a bill using slab rates.

# Monthly consumption	Rate per unit
# First 100 units	₹4.71
# Next 200 units (101–300)	₹10.29
# Next 200 units (301–500)	₹14.55
# Above 500 units	₹16.64


units = int(input("Enter the consumption units:"))


if units <= 100:
    print(f"electricity_bill is: ₹{units*4.71:.2f}")

elif units <= 300:
    print(f"electricity_bill is: ₹{(100*4.71) + (units-100)*10.29:.2f}")

elif units <= 500:
    print(f"electricity_bill is: ₹{(100*4.71) + (200*10.29) + ((units - 300)*14.55):.2f}")

else:
    print(f"electricity_bill is: ₹{(100*4.71) + (200*10.29) + (200*14.55) + ((units - 500)*16.64):.2f}")


