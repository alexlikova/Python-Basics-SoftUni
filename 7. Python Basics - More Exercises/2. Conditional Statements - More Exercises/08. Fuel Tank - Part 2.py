type_fuel = input().capitalize()
liter_fuel = float(input())
club_card = input().capitalize()

gasoline = 2.22
diesel = 2.33
gas = 0.93

price = 0

if club_card == "Yes":
    if type_fuel == "Gasoline":
        discount = 0.18
        price = gasoline - discount
    elif type_fuel == "Diesel":
        discount = 0.12
        price = diesel - discount
    elif type_fuel == "Gas":
        discount = 0.08
        price = gas - discount
    else:
        print("Error")
    price = price * liter_fuel

else:
    if type_fuel == "Gasoline":
        price = liter_fuel * gasoline
    elif type_fuel == "Diesel":
        price = liter_fuel * diesel
    elif type_fuel == "Gas":
        price = liter_fuel * gas
    else:
        print("Error")

if 20 <= liter_fuel <= 25:
    price = price * 0.92
elif liter_fuel > 25:
    price = price * 0.9

print(f"{price:.2f} lv.")

# ДА Я РЕША СЪС switch case
# ДА Я РЕША СЪС switch case
# ДА Я РЕША СЪС switch case

"""
type_fuel = input().capitalize()
liter_fuel = float(input())
club_card = input().capitalize()

gasoline = 2.22
diesel = 2.33
gas = 0.93

price = 0

def fuel_tank(type_fuel):
    switcher = {
        club_card == "Yes":
            if



    }
"""