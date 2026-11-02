# ASSIGNMENT
# 1 coordinates.py — store 5 points as tuples; find the one closest to (0, 0)

coordinates = [(3,6), (4,3), (6,4), (3,2), (2,7)]

closest_point = coordinates[0]

closest_dis = coordinates[0][0]**2 + coordinates[0][1]**2

for point in coordinates:

    x , y = point
    print(point)

    sq_distance = x**2 + y**2
    print("Distance:", sq_distance)

    if sq_distance < closest_dis:
       
        closest_point = point
        closest_dis = sq_distance
        

print("Closest distance:", closest_dis)    
print("Closest point to (0, 0):", closest_point) 




