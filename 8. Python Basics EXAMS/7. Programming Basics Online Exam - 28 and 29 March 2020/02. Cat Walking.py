min_walk = int(input())
number_walk = int(input())
calories = int(input())

total_min_walk = min_walk * number_walk
burned_calories = total_min_walk * 5
calories_needed_for_good_sleep = calories * 0.5

if burned_calories >= calories_needed_for_good_sleep:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")