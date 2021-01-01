inherited_money = float(input())
year_to_live = int(input())

spent_money = 0
years = 17

for year in range(1800, year_to_live + 1):
    years += 1
    if year % 2 == 0:
        spent_money = 12000
    else:
        spent_money = (years * 50) + 12000
    inherited_money -= spent_money


if inherited_money < 0:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")


