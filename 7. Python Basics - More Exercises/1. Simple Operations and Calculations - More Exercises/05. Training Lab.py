width = float(input())
length = float(input())

coridor_cm = 100 # coridor 100sm from width

width_cm = width * 100
length_cm = length * 100

desk_per_row = int((length_cm - coridor_cm) / 70) # 1 desk is 70 sm
rows = int((width_cm / 120))

catedra_door = 3

total_desks = (desk_per_row * rows) - catedra_door

print(f"{total_desks:.0f}")
