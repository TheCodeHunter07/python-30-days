# ASSIGNMENT
# 2 common_friends.py — using sets, show common friends, all friends, and friends unique to each person


person1_friends = {"Rahul", "Amit", "Sneha", "Priya", "Karan"}

person2_friends = {"Amit", "Priya", "Neha", "Karan", "Rohit"}


all_friends = person1_friends.union(person2_friends)

print("All friends:",all_friends)


common_friends = person1_friends.intersection(person2_friends)

print("common friends:",common_friends)

person1 = person1_friends - person2_friends

print("Friends unique to Person 1:", person1)

person2 = person2_friends - person1_friends

print("Friends unique to Person 2:", person2)