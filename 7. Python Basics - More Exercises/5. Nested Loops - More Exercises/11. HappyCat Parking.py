days, hours = [int(input()) for _ in range(2)]
fee = 0
day_sum = 0
total = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 == 1:
            fee = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            fee = 1.25
        else:
            fee = 1
        day_sum += fee
        total += fee
    print(f"Day: {day} - {day_sum:.2f} leva")
    day_sum = 0
print(f"Total: {total:.2f} leva")

"""
days, hours = [int(input()) + 1 for _ in range(2)]
current_tax, total_sum = 0, 0

for day in range(1, days):
    for hour in range(1, hours):
        if not day & 1 and hour & 1:
            current_tax += 2.50
        elif day & 1 and not hour & 1:
            current_tax += 1.25
        else:
            current_tax += 1.00
    print(f'Day: {day} - {current_tax:.2f} leva')
    total_sum += current_tax
    current_tax = 0

print(f'Total: {total_sum:.2f} leva')
"""