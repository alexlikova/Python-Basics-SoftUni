drink = input().title()
sugar = input().title()
number_of_drinks = int(input())

drinks_dict = {
    "Espresso": {"Without": 0.9, "Normal": 1, "Extra": 1.20},
    "Cappuccino": {"Without": 1, "Normal": 1.2, "Extra": 1.60},
    "Tea": {"Without": 0.5, "Normal": 0.6, "Extra": 0.7}
}

order = drinks_dict[drink][sugar] * number_of_drinks

if drink == 'Espresso' and number_of_drinks > 4:
    order *= 0.75

if sugar == 'Without':
    order *= 0.65

if order > 15.0:
    order *= 0.80

print(f'You bought {number_of_drinks} cups of {drink} for {order:.2f} lv.')

"""if not drink in drinks_dict or number_of_drinks < 0:
    print("error")
    exit()"""