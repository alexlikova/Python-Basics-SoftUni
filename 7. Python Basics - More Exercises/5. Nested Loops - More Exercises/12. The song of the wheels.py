m = int(input())


furthNum = False
counter = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                magic_number = a * b + c * d
                if a < b and c > d and magic_number == m:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        furthNum = True
                        password = f"{a}{b}{c}{d}"

print()
if furthNum:
    print(f"Password: {password}")
else:
    print("No!")


