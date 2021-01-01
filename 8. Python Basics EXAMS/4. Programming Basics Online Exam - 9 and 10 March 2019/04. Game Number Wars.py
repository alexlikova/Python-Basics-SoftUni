first_player, second_player = [input() for _ in range(2)]

points_first_player = 0
points_second_player = 0
number_wars = False
command = input()
while command != "End of game":

    first_play_card = int(command)
    second_play_card = int(input())

    diff = first_play_card - second_play_card
    if first_play_card > second_play_card:
        points_first_player += diff
    elif first_play_card < second_play_card:
        points_second_player += abs(diff)
    else:
        number_wars = True
        break
    command = input()

if number_wars:
    first_play_card = int(input())
    second_play_card = int(input())

    diff = first_play_card - second_play_card
    if diff > 0:
        print(f"Number wars!\n{first_player} is winner with {points_first_player} points")
    else:
        print(f"Number wars!\n{second_player} is winner with {points_second_player} points")

if command == "End of game":
    print(f"{first_player} has {points_first_player} points")
    print(f"{second_player} has {points_second_player} points")
    exit()

"""
first_player, second_player = [input() for _ in range(2)]

points_first_player = 0
points_second_player = 0
number_wars = False
command = input()

while command != "End of game":

    first_play_card = int(command)
    second_play_card = int(input())

    diff = first_play_card - second_play_card
    if first_play_card > second_play_card:
        points_first_player += diff
    elif first_play_card < second_play_card:
        points_second_player += abs(diff)
    else:
        number_wars = True
        #points_first_player = 0
        #points_second_player = 0
        command = input()
        continue
    if number_wars:
        break
    command = input()

if number_wars:
    if diff > 0:
        print(f"Number wars!\n{first_player} is winner with {points_first_player} points")
    else:
        print(f"Number wars!\n{second_player} is winner with {points_second_player} points")

if command == "End of game":
    print(f"{first_player} has {points_first_player} points")
    print(f"{second_player} has {points_second_player} points")
    exit()"""

"""
name_player_one = input()
name_player_two = input()
points_player_one = 0
points_player_two = 0

while True:
    try:
        card_player_one = int(input())
    except:
        print(f'{name_player_one} has {points_player_one} points')
        print(f'{name_player_two} has {points_player_two} points')
        break
    card_player_two = int(input())

    if card_player_one > card_player_two:
        points_player_one += card_player_one - card_player_two
    elif card_player_one < card_player_two:
        points_player_two += card_player_two - card_player_one
    else:
        print('Number wars!')
        card_player_one = int(input())
        card_player_two = int(input())

        if card_player_one > card_player_two:
            print(f'{name_player_one} is winner with {points_player_one} points')
        else:
            print(f'{name_player_two} is winner with {points_player_two} points')
        break
"""