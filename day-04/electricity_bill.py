units = int(input("Enter electricity units:"))

if units <= 100 :
    total = units*1.50 
    

elif units > 100 and units <= 200:
     total = (100*1.50) + ((units - 100) *2.50)
     

else:
     total = (100*1.50) +  ( 100 *2.50) + ((units - 200) *4.00)


print(f"Total electricity bill: ₹{total:.2f}")