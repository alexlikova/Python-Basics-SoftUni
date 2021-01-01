number_of_bottle = int(input())

bottle = 750
one_dish = 5
one_pot = 15

quantity_detergent = number_of_bottle * bottle
sum_dishes = 0
sum_pots = 0
command = input()
counter = 0
while command != "End":
    number = int(command)
    counter += 1
    if counter == 3:
        quantity_detergent = quantity_detergent - (number * one_pot)
        counter = 0
        sum_pots += number
        if quantity_detergent < 0:
            break
        command = input()
        continue
    sum_dishes += number
    quantity_detergent = quantity_detergent - (number * one_dish)
    if quantity_detergent < 0:
        break
    command = input()

if quantity_detergent >= 0:
    print(f"Detergent was enough!\n{sum_dishes} dishes and {sum_pots} pots were washed.\nLeftover detergent {quantity_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(quantity_detergent)} ml. more necessary!")