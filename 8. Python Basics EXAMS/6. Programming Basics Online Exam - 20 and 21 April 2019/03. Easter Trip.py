destination = input()
dates = input()
nights = int(input())

easter_trip_dict = {
    "France": {"21-23": 30, "24-27": 35, "28-31": 40},
    "Italy": {"21-23": 28, "24-27": 32, "28-31": 39},
    "Germany": {"21-23": 32, "24-27": 37, "28-31": 43}
}

price = easter_trip_dict[destination][dates] * nights

print(f"Easter trip to {destination} : {price:.2f} leva.")