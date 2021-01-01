n = int(input())

number_for_printing = 1

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(f"{number_for_printing}", end=" ")
        number_for_printing += 1
        if number_for_printing > n:
            break
    if number_for_printing > n:
        break
    print()