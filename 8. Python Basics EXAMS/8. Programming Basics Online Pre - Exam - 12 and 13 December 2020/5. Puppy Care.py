bought_food_kg = int(input())
bought_food_grams = bought_food_kg * 1000

command = input()
while command != "Adopted":
    eaten_food = int(command)

    bought_food_grams -= eaten_food
    command = input()

if bought_food_grams >= 0:
    print(f"Food is enough! Leftovers: {bought_food_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(bought_food_grams)} grams more.")