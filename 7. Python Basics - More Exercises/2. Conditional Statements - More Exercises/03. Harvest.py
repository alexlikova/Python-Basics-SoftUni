import math

x_area_vineyard = int(input())
y_grape_for_l = float(input())
z_sale_wine = int(input())
workers = int(input())

one_l_wine = 2.5

total_grape = x_area_vineyard * y_grape_for_l
harvest_wine = (total_grape * 0.4) / one_l_wine # zadeleno za proizvodstvo na vino

diff = abs(harvest_wine - z_sale_wine)
wine_for_one_worker = diff / workers

if harvest_wine >= z_sale_wine:
    print(f"Good harvest this year! Total wine: {math.floor(harvest_wine)} liters."
          f"\n{math.ceil(diff)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")