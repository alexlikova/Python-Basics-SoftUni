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

"""

start_number = int(input())
end_number = int(input())
magic_number = int(input())

counter_combination = 0
magic_number_match = False
for start in range(start_number, end_number + 1):
    for end in range(start_number, end_number + 1):
        counter_combination += 1
        sum = start + end
        if sum == magic_number:
            magic_number_match = True
            break
    if sum == magic_number:
        magic_number_match = True
        break
if magic_number_match:
    print(f"Combination N:{counter_combination} ({start} + {end} = {magic_number})")
else:
    print(f"{counter_combination} combinations - neither equals {magic_number}")


"""