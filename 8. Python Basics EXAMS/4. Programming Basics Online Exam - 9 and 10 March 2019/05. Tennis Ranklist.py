import math

participated_tournaments, initial_points_ranklist = int(input()), int(input())

total_points = 0
wins = 0
for number in range(1, participated_tournaments + 1):
    reached_stage_of_tournament = input()

    if reached_stage_of_tournament == "W":
        total_points += 2000
        wins += 1
    elif reached_stage_of_tournament == "F":
        total_points += 1200
    elif reached_stage_of_tournament == "SF":
        total_points += 720
    else:
        print(input("Please, type btw W, F or SF: "))

total_points += initial_points_ranklist
average_points = math.floor((total_points - initial_points_ranklist) / participated_tournaments)
percentage_wins = (wins / participated_tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percentage_wins:.2f}%")