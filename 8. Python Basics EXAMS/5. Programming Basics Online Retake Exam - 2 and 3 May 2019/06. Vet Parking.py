days = int(input())
hours = int(input())
price = 0
amount = 0
total_price = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        amount += price
    total_price += amount
    print(f"Day: {day} - {amount:.2f} leva")
    amount = 0
print(f"Total: {total_price:.2f} leva")
