import math

tennis_racket_price = float(input())
number_tennis_racket = int(input())
number_pair_shoes = int(input())

price_pair_shoes = tennis_racket_price / 6

total_price_shoes_rackets = tennis_racket_price * number_tennis_racket + number_pair_shoes * price_pair_shoes

other_equipment = total_price_shoes_rackets * 0.2

total_all_equipment = total_price_shoes_rackets + other_equipment

djokovic_needs_to_pay = math.floor(total_all_equipment / 8)
sponsors_need_to_pay = math.ceil(total_all_equipment * 7 / 8)

print(f"Price to be paid by Djokovic {djokovic_needs_to_pay:.0f}")
print(f"Price to be paid by sponsors {sponsors_need_to_pay:.0f}")