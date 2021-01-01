guests = int(input())
price_for_one_person = float(input())
budget = float(input())
cake = budget * 0.1
price = guests * price_for_one_person
if 10 <= guests <= 15:
    price *= 0.85
elif 15 < guests <= 20:
    price *= 0.8
elif guests > 20:
    price *= 0.75

total_price = price + cake
diff = budget - total_price
if budget >= total_price:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")
