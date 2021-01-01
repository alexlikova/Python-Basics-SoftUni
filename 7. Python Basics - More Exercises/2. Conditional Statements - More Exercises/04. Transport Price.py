n = int(input()) # km
travel_day_night = input().lower() # day or night

tariff = 0.0

if 0 < n < 20:
    taxi_initial_price = 0.70
    if travel_day_night == "day":
        tariff = 0.79
    else:
        tariff = 0.9
    price = taxi_initial_price + tariff * n

elif 20 <= n < 100:
    tariff = 0.09
    price = tariff * n
elif n >= 100:
    tariff = 0.06
    price = tariff * n
else:
    print("Error - negative km")
print(f"{price:.2f}")

