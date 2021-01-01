import math

price_one_videocard = int(input())
price_one_prehodnik = int(input())
price_electricity_videocard_day= float(input())
profit_videocard_day = float(input())

total_price_videocards = price_one_videocard * 13
total_price_prehodnici = price_one_prehodnik * 13
other_components_machine = 1000
total_cost = total_price_videocards + total_price_prehodnici + other_components_machine

total_profit_videocard_day = profit_videocard_day - price_electricity_videocard_day
total_profit_from_videocards = total_profit_videocard_day * 13

return_money_in_days = math.ceil(total_cost / total_profit_from_videocards)

print(f"{total_cost}\n{return_money_in_days}")