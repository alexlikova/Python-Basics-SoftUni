visitors = int(input())

fitness_center_dict = {"Back": 0, "Chest": 0, "Legs": 0, "Abs": 0, "Protein shake": 0, "Protein bar": 0}
count = 0
for number in range(1, visitors + 1):
    command = input()

    if command in fitness_center_dict:
        fitness_center_dict[command] += 1
    else:
        print(input(f"Please, type something else: "))
    if command == "Protein shake" or command == "Protein bar":
        count += 1

for key, value in fitness_center_dict.items():
    print(f"{value} - {key.lower()}")

print(f"{((visitors - count) / visitors * 100):.2f}% - work out")
print(f"{count / visitors * 100:.2f}% - protein")
