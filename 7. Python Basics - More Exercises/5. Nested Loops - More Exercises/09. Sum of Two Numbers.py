start, end, magic_number = [int(input()) for _ in range(3)]

counter = 0
magic_number_found = False

for a in range(start, end + 1):
    for b in range(start, end + 1):
        counter += 1
        if a + b == magic_number:
            magic_number_found = True
            print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
            exit()
print(f"{counter} combinations - neither equals {magic_number}")

