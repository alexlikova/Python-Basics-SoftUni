wanted_profit = float(input())

club_income = 0

command = input().title()

while command != "Party!":
    cocktail = int(len(command))
    number_of_cocktails = int(input())

    price = cocktail * number_of_cocktails
    if price % 2 != 0:
        price *= 0.75
    club_income += price
    if club_income >= wanted_profit:
        print(f"Target acquired.")
        break
    command = input().title()

diff = wanted_profit - club_income
if club_income < wanted_profit:
    print(f"We need {abs(diff):.2f} leva more.")

print(f"Club income - {club_income:.2f} leva.")