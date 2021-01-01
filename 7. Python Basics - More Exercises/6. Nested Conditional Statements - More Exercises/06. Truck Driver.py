season = input().capitalize()
km_travel = float(input())

money_km = 0

if 0 < km_travel <= 5_000:
    if season == "Summer":
        money_km = 0.90
    elif season == "Winter":
        money_km = 1.05
    elif season == "Spring" or season == "Autumn":
        money_km = 0.75
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))
elif 5000 < km_travel <= 10_000:
    if season == "Summer":
        money_km = 1.10
    elif season == "Winter":
        money_km = 1.25
    elif season == "Spring" or season == "Autumn":
        money_km = 0.95
    else:
        print(input("Wrong season. Choose between Summer or Winter: "))

elif 10_000 < km_travel <= 20_000:
    money_km = 1.45
else:
    print(input("Error, choose between 0 and 20 000 km. Try again: "))

gross_salary = money_km * km_travel * 4 # 4 months per season
net_salary = gross_salary * 0.9 # 10% danaci

print(f"{net_salary:.2f}")