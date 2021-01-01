team = input()

games_played = int(input())

result_list = [input() for _ in range(games_played)]

win = result_list.count('W')
equal = result_list.count('D')
lose = result_list.count('L')

win_points = win * 3
equal_points = equal * 1
lose_points = lose * 0
total_points = win_points + equal_points + lose_points

if games_played >= 1:
    print(f"{team} has won {total_points} points during this season.\nTotal stats:")
    print(f"## W: {win}")
    print(f"## D: {equal}")
    print(f"## L: {lose}")
    print(f"Win rate: {(win / games_played) * 100 :.2f}%")
else:
    print(f"{team} hasn't played any games during this season.")