number_locations = int(input())

for location in range(number_locations):
    expected_average_daily_yield_gold = float(input())
    days = int(input())

    total_gold_for_day = 0

    for day in range(days):
        yield_gold = float(input())
        total_gold_for_day += yield_gold

    total_average_gold = total_gold_for_day / days
    diff = total_average_gold - expected_average_daily_yield_gold
    if diff >= 0:
        print(f"Good job! Average gold per day: {total_average_gold:.2f}.")
    else:
        print(f"You need {abs(diff):.2f} gold.")