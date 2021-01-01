import math

name = input()
budget = float(input())
bottles_beer = int(input())
number_chips = int(input())

price_beer = 1.2
total_price_beer = price_beer * bottles_beer
price_chips = total_price_beer * 0.45
total_price_chips = math.ceil(price_chips * number_chips)

total_price = total_price_chips + total_price_beer

diff = budget - total_price
if budget >= total_price:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {abs(diff):.2f} more leva!")