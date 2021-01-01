budget = float(input())
sezon = str(input())
number_people = int(input())

naem = 0.0

if (sezon == "Spring"):
    naem = 3000
    if (0 < number_people <= 6):
        naem *= 0.9 #10%
    elif (6 < number_people <= 11):
        naem *= 0.85 #15%
    elif (number_people >= 12):
        naem *= 0.75 # 25%
elif (sezon == "Summer" or sezon == "Autumn"):
    naem = 4200
    if (0 < number_people <= 6):
        naem *= 0.9
    elif (7 <= number_people <= 11):
        naem *= 0.85
    elif (number_people >= 12):
        naem *= 0.75
elif (sezon == "Winter"):
    naem = 2600
    if (0 < number_people <= 6):
        naem *= 0.9
    elif (6 < number_people <= 11):
        naem *= 0.85
    elif (number_people > 11):
        naem *= 0.75
#else:
    #print("Type the season again: ")

if (number_people %2 ==0 and sezon != "Autumn"):
    naem *= 0.95

money = budget - naem

if (money >= 0):
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {(abs(money)):.2f} leva.")