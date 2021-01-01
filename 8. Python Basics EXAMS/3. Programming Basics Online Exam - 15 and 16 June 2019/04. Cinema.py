capacity = int(input())

cinema_is_full = False
busy_space = 0
cinema_income = 0
command = input()
while command != "Movie time!":
    number = int(command)
    if number % 3 != 0:
        price = number * 5
    else:
        price = (number * 5) - 5
    busy_space += number
    if busy_space > capacity:
        cinema_is_full = True
        break
    cinema_income += price
    command = input()

diff = capacity - busy_space
if cinema_is_full:
    print(f"The cinema is full.")
else:
    print(f"There are {diff} seats left in the cinema.")

print(f"Cinema income - {cinema_income} lv.")