game_play = int(input())

numbers_dict = {"From 0 to 9": 0, "From 10 to 19": 0, "From 20 to 29": 0, "From 30 to 39": 0, "From 40 to 50": 0,
                "total_sum": 0, "invalid": 0}

for number in range(game_play):
    number_play = int(input())

    if 0 <= number_play <= 9:
        points = number_play * 0.2
        numbers_dict["From 0 to 9"] += 1
    elif 10 <= number_play <= 19:
        points = number_play * 0.3
        numbers_dict["From 10 to 19"] += 1
    elif 20 <= number_play <= 29:
        points = number_play * 0.4
        numbers_dict["From 20 to 29"] += 1
    elif 30 <= number_play <= 39:
        points = 50
        numbers_dict["From 30 to 39"] += 1
    elif 40 <= number_play <= 50:
        points = 100
        numbers_dict["From 40 to 50"] += 1
    else: #invalid number if it is below 0 or above 50
        numbers_dict["invalid"] += 1

    if 0 <= number_play <= 50:
        numbers_dict["total_sum"] += points
    else:
        numbers_dict["total_sum"] = numbers_dict["total_sum"] / 2

total_sum = numbers_dict["total_sum"]
zero_nine_percent = numbers_dict["From 0 to 9"] / game_play * 100
ten_nineteen_percent = numbers_dict["From 10 to 19"] / game_play * 100
twenty_twentyNine_percent = numbers_dict["From 20 to 29"] / game_play * 100
thirty_thirtyNine_percent = numbers_dict["From 30 to 39"] / game_play * 100
forty_fifty_percent = numbers_dict["From 40 to 50"] / game_play * 100
invalid_percent = numbers_dict["invalid"] / game_play * 100

print(f"{total_sum:.2f}")
print(f"From 0 to 9: {zero_nine_percent:.2f}%")
print(f"From 10 to 19: {ten_nineteen_percent:.2f}%")
print(f"From 20 to 29: {twenty_twentyNine_percent:.2f}%")
print(f"From 30 to 39: {thirty_thirtyNine_percent:.2f}%")
print(f"From 40 to 50: {forty_fifty_percent:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")

"""
from collections import OrderedDict
move = int(input())
points = 0

percent_dict = OrderedDict()
percent_dict['From 0 to 9:'] = 0
percent_dict['From 10 to 19:'] = 0
percent_dict['From 20 to 29:'] = 0
percent_dict['From 30 to 39:'] = 0
percent_dict['From 40 to 50:'] = 0
percent_dict['Invalid numbers:'] = 0


for _ in range(move):
    num = int(input())
    if  0 <= num <= 9:
        points += num * 0.20
        percent_dict['From 0 to 9:'] += 1
    elif 10 <= num <= 19:
        points += num * 0.30
        percent_dict['From 10 to 19:'] += 1
    elif 20 <= num <= 29:
        points += num * 0.40
        percent_dict['From 20 to 29:'] += 1
    elif 30 <= num <= 39:
        points += 50
        percent_dict['From 30 to 39:'] += 1
    elif 40 <= num <= 50:
        points += 100
        percent_dict['From 40 to 50:'] += 1
    else:
        points /= 2
        percent_dict['Invalid numbers:'] += 1
        
print(f'{points:.2f}')

for k,v in percent_dict.items():
    print(f'{k} {v / move * 100:.2f}%')

"""