import math

record = float(input())
distance = float(input())
seconds_for_1m = float(input())

time = distance * seconds_for_1m
added_time = (math.floor(distance / 50)) * 30
total_time = time + added_time

diff = record - total_time
if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {abs(diff):.2f} seconds slower.")