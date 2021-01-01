budget = float(input())
workers = int(input())
price_for_worker = float(input())

decor = budget * 0.1
price_clothes = workers * price_for_worker
if workers > 150:
    price_clothes *= 0.9

total = price_clothes + decor

diff = budget - total
if budget >= total:
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {abs(diff):.2f} leva more.")