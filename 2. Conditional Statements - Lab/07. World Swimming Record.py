import math

record = float(input())
distance_m = float(input())
distance_sec_one_m = float(input())

distance_sec = distance_sec_one_m * distance_m

add_sec = math.floor(distance_m / 15) * 12.5

total_distance_sec = add_sec + distance_sec

result = record - total_distance_sec

if result <= 0:
    print(f"No, he failed! He was {abs (result):.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_distance_sec:.2f} seconds.")

