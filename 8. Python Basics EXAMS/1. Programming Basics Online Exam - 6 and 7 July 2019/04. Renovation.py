import math

#height = int(input())
#width = int(input())
#percent_not_painted = int(input())

height, width, percent_not_painted = [int(input()) for _ in range(3)]
walls = 4
total_area = height * width * walls
total_area_painting = int(math.ceil(total_area * (1 - (percent_not_painted / 100))))

painting_is_finished = False

command = input().title()

while command != "Tired!":
    liters_paint = int(command)
    total_area_painting -= liters_paint
    if total_area_painting <= 0:
        painting_is_finished = True
        break

    command = input().title()

if painting_is_finished:
    if total_area_painting < 0:
        print(f"All walls are painted and you have {abs(total_area_painting):.0f} l paint left!")
    elif total_area_painting == 0:
        print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"{total_area_painting:.0f} quadratic m left.")