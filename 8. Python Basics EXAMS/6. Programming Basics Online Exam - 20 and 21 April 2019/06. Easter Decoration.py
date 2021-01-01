basket = 1.5
wreath = 3.8
chocolate_bunny = 7

count_chocolate_bunny = 0
count_wreath = 0
count_basket = 0
total_amount = 0
total_number_sold_items = 0
customers = int(input())
for number in range(customers):
    command = input()
    while command != "Finish":
        if command == "basket":
            count_basket += 1
        elif command == "wreath":
            count_wreath += 1
        elif command == "chocolate bunny":
            count_chocolate_bunny += 1
        else:
            print(f"Error.")
        command = input()
    if command == "Finish":
        number_sold_items = count_chocolate_bunny + count_wreath + count_basket
        amount = count_basket * basket + count_wreath * wreath + count_chocolate_bunny * chocolate_bunny

        if number_sold_items % 2 == 0:
            amount *= 0.8
        total_amount += amount
        total_number_sold_items += number_sold_items
        print(f"You purchased {number_sold_items} items for {amount:.2f} leva.")
        amount = 0
        count_basket = 0
        count_wreath = 0
        count_chocolate_bunny = 0
        number_sold_items = 0
average_score = total_amount / customers
print(f"Average bill per client is: {average_score:.2f} leva.")



"""
number_clients = int(input())
loop = number_clients
price_dict = { 'basket': 1.50, 'wreath' : 3.80, 'chocolate bunny' : 7}
total_sum = 0

while loop:
    loop-= 1
    current_sum = 0
    items_count = 0

    while True:
        current_items = input()
        if current_items == 'Finish': break
        items_count += 1
        current_sum += price_dict[current_items]


    if not items_count & 1:
        current_sum *= 0.80
    total_sum += current_sum
    print(f'You purchased {items_count} items for {current_sum:.2f} leva.')


print(f'Average bill per client is: {total_sum / number_clients:.2f} leva.')
"""