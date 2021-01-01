price_kg_flour, needed_kg_flour, needed_kg_sugar = [float(input()) for _ in range(3)]
number_eggshells, number_needed_yeast = int(input()), int(input())

price_kg_sugar = price_kg_flour * 0.75
price_eggshells = price_kg_flour * 1.1
price_yeast = price_kg_sugar * 0.2

total = (price_kg_flour * needed_kg_flour) + (price_kg_sugar * needed_kg_sugar) + \
        (price_eggshells * number_eggshells) + (price_yeast * number_needed_yeast)

print(f"{total:.2f}")