import math

number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_cactus = int(input())
price_present = float(input())

magnolii = 3.25
zumbuli = 4.0
roses = 3.5
cactus = 8.0

price_magnolii = magnolii * number_magnolii
price_zumbuli = zumbuli * number_zumbuli
price_roses = roses * number_roses
price_cactus = cactus * number_cactus

total_price = price_roses + price_cactus + price_magnolii + price_zumbuli
net_profit = total_price * 0.95

diff = abs(net_profit - price_present)

if net_profit >= price_present:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva." )
