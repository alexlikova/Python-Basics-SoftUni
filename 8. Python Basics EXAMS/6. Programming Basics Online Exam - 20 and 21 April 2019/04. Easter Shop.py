initial_number_of_eggs = int(input())

sold_eggs = 0
command = input()
while command != "Close":
    number_of_eggs = int(input())
    if command == "Fill":
        initial_number_of_eggs += number_of_eggs
    elif command == "Buy":
        if initial_number_of_eggs >= number_of_eggs:
            initial_number_of_eggs -= number_of_eggs
            sold_eggs += number_of_eggs
        else:
            print(f"Not enough eggs in store!\n"
                  f"You can buy only {initial_number_of_eggs}.")
            exit()
    command = input()

if command == "Close":
    print(f"Store is closed!\n"
          f"{sold_eggs} eggs sold.")


"""all_eggs = int(input())
total_bought_eggs = 0

while True:
    command = input()
    if command == 'Close':
        print(f'Store is closed!\n{total_bought_eggs} eggs sold.')
        break

    eggs_count = int(input())

    if command == 'Buy':
        if all_eggs >= eggs_count:
            all_eggs -= eggs_count
            total_bought_eggs += eggs_count
        else:
            print(f'Not enough eggs in store!\nYou can buy only {all_eggs}.')
            break
    elif command == 'Fill':
        all_eggs += eggs_count"""
