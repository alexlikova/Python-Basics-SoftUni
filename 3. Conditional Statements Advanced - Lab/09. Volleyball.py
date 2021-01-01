import math

year = input().lower()
p_holidays = int(input())
h_weekends_home = int(input())

total_weekends = 48

sofia_games = (total_weekends - h_weekends_home) * 3/4
roden_grad_games = h_weekends_home
holidays_games = p_holidays * 2/3

if year == "leap":
    total_games = (sofia_games + roden_grad_games + holidays_games) * 1.15
else:
    if (year == "normal"):
        total_games = (sofia_games + roden_grad_games + holidays_games)
    else:
        print("Type leap or normal:")

print(math.floor(total_games))