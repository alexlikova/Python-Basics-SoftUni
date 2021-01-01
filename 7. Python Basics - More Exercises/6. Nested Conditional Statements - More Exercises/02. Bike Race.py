import math

junior_bikers = int(input())
senior_bikers = int(input())
trace = input()

total_sum = 0

if trace == "trail":
    junior_fee = 5.5
    senior_fee = 7.0
elif trace == "cross-country":
    junior_fee = 8.0
    senior_fee = 9.50
    total_player = junior_bikers + senior_bikers
elif trace == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif trace == "road":
    junior_fee = 20
    senior_fee = 21.50
else:
    print(input("Error, type the correct trace here: "))

total_fee = junior_fee * junior_bikers + senior_fee * senior_bikers
if trace == "cross-country":
    if total_player >= 50:
        total_fee *= 0.75

donate_money_left = total_fee * 0.95 # 5% for expenses
# КАК ДА СЕ НАПРАВИ ЗАКРЪГЛЯНЕТО 377.625 на 377.63 БЕЗ да се използва функция???
print(f"{donate_money_left +0.001:.2f}")

"""
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
"""