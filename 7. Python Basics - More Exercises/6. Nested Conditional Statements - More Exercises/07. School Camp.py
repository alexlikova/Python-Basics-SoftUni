season = input().capitalize()
group = input().lower()
number_of_students = int(input())
nights = int(input())

price_night = 0
sport = ""
if season == "Winter":
    if group == "girls":
        price_night = 9.6
        sport = "Gymnastics"
    elif group == "boys":
        price_night = 9.6
        sport = "Judo"
    else:
        price_night = 10
        sport = "Ski"

elif season == "Spring":
    if group == "girls":
        price_night = 7.2
        sport = "Athletics"
    elif group == "boys":
        price_night = 7.2
        sport = "Tennis"
    else:
        price_night = 9.5
        sport = "Cycling"

elif season == "Summer":
    if group == "girls":
        price_night = 15
        sport = "Volleyball"
    elif group == "boys":
        price_night = 15
        sport = "Football"
    else:
        price_night = 20
        sport = "Swimming"
else:
    print(input("Choose between Winter, Spring or Summer holiday: "))

total_price = price_night * nights * number_of_students

if 10 <= number_of_students < 20:
    total_price *= 0.95
elif 20 <= number_of_students < 50:
    total_price *= 0.85
elif number_of_students >= 50:
    total_price *= 0.5

print(f"{sport} {total_price:.2f} lv.")