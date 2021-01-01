money_for_holiday = float(input())
money_now = float(input())

count_spend = 0
total_days = 0
no_money_saved = False

while money_for_holiday > money_now:
    action = input()
    amount = int(input())

    if action == "save":
        money_now += amount
        count_spend = 0
    elif action == "spend":
        money_now -= amount
        count_spend += 1
        if money_now <= 0:
            money_now = 0
        if count_spend == 5:
            no_money_saved = True
            break
    total_days += 1

if no_money_saved:
    print(f"You can't save the money.\n{count_spend}")
else:
    print(f"You saved the money for {total_days} days.")