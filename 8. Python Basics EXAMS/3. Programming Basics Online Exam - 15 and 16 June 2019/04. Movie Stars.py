budget = float(input())

total_salary = 0
budget_is_finished = False
command = input().upper()
while command != "ACTION":

    name_actor = command
    if len(name_actor) <= 15:
        salary = float(input())
    else:
        salary = budget * 0.2
    total_salary += salary
    budget -= salary
    if budget <= 0:
        budget_is_finished = True
        break
    command = input()

if budget_is_finished:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {abs(budget):.2f} leva.")
