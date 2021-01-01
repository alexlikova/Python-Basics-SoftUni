sold_games = int(input())

#games = {"Hearthstone", "Fornite", "Overwatch", "Other"}
counter_hearthstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_other = 0
for n in range(1, sold_games + 1):
    game_name = input().title()
    if game_name == "Hearthstone":
        counter_hearthstone += 1
    elif game_name == "Fornite":
        counter_fornite += 1
    elif game_name == "Overwatch":
        counter_overwatch += 1
    else:
        counter_other += 1

percent_hearthstone = counter_hearthstone / sold_games * 100
percent_fornite = counter_fornite / sold_games * 100
percent_overwatch = counter_overwatch / sold_games * 100
percent_other = counter_other / sold_games * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_other:.2f}%")

"""
ceil_games = int(input())
game_list = [ input() for _ in range(ceil_games)]

hearthstone = game_list.count('Hearthstone')
fornite = game_list.count('Fornite')
overwatch = game_list.count('Overwatch')

first_game = hearthstone / ceil_games * 100
second_game = fornite / ceil_games * 100
three_game = overwatch / ceil_games * 100
all_games_sum = abs((first_game + second_game + three_game) - 100)

print(f'Hearthstone - {first_game:.2f}%\nFornite - {second_game:.2f}%\nOverwatch - {three_game:.2f}%')
print(f'Others - {all_games_sum:.2f}%')

"""