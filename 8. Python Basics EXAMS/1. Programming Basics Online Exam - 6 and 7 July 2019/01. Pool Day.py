import math

people = int(input())
entrance_fee = float(input())
deck_chair = float(input())
umbrella = float(input())

total_entrance_fee = people * entrance_fee
total_price_deck_chair = (math.ceil((people * 0.75)) * deck_chair)
total_price_umbrella = (math.ceil(people / 2) * umbrella)

total = total_price_deck_chair + total_entrance_fee + total_price_umbrella
print(f"{total:.2f} lv.")
