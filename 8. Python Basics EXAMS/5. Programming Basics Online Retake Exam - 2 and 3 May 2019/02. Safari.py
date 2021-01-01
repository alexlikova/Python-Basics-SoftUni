price_l_gasoline = 2.1
guide = 100

budget = float(input())
needed_l_gasoline = float(input())
day_weekend = input()

price = (price_l_gasoline * needed_l_gasoline) + guide

if day_weekend == "Saturday":
    price *= 0.9
elif day_weekend == "Sunday":
    price *= 0.8
else:
    print(input("Type Sat or Sun, please: "))

diff = budget - price
if budget >= price:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")