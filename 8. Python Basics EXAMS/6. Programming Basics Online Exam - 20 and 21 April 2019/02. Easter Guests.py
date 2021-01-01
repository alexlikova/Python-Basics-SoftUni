import math

easter_bread = 4
egg = 0.45

guest, budget = int(input()), int(input())

needed_eggs = guest * 2
price_for_eggs = needed_eggs * egg
needed_easter_bread = math.ceil(guest / 3)
price_for_easter_bread = needed_easter_bread * easter_bread
total_price = price_for_eggs + price_for_easter_bread

diff = budget - total_price
if diff >= 0:
    print(f"Lyubo bought {needed_easter_bread} Easter bread and {needed_eggs} eggs.\n"
          f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {abs(diff):.2f} lv. more.")