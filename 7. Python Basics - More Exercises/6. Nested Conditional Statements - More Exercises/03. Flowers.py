number_hrizantemii = int(input())
number_roses = int(input())
number_laleta = int(input())
season = input()
is_day_holiday = input()

aranjirane = 2

if season == "Spring" or season == "Summer":
    hrizantemii_price = 2.0
    roses_price = 4.10
    laleta_price = 2.5

elif season == "Winter" or season == "Autumn":
    hrizantemii_price = 3.75
    roses_price = 4.50
    laleta_price = 4.15

else:
    print(input("No valid season. Try again: "))

total_price = hrizantemii_price * number_hrizantemii + laleta_price * number_laleta + roses_price * number_roses

if is_day_holiday == "Y":
    total_price *= 1.15
else:
    total_price = total_price

total_number_flowers = number_hrizantemii + number_laleta + number_roses

if total_number_flowers > 20:
    total_price *= 0.8

if number_laleta > 7 and season == "Spring":
    total_price *= 0.95

if number_roses >= 10 and season == "Winter":
    total_price *= 0.9

print(f"{total_price + aranjirane:.2f}")