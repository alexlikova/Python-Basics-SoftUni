capacity = float(input())

busy_capacity = 0
count = 1
command = input()
while command != "End":
    kg_suitcase = float(command)

    if count % 3 == 0 and count != 0:
        kg_suitcase *= 1.1

    if capacity <= 0:
        break
    capacity -= kg_suitcase
    command = input()
    count += 1

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")
else:
    print(f"No more space!")

print(f"Statistic: {count - 1} suitcases loaded.")

"""
contents = float(input())
goods = 0
count_luggage = 0

while True:
   luggage = input()
   
   if luggage == 'End' or contents < goods:
     if luggage == 'End':
       print('Congratulations! All suitcases are loaded!')
     else:
       print('No more space!')
       count_luggage -= 1  
     break
   else:
     if count_luggage % 3 == 0:
        goods += float(luggage) * 1.10
     else:
        goods += float(luggage)
  
   count_luggage += 1

print(f'Statistic: {count_luggage} suitcases loaded.')
"""