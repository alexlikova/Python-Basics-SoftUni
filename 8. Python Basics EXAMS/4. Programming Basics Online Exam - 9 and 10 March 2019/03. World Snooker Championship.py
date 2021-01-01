championship_stage = input()
ticket_type = input()
tickets_number = int(input())
trophy_photo = input()

price_trophy_photo = False

snooker_championship_dict = {
    "Quarter final": {"Standard": 55.5, "Premium": 105.2, "VIP": 118.9},
    "Semi final": {"Standard": 75.88, "Premium": 125.22, "VIP": 300.4},
    "Final": {"Standard": 110.1, "Premium": 160.66, "VIP": 400}
}

price = snooker_championship_dict[championship_stage][ticket_type] * tickets_number

if price > 4000:
    price *= 0.75
    trophy_photo = "N"
elif 2500 < price <= 4000:
    price *= 0.9

if trophy_photo == "Y":
    price = price + (tickets_number * 40)

print(f"{price:.2f}")
