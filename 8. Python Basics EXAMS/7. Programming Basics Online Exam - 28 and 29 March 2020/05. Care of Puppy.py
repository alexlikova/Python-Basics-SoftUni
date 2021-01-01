quantity_food_kg = int(input())
quantity_food_gr = quantity_food_kg * 1000

total_eaten_food = 0
command = input()
while command != "Adopted":
    eaten_food = int(command)

    total_eaten_food += eaten_food
    command = input()

diff = quantity_food_gr - total_eaten_food
if diff >= 0:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {abs(diff)} grams more.")