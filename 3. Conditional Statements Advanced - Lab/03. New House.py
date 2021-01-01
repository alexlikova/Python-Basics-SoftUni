flowers = input()
count = int(input())
budget = float(input())
result = 0

flowers_price = {
    'Roses': 5,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3,
    'Gladiolus':2.50,
}

if flowers == 'Roses' and count > 80:
    result = count * 0.90
elif flowers == 'Dahlias' and count > 90:
       result = count  * 0.85
elif flowers == 'Tulips' and count > 80:
      result = count * 0.85
elif flowers == 'Narcissus' and count < 120:
      result = count * 1.15
elif flowers == 'Gladiolus' and count < 80:
      result = count * 1.20
else:
     result = count

result *= flowers_price[flowers]
total = budget - result

if total > -1:
   print(f'Hey, you have a great garden with {count} {flowers} and {total:.2f} leva left.')
else:
   print(f'Not enough money, you need {abs(total):.2f} leva more.')

"""flower_type = input()
number_flower = int(input())
budget = float(input())

if (flower_type == "Roses"):
    price = 5.0
    cost = number_flower * price
    if (number_flower > 80):
        cost = price * 0.9 * number_flower
elif (flower_type == "Dahlias"):
    price = 3.80
    cost = number_flower * price
    if (number_flower > 90):
        cost = 0.85 * cost

elif (flower_type == "Tulips"):
    price = 2.80
    cost = number_flower * price
    if (number_flower > 80):
        cost = 0.85 * cost
elif (flower_type == "Narcissus"):
    price = 3.0
    cost = number_flower * price
    if (number_flower < 120):
        cost = 1.15 * cost
elif (flower_type == "Gladiolus"):
    price = 2.50
    cost = number_flower * price
    if (number_flower < 80):
        cost = 1.20 * cost
else:
    print()

money = budget - cost

if (budget >= cost):
    print(f"Hey, you have a great garden with {number_flower} {flower_type} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money):.2f} leva more.")"""