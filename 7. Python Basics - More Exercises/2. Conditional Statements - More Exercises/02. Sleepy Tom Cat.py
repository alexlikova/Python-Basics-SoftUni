import math

days = int(input())

work_day_play = 63
holiday_play = 127
norm_play_game = 30_000

total_holiday_play = days * holiday_play
total_work_day_play = (365 - days) * work_day_play

total_play = total_work_day_play + total_holiday_play

diff = abs(total_play - norm_play_game)
hours = diff // 60
min = diff % 60

if total_play <= norm_play_game:

    print(f"Tom sleeps well\n{hours:.0f} hours and {min} minutes less for play")
else:
    print(f"Tom will run away\n{hours:.0f} hours and {min} minutes more for play")