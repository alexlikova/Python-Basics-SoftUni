fist_number, second_number, third_number = [int(input()) for _ in range(3)]

if 1 <= fist_number <= 9 and 1 <= second_number <= 9 and 1 <= third_number <= 9:
    for a in range(2, fist_number + 1, 2):
        for b in range(2, second_number + 1):
            for c in range(2, third_number + 1, 2):
                if b == 2 or b == 3 or b == 5 or b == 7:
                    print(f"{a} {b} {c}")
else:
    print(input(f"Needs to be between 1 and 9: "))
