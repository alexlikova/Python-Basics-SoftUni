import sys

easter_bread = int(input())

sum_grades = 0
max_points = - sys.maxsize
number_one = ""
for number in range(1, easter_bread + 1):
    name = input()
    while True:
        command = input()
        if sum_grades > max_points:
            max_points = sum_grades
            number_one = name
        if command == "Stop":
            print(f"{name} has {sum_grades} points.")
            if number_one == name and max_points == sum_grades:
                print(f"{number_one} is the new number 1!")
            sum_grades = 0
            break
        grade = int(command)
        sum_grades += grade

print(f"{number_one} won competition with {max_points} points!")

"""
number_players = int(input())
max_points = 0
winner = ''

while number_players:
    number_players -= 1
    current_points = 0
    chef_name = input()
    while True:
        try:
            current_points += int(input())
        except:
            break

    print(f'{chef_name} has {current_points} points.')

    if max_points < current_points:
        max_points = current_points
        winner = f'{chef_name} won competition with {max_points} points!'
        print(f'{chef_name} is the new number 1!')

print(winner)
"""