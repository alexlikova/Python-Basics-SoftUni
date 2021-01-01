painted_eggs = int(input())

easter_eggs_colours_dict = {"red": 0, "orange": 0, "blue": 0, "green": 0}

for egg in range(1, painted_eggs + 1):
    what_colour_egg = input()

    if what_colour_egg in easter_eggs_colours_dict:
        easter_eggs_colours_dict[what_colour_egg] += 1

max_number_of_colour = max(easter_eggs_colours_dict.values())
max_colour_name = max(easter_eggs_colours_dict, key=lambda key: easter_eggs_colours_dict[key])
for key, value in easter_eggs_colours_dict.items():
    print(f"{key.title()} eggs: {value}")

print(f"Max eggs: {max_number_of_colour} -> {max_colour_name}")

"""
loop = int(input())
eggs_dict = {'red': 0, 'orange': 0, 'blue': 0, 'green': 0}

for _ in range(loop):
    color = input()
    eggs_dict[color] += 1

print(f'Red eggs: {eggs_dict["red"]}')
print(f'Orange eggs: {eggs_dict["orange"]}')
print(f'Blue eggs: {eggs_dict["blue"]}')
print(f'Green eggs: {eggs_dict["green"]}')

eggs_dict = sorted(eggs_dict.items(), key= lambda x: -x[1])[0]
print(f'Max eggs: {eggs_dict[1]} -> {eggs_dict[0]}')
"""