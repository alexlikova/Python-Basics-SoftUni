import math

days = int(input())
food_left_kg = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_gr = float(input())

turtle_food_kg = turtle_food_gr / 1000

total_food_dog = dog_food_day * days
total_food_cat = cat_food_day * days
total_food_turtle = turtle_food_kg * days

total_food = total_food_cat + total_food_dog + total_food_turtle

diff = abs(total_food - food_left_kg)
if total_food > food_left_kg:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
else:
    print(f"{math.floor(diff)} kilos of food left.")

