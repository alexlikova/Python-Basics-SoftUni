eggs_first_player = int(input())
eggs_second_player = int(input())

command = input()
game_has_finished = False
while command != "End of battle":
    winner = command

    if command == "one":
        eggs_second_player -= 1
    elif command == "two":
        eggs_first_player -= 1
    else:
        print(input("Type one or two, pleas: "))

    if eggs_first_player <= 0:
        print(f"Player one is out of eggs. Player two has {eggs_second_player} eggs left.")
        break
    elif eggs_second_player <= 0:
        print(f"Player two is out of eggs. Player one has {eggs_first_player} eggs left.")
        break
    command = input()

if command == "End of battle":
    print(f"Player one has {eggs_first_player} eggs left.\n"
          f"Player two has {eggs_second_player} eggs left.")