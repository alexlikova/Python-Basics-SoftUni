total_number_of_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k_two = 0
everest = 0
total_people = 0
for group in range(1, total_number_of_groups + 1):
    people_in_the_group = int(input())

    if people_in_the_group <= 5:
        musala += people_in_the_group
    elif 6 <= people_in_the_group <= 12:
        monblan += people_in_the_group
    elif 13 <= people_in_the_group <= 25:
        kilimandjaro += people_in_the_group
    elif 26 <= people_in_the_group <= 40:
        k_two += people_in_the_group
    else:
        everest += people_in_the_group

    total_people += people_in_the_group

print(f"{musala / total_people * 100:.2f}%")
print(f"{monblan / total_people * 100:.2f}%")
print(f"{kilimandjaro / total_people * 100:.2f}%")
print(f"{k_two / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")


"""
groups = int(input())
all_people = 0
g1, g2, g3, g4, g5 = 0, 0, 0, 0, 0

for _ in range(groups):
   people = int(input())
   all_people += people 

   if people <= 5:
      g1 += people
   elif people >= 6 and people <= 12:
      g2 += people
   elif people >= 13 and people <= 25:
      g3 += people
   elif people >= 26 and people <= 40:
      g4 += people
   else:
      g5 += people

print(f'{(g1 / all_people * 100):.2f}%')
print(f'{(g2 / all_people * 100):.2f}%')
print(f'{(g3 / all_people * 100):.2f}%')
print(f'{(g4 / all_people * 100):.2f}%')
print(f'{(g5 / all_people * 100):.2f}%')
"""