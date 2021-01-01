name_actor = input()
initial_points = float(input())
number_people_that_evaluate = int(input())

for number in range(1, number_people_that_evaluate + 1):
    name_person_evaluates = input()
    points_person_evaluates = float(input())

    real_points_evaluating_person = (len(name_person_evaluates) * points_person_evaluates) / 2

    initial_points += real_points_evaluating_person

    if initial_points > 1250.5:
        break

diff = abs(1250.5 - initial_points)
if initial_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {initial_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")