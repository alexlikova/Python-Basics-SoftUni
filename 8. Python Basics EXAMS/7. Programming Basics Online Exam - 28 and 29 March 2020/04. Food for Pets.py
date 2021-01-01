days = int(input())
quantity_food = float(input())

total_food_dog = 0
total_food_cat = 0
total_biscuits = 0
for day in range(1, days + 1):
    eaten_food_dog = int(input())
    eaten_food_cat = int(input())

    total_food_dog += eaten_food_dog
    total_food_cat += eaten_food_cat

    if day % 3 == 0:
        current_biscuits = (eaten_food_dog + eaten_food_cat) * 0.1
        total_biscuits += current_biscuits

total_eaten_food = total_food_dog + total_food_cat
print(f"Total eaten biscuits: {total_biscuits:.0f}gr.")
print(f"{total_eaten_food / quantity_food * 100:.2f}% of the food has been eaten.")
print(f"{total_food_dog / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{total_food_cat / total_eaten_food * 100:.2f}% eaten from the cat.")
