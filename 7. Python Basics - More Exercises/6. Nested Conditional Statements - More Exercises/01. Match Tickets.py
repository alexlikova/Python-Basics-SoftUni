budget = float(input())
category = input()
people = int(input())

vip = 499.99
normal = 249.99
price = 0

if 1 <= people <= 4:
    budget *= 0.25
    if category == "VIP":
        price = vip * people
        diff = budget - price
    elif category == "Normal":
        price = normal * people
        diff = budget - price
    else:
        print("Error, type vip or normal:")
elif 5 <= people <= 9:
    budget *= 0.40
    if category == "VIP":
        price = vip * people
        diff = budget - price
    elif category == "Normal":
        price = normal * people
        diff = budget - price
    else:
        print("Error, type vip or normal:")
elif 10 <= people <= 24:
    budget *= 0.50
    if category == "VIP":
        price = vip * people
        diff = budget - price
    elif category == "Normal":
        price = normal * people
        diff = budget - price
    else:
        print("Error, type vip or normal:")
elif 25 <= people <= 49:
    budget *= 0.60
    if category == "VIP":
        price = vip * people
        diff = budget - price
    elif category == "Normal":
        price = normal * people
        diff = budget - price
    else:
        print("Error, type vip or normal:")
elif people >= 50:
    budget *= 0.75
    if category == "VIP":
        price = vip * people
        diff = budget - price
    elif category == "Normal":
        price = normal * people
        diff = budget - price
    else:
        print("Error, type vip or normal:")
else:
    print(input("Error, cannot be a negative number!"))

if diff >= 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")