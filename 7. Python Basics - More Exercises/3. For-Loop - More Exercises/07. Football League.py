"""
#stadium_capacity = int(input())
#all_fans = int(input())

stadium_capacity, all_fans = [int(input()) for _ in range(2)]

counter_dict = {"A": 0, "B": 0, "V": 0, "G": 0}

for letter in range(all_fans):
    sector = input()
    if sector in counter_dict:
        if sector == "A":
            counter_dict["A"] += 1
        elif sector == "B":
            counter_dict["B"] += 1
        elif sector == "V":
            counter_dict["V"] += 1
        elif sector == "G":
            counter_dict["G"] += 1
        else:
            print(f"Error, this sector does not exist! Try to type: A, B, V or G: ")
    else:
        print(f"This sector does not exist. Try A, B, V, or G: ")

for key, value in counter_dict.items():
    print(f"{value / all_fans * 100:.2f}%")

print(f"{all_fans / stadium_capacity * 100:.2f}%")
"""
"""

stadium = int(input())
fens = int(input())
sectors_list = [input() for _ in range(fens)]

print(f'{sectors_list.count("A") / fens * 100:.2f}%')
print(f'{sectors_list.count("B") / fens * 100:.2f}%')
print(f'{sectors_list.count("V") / fens * 100:.2f}%')
print(f'{sectors_list.count("G") / fens * 100:.2f}%')
print(f'{fens / stadium * 100:.2f}%')

"""

stadium_capacity, all_fans = [int(input()) for _ in range(2)]

counter_dict = {"A": 0, "B": 0, "V": 0, "G": 0}

for letter in range(all_fans):
    sector = input()
    if sector in counter_dict:
        if sector == "A":
            counter_dict["A"] += 1
        elif sector == "B":
            counter_dict["B"] += 1
        elif sector == "V":
            counter_dict["V"] += 1
        elif sector == "G":
            counter_dict["G"] += 1
        else:
            print(f"Error, this sector does not exist! Try to type: A, B, V or G: ")
    else:
        print(f"This sector does not exist. Try A, B, V, or G: ")

for key, value in counter_dict.items():
    print(f"{value / all_fans * 100:.2f}%")

print(f"{all_fans / stadium_capacity * 100:.2f}%")
