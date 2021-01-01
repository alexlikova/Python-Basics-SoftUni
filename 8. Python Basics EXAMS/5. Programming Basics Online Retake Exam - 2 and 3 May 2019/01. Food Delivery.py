chicken_menu = 10.35
fish_menu = 12.4
vegeterian_menu = 8.15

delivery = 2.50

number_chicken_menu, number_fish_menu, number_vegeterian_menu = [int(input()) for _ in range(3)]
price = chicken_menu * number_chicken_menu + fish_menu * number_fish_menu + vegeterian_menu * number_vegeterian_menu
dessert = price * 0.2
total_price = price + dessert + delivery

print(f"Total: {total_price:.2f}")
