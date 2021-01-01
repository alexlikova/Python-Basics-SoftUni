days = int(input())
room = str(input()).lower()
feedback = str(input()).lower()

nights = days - 1

room_one_person = 18
apartment = 25
president_apartment = 35
price = 0.0

if room == "room for one person":
    price = room_one_person * nights

elif room == "apartment":
    if 0 < nights <= 10:
        price = apartment * 0.7 * nights
    elif 10 < nights <= 15:
        price = apartment * 0.65 * nights

    else:
        price = apartment * 0.5 * nights

elif room == "president apartment":
    price = president_apartment * nights

    if 0 < nights <= 10:
        price *= 0.9
    elif 10 < nights <= 15:
        price *= 0.85
    else:
        price *= 0.8

if feedback == "positive":
    price = price * 1.25
else:
    price = price * 0.9
print(f"{price:.2f}")
