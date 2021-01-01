campaign_days = int(input())
pastry_cook = int(input())
number_cakes = int(input())
number_gofreti = int(input())
number_pankaces = int(input())

cake = 45
gofreta = 5.8
pancake = 3.2

total_price_cakes = cake * number_cakes
total_price_gofreti = gofreta * number_gofreti
total_price_pancakes = pancake * number_pankaces

total_amount_one_pastry_cook = total_price_cakes + total_price_gofreti + total_price_pancakes
total_amount_one_day = total_amount_one_pastry_cook * pastry_cook
total_amount_whole_campaign = total_amount_one_day * campaign_days

net_profit = total_amount_whole_campaign * 7/8

print(net_profit)