bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

one_bitcoin = 1168
chinese_yuan_to_usd = 0.15
usd_to_lv = 1.76
euro_to_lv = 1.95

bitcoin_lv = bitcoin * one_bitcoin
chinese_yuan_lv = chinese_yuan * chinese_yuan_to_usd * usd_to_lv
total_lv = bitcoin_lv + chinese_yuan_lv

result_lv = total_lv - (total_lv * (commission/100))
result_euro = result_lv / euro_to_lv

print(f"{result_euro:.2f}")