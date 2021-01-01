pastry = input().title()
number_pastries = int(input())
date_month_december = int(input())

pastry_shop_dict = {
    "before": {"Cake": 24, "Souffle": 6.66, "Baklava": 12.6},
    "after": {"Cake": 28.7, "Souffle": 9.8, "Baklava": 16.98}
}

if date_month_december <= 22:
    if date_month_december <= 15:
        price = pastry_shop_dict["before"][pastry] * number_pastries
    else:
        price = pastry_shop_dict["after"][pastry] * number_pastries

    if 100 <= price <= 200:
        price *= 0.85
    elif price > 200:
        price *= 0.75
    if date_month_december <= 15:
        price *= 0.9
else:
    price = pastry_shop_dict["after"][pastry] * number_pastries
print(f"{price:.2f}")

"""
type_cake, count_cake, day = [input() for _ in range(3)]
before, after = 'before', 'after'
items =  { before : {'Cake' : 24, 'Souffle' : 6.66, 'Baklava' :12.60},
           after : {'Cake' : 28.70, 'Souffle' : 9.80, 'Baklava' :16.98}
         }
if int(day) <= 15:
    subtotal = items[before][type_cake] * float(count_cake)
else:
    subtotal = items[after][type_cake] * float(count_cake)

total = subtotal

if int(day) <= 22:
    if 100 <= subtotal <= 200:
        total *= 0.85

    if subtotal > 200:
        total *= 0.75

    if int(day) <= 15:
        total *= 0.90

print(f'{total:.2f}')
"""