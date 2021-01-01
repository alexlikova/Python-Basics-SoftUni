price_easter_bread = 3.2
price_for_12eggs_eggshells = 4.35
price_for_kg_cookies = 5.4
egg_paint_for_one_egg = 0.15

number_easter_bread, number_eggshells, kg_cookies = [int(input()) for _ in range(3)]

price = (number_easter_bread * price_easter_bread) + (number_eggshells * price_for_12eggs_eggshells) + \
        (kg_cookies * price_for_kg_cookies) + (egg_paint_for_one_egg * 12 * number_eggshells)

print(f"{price:.2f}")