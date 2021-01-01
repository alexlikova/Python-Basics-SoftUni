import math

needed_hours = int(input())
days_for_project = int(input())
employees_working_overtime = int(input())

total_working_hours = 8 * days_for_project
project_working_hours = total_working_hours * 0.9 # 10% are for training

overtime_hours = employees_working_overtime * 2 * days_for_project

total_project_working_hours = project_working_hours + overtime_hours

diff = abs(total_project_working_hours - needed_hours)

if total_project_working_hours >= needed_hours:
    print(f"Yes!{math.floor(diff)} hours left.")
else:
    print(f"Not enough time!{math.ceil(diff)} hours needed.")
