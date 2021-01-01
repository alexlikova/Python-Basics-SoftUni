width = int(input())
lenght = int(input())
cake = width * lenght

command = input()
total_piece_cake = 0
cake_finished = False

while command != "STOP":
    pieces_cake = int(command)
    total_piece_cake += pieces_cake

    if total_piece_cake >= cake:
        cake_finished = True
        break

    command = input()

difference = abs(total_piece_cake - cake)
if cake_finished:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")
