width = int(input())
length = int(input())
high = int(input())
text = input()

free_space = width * length * high

while text != "Done":
    volume = int(text)
    free_space -= volume
    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space):.0f} Cubic meters more.")
        break

    text = input()

else:
    print(f"{free_space:.0f} Cubic meters left.")