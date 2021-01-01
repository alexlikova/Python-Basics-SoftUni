player_name = input()

initial_points = 301
successful_shots = 0
unsuccessful_shots = 0
win = False

command = input()
while command != "Retire":
    area = command
    points = int(input())

    if area == "Single":
        points *= 1
    elif area == "Double":
        points *= 2
    else:
        points *= 3

    if points < initial_points:
        successful_shots += 1
    elif points == initial_points:
        successful_shots += 1
        win = True
        break
    else:
        unsuccessful_shots += 1
        command = input()
        continue

    initial_points -= points
    command = input()

if win:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")