number_of_cats = int(input())

price_kg_food = 12.45
small_cats = 0
big_cats = 0
huge_cats = 0
total_gr_food = 0

for cat in range(1, number_of_cats + 1):
    gram_food_cat = float(input())

    if 100 <= gram_food_cat < 200:
        small_cats += 1
    elif 200 <= gram_food_cat < 300:
        big_cats += 1
    elif 300 <= gram_food_cat < 400:
        huge_cats += 1
    total_gr_food += gram_food_cat

total_price = (total_gr_food / 1000) * price_kg_food

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")