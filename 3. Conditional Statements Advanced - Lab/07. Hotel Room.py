month = input().lower()
nights = int(input())

apartament_price = 0.0
studio_price = 0.0

if month == "may" or month == "october":
    studio_price = 50
    apartament_price = 65
    if (7 < nights <= 14):
        studio_price *= 0.95
    elif (nights > 14):
        apartament_price *= 0.9
        studio_price *= 0.7

elif month == "june" or month == "september":
    studio_price = 75.2
    apartament_price = 68.7
    if (nights > 14):
        apartament_price *= 0.9
        studio_price *= 0.8

elif month == "july" or month == "august":
    studio_price = 76
    apartament_price = 77
    if (nights > 14):
        apartament_price *= 0.9

else:
    print("Type a month btw may, october, july, august or september")

total_price_studio = studio_price * nights
total_price_apartment = apartament_price * nights
print(f"Apartment: {total_price_apartment:.2f} lv.\nStudio: {total_price_studio:.2f} lv.")
