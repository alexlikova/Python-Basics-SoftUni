win, loss, equal = 0, 0, 0

for _ in range(3):
    host, guest = input().split(':')
    if host > guest:
        win += 1
    elif host < guest:
        loss += 1
    else:
        equal += 1

print(f'Team won {win} games.\nTeam lost {loss} games.\nDrawn games: {equal}')


"""result_first_game, result_second_game, result_third_game = [input() for _ in range(3)]

win = 0
lose = 0
equal = 0

if result_first_game[0] > result_first_game[2]:
    win += 1
elif result_first_game[0] < result_first_game[2]:
    lose += 1
else:
    equal += 1

if result_second_game[0] > result_second_game[2]:
    win += 1
elif result_second_game[0] < result_second_game[2]:
    lose += 1
else:
    equal += 1

if result_third_game[0] > result_third_game[2]:
    win += 1
elif result_third_game[0] < result_third_game[2]:
    lose += 1
else:
    equal += 1

print(f"Team won {win} games.\nTeam lost {lose} games.\n"
      f"Drawn games: {equal}")"""