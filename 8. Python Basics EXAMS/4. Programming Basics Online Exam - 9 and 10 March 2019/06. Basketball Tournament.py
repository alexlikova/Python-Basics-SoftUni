win = 0
lose = 0
total_games = 0
command = input()
while command != "End of tournaments":
    tournaments = int(input())
    for tournament_number in range(1, tournaments + 1):
        tournament_name = command
        for game in range(1, tournaments + 1):
            total_games += 1
            score_first_team = int(input())
            score_second_team = int(input())

            diff = score_first_team - score_second_team
            if score_first_team > score_second_team:
                win += 1
                print(f"Game {game} of tournament {tournament_name}: win with {diff:.0f} points.")
            elif score_first_team < score_second_team:
                lose += 1
                print(f"Game {game} of tournament {tournament_name}: lost with {abs(diff):.0f} points.")
        command = input()

        if command == "End of tournaments":
            break
        #n = int(input())

print(f"{win / total_games * 100:.2f}% matches win")
print(f"{lose / total_games * 100:.2f}% matches lost")

"""

all_game_counter = 0
win, lost = 0, 0

while True:
    tournament_name = input()
    if tournament_name == 'End of tournaments':
        break

    current_game_current = 0
    game_numbers = int(input())

    all_game_counter += game_numbers

    for _ in range(game_numbers):
        current_game_current += 1
        host = int(input())
        guest = int(input())

        if host > guest:
            win += 1
            print(f'Game {current_game_current} of tournament {tournament_name}: win with {host - guest} points.')
        else:
            lost += 1
            print(f'Game {current_game_current} of tournament {tournament_name}: lost with {guest - host} points.')

print(f'{win / all_game_counter * 100:.2f}% matches win')
print(f'{lost / all_game_counter * 100:.2f}% matches lost')
"""