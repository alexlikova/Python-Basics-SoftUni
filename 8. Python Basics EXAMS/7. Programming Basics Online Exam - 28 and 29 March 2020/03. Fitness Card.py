budget = float(input())
sex = input().lower()
age = int(input())
sport = input()

fitness_card_dict = {
    "m": {"Gym": 42, "Boxing": 41, "Yoga": 45, "Zumba": 34, "Dances": 51, "Pilates": 39},
    "f": {"Gym": 35, "Boxing": 37, "Yoga": 42, "Zumba": 31, "Dances": 53, "Pilates": 37}
}

if age > 19:
    price = fitness_card_dict[sex][sport]
else:
    price = fitness_card_dict[sex][sport] * 0.8

diff = price - budget
if budget >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")