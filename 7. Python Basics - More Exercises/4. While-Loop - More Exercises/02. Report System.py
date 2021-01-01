needed_money = int(input())

total_sum = 0
sum_cash = 0
sum_cc = 0
counter = 0
cash_counter = 0
cc_counter = 0

command = input().capitalize()

while command != "End":
    amount = int(command)
    counter += 1
    if counter % 2 != 0: # odd --> cash
        if amount > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            sum_cash += amount
            total_sum += amount
            print("Product sold!")

    else: # even --> credit card
        if amount < 10:
            print("Error in transaction!")
        else:
            cc_counter += 1
            sum_cc += amount
            total_sum += amount
            print("Product sold!")

    if total_sum >= needed_money:
        print(f"Average CS: {sum_cash / cash_counter:.2f}\nAverage CC: {sum_cc / cc_counter:.2f}")
        break
    command = input().title()

if command == "End":
    print("Failed to collect required money for charity.")
