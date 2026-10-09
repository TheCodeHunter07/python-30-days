year = int(input("Enter the year :"))

if year % 400 == 0 :
    print("its Leap year")
elif year % 100 == 0:
    print("its not Leap year")
elif year % 4 == 0:
    print("its Leap year")
else:
    print("its not Leap year")