budget = float(input())
nights = int(input())
lv_night = float(input())
percent_add_expenses = int(input())

if nights > 7:
    lv_night *= 0.95

price = lv_night * nights
add_expenses = budget * (percent_add_expenses / 100)
total_price = price + add_expenses

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")