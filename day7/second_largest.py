# Stretch: Find the second-largest number in a list without using sort().


numbers = [12, 45, 7, 89, 34, 56]



if numbers[0] > numbers[1]:
    largest = numbers[0]
    second_largest = numbers[1]
else:
    largest = numbers[1]
    second_largest = numbers[0]

for number in numbers[2:]:

    if number > largest:
       second_largest = largest
       largest = number

    elif number > second_largest and number != largest:
       second_largest = number

print("Largest number:", largest)
print("Second-largest number:", second_largest)