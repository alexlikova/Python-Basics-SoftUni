import math
import sys

number_of_airlines = int(input())

winner_name = ""
winner_average_passengers = - sys.maxsize

for number in range(number_of_airlines):
    airline_name = input()

    total_passengers = 0
    counter_flights = 0

    command = input()
    while command != "Finish":
        passengers = int(command)

        total_passengers += passengers
        counter_flights += 1
        command = input()

    average = math.floor(total_passengers / counter_flights)
    print(f"{airline_name}: {average:.0f} passengers.")

    if average > winner_average_passengers:
        winner_average_passengers = average
        winner_name = airline_name

print(f"{winner_name} has most passengers per flight: {winner_average_passengers:.0f}")