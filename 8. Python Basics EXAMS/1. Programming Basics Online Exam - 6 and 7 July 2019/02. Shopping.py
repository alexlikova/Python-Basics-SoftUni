import math

budget = float(input())
number_videocards, number_processors, number_ram_memeory = [int(input()) for _ in range(3)]

videocard = 250
total_price_videocards = videocard * number_videocards
processor = total_price_videocards * 0.35
ram_memory = total_price_videocards * 0.1

total = (number_videocards * videocard) + (number_processors * processor) + (number_ram_memeory * ram_memory)

if number_videocards > number_processors:
    total *= 0.85

diff = budget - total

if diff >= 0:
    print(f"You have {abs(diff):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva more!")
