budget = float(input())

count_bought_products = 0
total_amount = 0
money_not_enough = False
total_count = 0
command = input()
while command != "Stop":
    product_name = command
    product_price = float(input())
    count_bought_products += 1
    total_count += 1
    if count_bought_products == 3:
        product_price /= 2
        count_bought_products = 0

    total_amount += product_price
    if budget < total_amount:
        money_not_enough = True
        break
    command = input()

if command == "Stop":
    print(f"You bought {total_count} products for {total_amount:.2f} leva.")

diff = total_amount - budget
if money_not_enough:
    print(f"You don't have enough money!\n"
          f"You need {diff:.2f} leva!")

"""
budget = float(input())
spend_money = 0
buy_item_count = 0
item = input()

while item != 'Stop':
    buy_item_count += 1
    item_price = float(input())

    if buy_item_count % 3 == 0:
      spend_money += item_price / 2
    else:
      spend_money += item_price

    if budget < spend_money:
      print(f"You don't have enough money!\nYou need {spend_money - budget:.2f} leva!")
      exit()
    item = input()

print(f"You bought {buy_item_count} products for {spend_money:.2f} leva.")
"""