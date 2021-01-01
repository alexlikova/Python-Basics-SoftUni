fruit, size = input().title(), input().lower()
orders = int(input())

energy_booster_dict = {
    "small": {"Watermelon": 56, "Mango": 36.66, "Pineapple": 42.1, "Raspberry": 20},
    "big": {"Watermelon": 28.7, "Mango": 19.6, "Pineapple": 24.8, "Raspberry": 15.2}
}

if size == "small":
    price = energy_booster_dict[size][fruit] * orders * 2
else:
    price = energy_booster_dict[size][fruit] * orders * 5

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")