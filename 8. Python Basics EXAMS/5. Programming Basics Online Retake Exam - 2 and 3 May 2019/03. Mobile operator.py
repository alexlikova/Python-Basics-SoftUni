term_of_contract = input().lower()
type_of_contract = input()
mobile_internet = input()
number_of_months = int(input())

mobile_operator_dict = {
    "one": {"Small": 9.98, "Middle": 18.99, "Large": 25.98, "ExtraLarge": 35.99},
    "two": {"Small": 8.58, "Middle": 17.09, "Large": 23.59, "ExtraLarge": 31.79},
}
price_per_month = 0

if mobile_internet == "yes":
    if mobile_operator_dict[term_of_contract][type_of_contract] <= 10:
        price_per_month = mobile_operator_dict[term_of_contract][type_of_contract] + 5.5
    elif mobile_operator_dict[term_of_contract][type_of_contract] <= 30:
        price_per_month = mobile_operator_dict[term_of_contract][type_of_contract] + 4.35
    else:
        price_per_month = mobile_operator_dict[term_of_contract][type_of_contract] + 3.85
else:
    price_per_month = mobile_operator_dict[term_of_contract][type_of_contract]

total_price = price_per_month * number_of_months

if term_of_contract == "two":
        total_price *= 0.9625

print(f"{total_price:.2f} lv.")